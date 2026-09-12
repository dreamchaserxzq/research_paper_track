#!/usr/bin/env python3
"""Deterministic, offline paper registry and report builder (Python standard library)."""
from __future__ import annotations
import argparse
import collections
import datetime as dt
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = 'metadata/history/2026-09-12'
ARXIV = re.compile(r'(?<!\d)(\d{4}\.\d{4,5})(?:v\d+)?(?!\d)')
FIELDS = ('title title_zh_summary authors abstract doi venue publisher publication_type publication_date '
          'official_url arxiv_id code_url data_url training_pdes evaluation_pdes physical_domains '
          'generalization_axes foundation_model_level published_category published_categories '
          'selection_tier representation conditioning pretraining evaluation limitations '
          'research_utility reading_status author_statement method_summary contribution_summary research_relation last_status_check').split()
FORMAL = {'accepted', 'published'}


def dumps(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))


def sha(value):
    return hashlib.sha256(value).hexdigest()


def jsonl(path):
    return [(i, json.loads(line)) for i, line in enumerate(path.read_text().splitlines(), 1) if line.strip()]


def normalize_arxiv(value):
    if not value:
        return None
    match = re.fullmatch(r'(?:https?://arxiv\.org/(?:abs|pdf)/|arxiv:)?(\d{4}\.\d{4,5})(?:v\d+)?(?:\.pdf)?', str(value).strip(), re.I)
    if not match:
        raise ValueError(f'invalid arXiv identifier: {value}')
    return match[1]


def normalize_doi(value):
    if not value:
        return None
    value = re.sub(r'^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)', '', str(value).strip(), flags=re.I).lower()
    if not re.fullmatch(r'10\.\d{4,9}/\S+', value):
        raise ValueError(f'invalid DOI: {value}')
    return value


def norm_text(value):
    return re.sub(r'[^\w]+', '', unicodedata.normalize('NFKC', value or '').casefold())


def timestamp(value):
    if not isinstance(value, str) or not value.endswith(('Z', '+00:00')):
        raise ValueError(f'UTC ISO timestamp required: {value!r}')
    return dt.datetime.fromisoformat(value.replace('Z', '+00:00'))


def utc(value):
    return value.isoformat().replace('+00:00', 'Z')


def evidence_valid(evidence, kinds=None):
    if not isinstance(evidence, list) or not evidence:
        return False
    for item in evidence:
        if not isinstance(item, dict):
            return False
        if not isinstance(item.get('url'), str) or urlparse(item['url']).scheme not in {'http', 'https'} or not urlparse(item['url']).hostname:
            return False
        timestamp(item.get('checked_at'))
    if kinds:
        return any(item.get('kind') in kinds and
                   (urlparse(item['url']).hostname or '').rstrip('.').lower() not in {'arxiv.org', 'www.arxiv.org', 'export.arxiv.org'} and
                   '10.48550/arxiv.' not in unquote(item['url']).lower()
                   for item in evidence)
    return True


def validate_event(event):
    if not isinstance(event, dict):
        raise ValueError('event must be an object')
    if not isinstance(event.get('event_id'), str) or not event['event_id']:
        raise ValueError('event_id is required')
    if event.get('event_type') not in {'discovery', 'assessment', 'publication', 'correction'}:
        raise ValueError('invalid event_type')
    timestamp(event.get('recorded_at'))
    p = event.get('paper')
    if not isinstance(p, dict) or not any(p.get(k) for k in ['arxiv_id', 'doi']):
        raise ValueError('new events require an arxiv_id or DOI; unresolved identities remain pending')
    normalize_arxiv(p.get('arxiv_id'))
    normalize_doi(p.get('doi'))
    for key in ['title', 'abstract', 'venue', 'publisher', 'publication_date', 'official_url', 'code_url', 'data_url']:
        if p.get(key) is not None and (not isinstance(p[key], str) or not p[key].strip()):
            raise ValueError(f'{key} must be a nonempty string or null')
    for key in ['authors', 'training_pdes', 'evaluation_pdes', 'physical_domains', 'generalization_axes']:
        if p.get(key) is not None and (not isinstance(p[key], list) or not all(isinstance(s, str) and s.strip() for s in p[key])):
            raise ValueError(f'{key} must be a string array or null')
    if not evidence_valid(event.get('evidence')):
        raise ValueError('events require dated, linked evidence')
    if any(timestamp(e['checked_at']) > timestamp(event['recorded_at']) for e in event['evidence']):
        raise ValueError('evidence checked after event was recorded')
    status = p.get('status')
    if status is not None and status not in {'preprint', 'submitted', 'unknown', 'accepted', 'published'}:
        raise ValueError('invalid status')
    if status in FORMAL:
        kinds = {'publisher', 'proceedings'} if status == 'published' else {'publisher', 'proceedings', 'acceptance'}
        if not p.get('venue') or not evidence_valid(event['evidence'], kinds):
            raise ValueError('formal status requires venue and publisher/proceedings/acceptance evidence appropriate to status')
    if 'supersedes' in event and (not isinstance(event['supersedes'], list) or not all(isinstance(s, str) for s in event['supersedes'])):
        raise ValueError('supersedes must contain source or event IDs')
    if event.get('supersedes') and event['event_type'] != 'correction':
        raise ValueError('only correction events may supersede source records')
    for key, limit in [('score_relevance', 5), ('score_generality', 3), ('score_innovation', 3), ('score_value', 2), ('score_total', 10)]:
        if p.get(key) is not None and (type(p[key]) not in {int, float} or not 0 <= p[key] <= limit):
            raise ValueError(f'invalid {key}')
    score_keys = {'score_relevance', 'score_generality', 'score_innovation', 'score_value', 'score_total'}
    if score_keys.intersection(p) or 'score_scheme' in p:
        scheme = p.get('score_scheme')
        if scheme not in {'daily-v1', 'published-v2'}:
            raise ValueError('scored events require daily-v1 or published-v2 score_scheme')
        components = ['score_relevance', 'score_generality', 'score_innovation' if scheme == 'daily-v1' else 'score_value']
        if not all(type(p.get(k)) in {int, float} for k in components + ['score_total']):
            raise ValueError('scored events require full numeric breakdown')
        if scheme == 'daily-v1' and p['score_relevance'] > 4:
            raise ValueError('daily relevance score exceeds 4')
        if (scheme == 'daily-v1' and 'score_value' in p) or (scheme == 'published-v2' and 'score_innovation' in p):
            raise ValueError('mixed score schemes')
        if sum(p[k] for k in components) != p['score_total']:
            raise ValueError('score components do not sum to total')
    if event.get('selected') is not None and type(event['selected']) is not bool:
        raise ValueError('selected must be boolean')


def validate_run(run):
    if not isinstance(run, dict): raise ValueError('run must be an object')
    if not re.fullmatch(r'[\w.-]+', run.get('run_id', '')):
        raise ValueError('invalid run_id')
    if run.get('task_type') not in {'daily', 'published', 'status'} or run.get('status') not in {'success', 'degraded', 'failed'}:
        raise ValueError('invalid task_type/status')
    times = {key: timestamp(run.get(key)) for key in ['started_at', 'completed_at', 'coverage_start', 'coverage_end']}
    if times['completed_at'] < times['started_at'] or times['coverage_start'] > times['coverage_end'] or times['coverage_end'] > times['completed_at']:
        raise ValueError('invalid run time ordering')
    previous = run.get('previous_successful_coverage_end')
    if previous is not None and times['coverage_start'] > timestamp(previous):
        raise ValueError('coverage gap after previous successful run')
    queries, candidates = run.get('queries'), run.get('candidates')
    if not isinstance(queries, list) or not isinstance(candidates, list):
        raise ValueError('queries and candidates must be arrays')
    ids = set()
    aliases = {}
    for c in candidates:
        if not isinstance(c, dict): raise ValueError('candidate must be an object')
        aid, doi = normalize_arxiv(c.get('arxiv_id')), normalize_doi(c.get('doi'))
        ident = 'arxiv:' + aid if aid else 'doi:' + doi if doi else None
        if not ident or ident in ids:
            raise ValueError('missing or duplicate candidate ID')
        ids.add(ident)
        for alias in ([aid, 'arxiv:' + aid] if aid else []) + ([doi, 'doi:' + doi] if doi else []):
            if alias in aliases and aliases[alias] != ident: raise ValueError('ambiguous candidate alias')
            aliases[alias] = ident
        discovered = timestamp(c.get('discovered_at'))
        if discovered > times['completed_at']:
            raise ValueError('candidate discovered after run completion')
        for key in ['submitted_at', 'updated_at']:
            if c.get(key) is not None and timestamp(c[key]) > discovered:
                raise ValueError(f'{key} after discovery')
        if c.get('decision') not in {'selected', 'excluded', 'pending'} or not isinstance(c.get('reason'), str) or not c['reason'].strip():
            raise ValueError('candidate decision and reason required')
        kind = c.get('discovery_type')
        if kind not in {'new', 'backfill', 'version_update'}:
            raise ValueError('invalid discovery_type')
        if kind == 'new' and (not c.get('submitted_at') or not times['coverage_start'] <= timestamp(c['submitted_at']) <= times['coverage_end']):
            raise ValueError('new candidate submitted outside coverage (use backfill)')
        if kind == 'version_update' and (not c.get('updated_at') or not times['coverage_start'] <= timestamp(c['updated_at']) <= times['coverage_end']):
            raise ValueError('version update outside coverage')
    queried = set()
    for q in queries:
        if not isinstance(q, dict): raise ValueError('query must be an object')
        if any(not isinstance(q.get(k), str) or not q[k].strip() for k in ['query', 'source']) or q.get('status') not in {'success', 'failed'}:
            raise ValueError('invalid query')
        if q['status'] == 'failed' and (not isinstance(q.get('error'), str) or not q['error'].strip()):
            raise ValueError('failed query requires error')
        if not isinstance(q.get('candidate_ids'), list) or not all(isinstance(i, str) for i in q['candidate_ids']):
            raise ValueError('query candidate_ids required')
        for value in q['candidate_ids']:
            value = value.strip()
            if value not in aliases: raise ValueError('query candidate has no matching record')
            queried.add(aliases[value])
    if queried != ids:
        raise ValueError('query candidates and candidate records differ')
    if run['status'] == 'success' and (not queries or any(q['status'] == 'failed' for q in queries)):
        raise ValueError('successful coverage requires queries and no source failures')
    return {'queries': len(queries), 'candidates': len(ids),
            'selected': sum(c['decision'] == 'selected' for c in candidates),
            'excluded': sum(c['decision'] == 'excluded' for c in candidates),
            'pending': sum(c['decision'] == 'pending' for c in candidates)}


def digest_records(root):
    """Only explicit paper cards before appendix, never incidental baseline/candidate mentions."""
    records = []
    paths = list((root / 'digests').glob('PDE-FM-*.md')) + list((root / 'digests/archive-ai-for-pde/daily').glob('*.md'))
    for path in sorted(paths):
        text = path.read_text()
        main = re.split(r'^#{1,3}\s*(?:附|已有论文更新)', text, flags=re.M)[0]
        date = path.stem[-8:]
        date = f'{date[:4]}-{date[4:6]}-{date[6:]}'
        card_start = r'^(?:#{1,4}[ \t]*)?(?:\*\*)?📄[ \t]*'
        for match in re.finditer(card_start + r'([^\n]+)\n(.*?)(?=' + card_start + r'|^## |\Z)', main, re.M | re.S):
            title, body = match.groups()
            found = re.search(r'^-[ \t]*(?:🔗[ \t]*)?链接[：:][ \t]*(?:\[[^\]]*\]\()?https?://arxiv\.org/abs/(\d{4}\.\d{4,5})(?:v\d+)?', body, re.M)
            if not found:
                continue
            ident = found[1]
            tag = re.search(r'分类标签[：:]\s*([ABCD](?:/[ABCD])*)', body)
            score = re.search(r'评分[：:]\s*(\d+(?:\.\d+)?)/10', body)
            line = main.count('\n', 0, match.start()) + 1
            historical = 'archive-ai-for-pde' in path.parts
            def statement(label):
                m = re.search(label + r'[：:]\s*([^\n]+)', body)
                return m[1] if m else None
            records.append({'source_id': f'{path.relative_to(root)}:{line}', 'priority': 20,
                'source_kind': 'digest', 'paper': {'title': title.strip('* []'), 'arxiv_id': ident,
                'status': 'preprint', 'first_seen': date, 'daily_directions': tag[1].split('/') if tag and not historical else None,
                'registry_schema_version': 'ai-for-pde-historical' if historical else 'pde-fm-daily',
                'author_statement': statement('作者/机构'), 'method_summary': statement('方法要点'),
                'contribution_summary': statement('核心贡献'), 'research_relation': statement('与 PDE 基座大模型研究的关联'),
                'score_total': float(score[1]) if score else None}, 'selected': True})
    return records


def load_inputs(root):
    snapshot = root / SNAPSHOT
    manifest = json.loads((snapshot / 'manifest.json').read_text())
    records = []
    for entry in manifest['files']:
        path = root / entry['snapshot_path']
        if sha(path.read_bytes()) != entry['sha256']:
            raise ValueError(f'historical snapshot changed: {path}')
        if path.suffix != '.jsonl':
            continue
        priority = 70 if path.name == 'published_papers.jsonl' else 10 if path.name == 'paper_registry.jsonl' else 50 if 'updates_' in path.name else 30
        for line, raw in jsonl(path):
            p = dict(raw)
            if p.get('registry_schema_version') == 'bootstrap-v1':
                p['title_zh_summary'] = p.get('title_zh_summary') or p.get('title')
                p['title'] = None
            p['status'] = p.get('status') or p.get('new_status') or p.get('status_update') or 'unknown'
            p['status'] = 'preprint' if p['status'] == 'arxiv' else p['status']
            p['venue'] = p.get('venue') or p.get('formal_venue')
            p['publisher'] = p.get('publisher') or p.get('formal_publisher')
            records.append({'source_id': f'{entry["snapshot_path"]}:{line}', 'priority': priority,
                            'source_kind': 'legacy', 'paper': p, 'raw': raw})
    legacy_seen = {normalize_arxiv(line) for line in (snapshot / 'seen_papers.txt').read_text().splitlines() if line.strip() and not line.startswith('#')}
    for ident in sorted(legacy_seen):
        records.append({'source_id': f'{SNAPSHOT}/seen_papers.txt#{ident}', 'priority': 0,
                        'source_kind': 'legacy_seen', 'paper': {'arxiv_id': ident}, 'selected': True})
    records.extend(digest_records(root))
    event_ids = set()
    for path in sorted((root / 'metadata/inbox').glob('*.jsonl')):
        for line, event in jsonl(path):
            validate_event(event)
            if event['event_id'] in event_ids:
                raise ValueError(f'duplicate event_id: {event["event_id"]}')
            event_ids.add(event['event_id'])
            records.append({'source_id': event['event_id'], 'source_path': f'{path.relative_to(root)}:{line}',
                'source_kind': 'event', 'priority': 100, 'paper': dict(event['paper']), 'raw': event,
                'selected': event.get('selected', False), 'supersedes': event.get('supersedes', []),
                'evidence': event['evidence']})
    all_ids = {r['source_id'] for r in records}
    if len(all_ids) != len(records):
        raise ValueError('source/event IDs must be globally unique')
    for r in records:
        for old in r.get('supersedes', []):
            if old not in all_ids or old == r['source_id']:
                raise ValueError(f'invalid supersedes reference: {old}')
    return records


def identity_groups(records):
    """Strong IDs first. Exact title+first-author only when no strong ID exists."""
    parent = list(range(len(records)))
    superseded = {s for r in records for s in r.get('supersedes', [])}
    active = {i for i, r in enumerate(records) if r['source_id'] not in superseded}
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    def union(i, j):
        parent[find(j)] = find(i)
    def component_ids(indices):
        roots = {find(i) for i in indices}
        members = [r['paper'] for i, r in enumerate(records) if find(i) in roots and i in active]
        return ({p['arxiv_id'] for p in members if p.get('arxiv_id')},
                {p['doi'] for p in members if p.get('doi')})
    by_arxiv, by_doi = collections.defaultdict(list), collections.defaultdict(list)
    for i, r in enumerate(records):
        p = r['paper']
        p['arxiv_id'] = normalize_arxiv(p.get('arxiv_id') or p.get('arxiv_url'))
        p['doi'] = normalize_doi(p.get('doi'))
        if p['arxiv_id']:
            by_arxiv[p['arxiv_id']].append(i)
        if p['doi'] and i in active:
            by_doi[p['doi']].append(i)
    for indices in by_arxiv.values():
        for i in indices[1:]: union(indices[0], i)
    by_source = {r['source_id']: i for i, r in enumerate(records)}
    for i, record in enumerate(records):
        for source in record.get('supersedes', []):
            if source not in by_source: raise ValueError('unknown superseded source')
            j = by_source[source]
            old_aid, new_aid = records[j]['paper']['arxiv_id'], record['paper']['arxiv_id']
            if old_aid and new_aid and old_aid != new_aid:
                raise ValueError('arxiv identity correction requires a separate reviewed migration')
            union(i, j)
    ambiguous = []
    for doi, indices in by_doi.items():
        aids, _ = component_ids(indices)
        if len(aids) > 1:
            ambiguous.append({'field': 'identity', 'doi': doi, 'arxiv_ids': sorted(aids), 'resolution': 'pending'})
            continue
        for i in indices[1:]: union(indices[0], i)
    # Exact title/author can attach a DOI-only record to a unique existing identity.
    title_groups = collections.defaultdict(list)
    for i, r in enumerate(records):
        if i not in active: continue
        p = r['paper']; authors = p.get('authors') or []
        first = authors[0] if authors else p.get('first_author')
        if p.get('title') and first:
            title_groups[(norm_text(p['title']), norm_text(str(first)))].append(i)
    # Evaluate complete connected title proposals first so an ambiguous chain
    # cannot attach a DOI to whichever arxiv happened to be visited first.
    proposed = {find(i): find(i) for i in range(len(records))}
    def proposed_find(i):
        while proposed[i] != i:
            i = proposed[i]
        return i
    for indices in title_groups.values():
        roots = [find(i) for i in indices]
        for r in roots[1:]: proposed[proposed_find(r)] = proposed_find(roots[0])
    proposals = collections.defaultdict(list)
    for i in range(len(records)):
        if i in active: proposals[proposed_find(find(i))].append(i)
    for indices in proposals.values():
        aids, dois = component_ids(indices)
        if len(aids) <= 1 and len(dois) <= 1:
            for i in indices[1:]: union(indices[0], i)
        elif len({find(i) for i in indices}) > 1:
            ambiguous.append({'field': 'identity', 'arxiv_ids': sorted(aids), 'dois': sorted(dois),
                              'resolution': 'pending', 'reason': 'ambiguous exact title/author bridge'})
    grouped = collections.defaultdict(list)
    for i, r in enumerate(records): grouped[find(i)].append(r)
    for group in grouped.values():
        if len({r['paper']['arxiv_id'] for r in group if r['paper'].get('arxiv_id')}) > 1:
            raise ValueError('cross-arxiv identity migration requires separate review')
    return list(grouped.values()), ambiguous


def merge_group(group):
    # A conflicting new assertion needs explicit supersession, not just a later timestamp.
    superseded = {s for r in group for s in r.get('supersedes', [])}
    live = [r for r in group if r['source_id'] not in superseded]
    if not live:
        raise ValueError('cyclic supersession removes all evidence')
    old = [r for r in live if r['source_kind'] != 'event']
    def precedence(r):
        return (r['priority'], (r.get('raw') or {}).get('recorded_at') or r['paper'].get('updated_at') or r['paper'].get('last_status_check') or '', r['source_id'])
    ordered = sorted(live, key=precedence, reverse=True)
    aids = sorted({r['paper']['arxiv_id'] for r in group if r['paper'].get('arxiv_id')})
    dois = sorted({r['paper']['doi'] for r in live if r['paper'].get('doi')})
    ident = 'arxiv:' + aids[0] if aids else 'doi:' + dois[0] if dois else 'unresolved:' + sha(min(r['source_id'] for r in group).encode())[:20]
    result = {'schema_version': 'paper-v1', 'paper_id': ident}
    provenance, conflicts = {}, []
    for field in FIELDS + ['status']:
        candidates = [r for r in ordered if r['paper'].get(field) not in (None, '', [], {})]
        if not candidates:
            result[field] = 'unknown' if field == 'status' else None
            continue
        chosen = candidates[0]
        vals = {dumps(r['paper'][field]) for r in candidates}
        if field in {'doi', 'venue', 'publication_date', 'status'} and len(vals) > 1:
            # Non-formal older status is natural progression, not a conflict.
            formal = [r for r in candidates if r['paper'][field] in FORMAL] if field == 'status' else []
            if field == 'status' and formal:
                chosen = next((r for r in formal if r['paper'][field] == 'published'), formal[0])
                vals = {dumps(chosen['paper'][field])}
            elif field == 'status':
                vals = {dumps(chosen['paper'][field])}
            existing = sorted([r for r in candidates if r in old], key=precedence, reverse=True)
            if len(vals) > 1:
                if chosen['source_kind'] == 'event' and existing:
                    chosen = existing[0]
                conflicts.append({'paper_id': ident, 'field': field, 'resolution': 'pending',
                    'selected_source': chosen['source_id'], 'alternatives': [
                        {'source_id': r['source_id'], 'value': r['paper'][field]} for r in candidates]})
        result[field] = chosen['paper'][field]
        provenance[field] = chosen['source_id']
    result['arxiv_url'] = f'https://arxiv.org/abs/{aids[0]}' if aids else None
    result['arxiv_id'] = aids[0] if aids else None
    result['identifier_aliases'] = {'arxiv': aids, 'doi': dois}
    result['selected_for_digest'] = any(r.get('selected') for r in group)
    result['first_seen'] = min((r['paper']['first_seen'] for r in group if r['paper'].get('first_seen')), default=None)
    result['daily_directions'] = sorted({v for r in group for v in r['paper'].get('daily_directions') or []})
    result['assessments'] = [{'source_id': r['source_id'], 'schema': r['paper'].get('score_scheme') or r['paper'].get('registry_schema_version') or ('daily' if r['source_kind'] == 'digest' else 'legacy_unknown'),
        'scores': {k:v for k,v in r['paper'].items() if k.startswith('score_') and k != 'score_scheme'},
        'score_total': r['paper'].get('score_total'), 'directions': r['paper'].get('directions') or r['paper'].get('daily_directions')} for r in group if r['paper'].get('score_total') is not None]
    result['provenance'] = provenance
    result['sources'] = sorted(r['source_id'] for r in group)
    result['evidence'] = [e for r in live for e in r.get('evidence', [])]
    status_source = next((r for r in live if r['source_id'] == provenance.get('status')), None)
    result['verification'] = 'source_checked' if status_source and status_source['source_kind'] == 'event' else 'legacy_unverified'
    result['conflict_fields'] = sorted(c['field'] for c in conflicts)
    if conflicts:
        result['verification'] = 'conflict_pending'
    return result, conflicts


def escape(value):
    if value is None or value == []:
        return 'unknown'
    if isinstance(value, list): value = ', '.join(str(v) for v in value)
    if isinstance(value, dict): value = dumps(value)
    return str(value).replace('|', '\\|').replace('\n', ' ')


def outputs(root):
    records = load_inputs(root)
    groups, conflicts = identity_groups(records)
    papers = []
    source_groups = {}
    for group in groups:
        p, cs = merge_group(group); papers.append(p); conflicts.extend(cs)
        source_groups.update({r['source_id']: p['paper_id'] for r in group})
    papers.sort(key=lambda p: p['paper_id'])
    if len({p['paper_id'] for p in papers}) != len(papers):
        raise ValueError('duplicate canonical identity')
    for p in papers:
        if any(c.get('field') == 'identity' and (p['arxiv_id'] in c.get('arxiv_ids', []) or p['doi'] == c.get('doi') or p['doi'] in c.get('dois', [])) for c in conflicts):
            p['conflict_fields'] = sorted(set(p['conflict_fields']) | {'identity'})
            p['verification'] = 'conflict_pending'
    for r in records:
        for source in r.get('supersedes', []):
            if source_groups[source] != source_groups[r['source_id']]:
                raise ValueError('supersedes cannot cross paper identities')
    result = {}
    def rows(name, data): result[name] = ''.join(dumps(r) + '\n' for r in data)
    rows('metadata/papers.jsonl', papers)
    rows('metadata/paper_registry.jsonl', papers)
    rows('metadata/published_papers.jsonl', [p for p in papers if p['status'] in FORMAL])
    rows('metadata/conflicts.jsonl', sorted(conflicts, key=dumps))
    rows('metadata/source_records.jsonl', sorted(records, key=lambda r: r['source_id']))
    seen = sorted(p['arxiv_id'] for p in papers if p['arxiv_id'] and p['selected_for_digest'])
    result['seen_papers.txt'] = '# Generated by scripts/papertrack.py build; edit inbox events, not this view.\n' + '\n'.join(seen) + '\n'
    runs = []; run_ids = set()
    for path in sorted((root / 'metadata/runs').glob('*.json')):
        run = json.loads(path.read_text()); counts = validate_run(run)
        if run['run_id'] in run_ids: raise ValueError('duplicate run_id')
        run_ids.add(run['run_id'])
        if run.get('digest_path'):
            target = (root / run['digest_path']).resolve()
            if not target.is_relative_to(root.resolve()) or not target.is_file(): raise ValueError('invalid digest_path')
        selected = [c for c in run['candidates'] if c['decision'] == 'selected']
        if run['status'] == 'success' and not run.get('digest_path'):
            raise ValueError('successful run requires its report path')
        for candidate in selected:
            aid, doi = normalize_arxiv(candidate.get('arxiv_id')), normalize_doi(candidate.get('doi'))
            matches = [p for p in papers if (aid and p['arxiv_id'] == aid) or (doi and doi in p['identifier_aliases']['doi'])]
            if len(matches) != 1:
                raise ValueError('selected run candidate has no unambiguous registry identity')
            if run['task_type'] == 'daily' and not matches[0]['selected_for_digest']:
                raise ValueError('selected daily candidate absent from generated seen set')
        if run['task_type'] == 'daily' and run.get('digest_path'):
            cards = [r for r in records if r['source_kind'] == 'digest' and r['source_id'].rsplit(':', 1)[0] == run['digest_path']]
            reported_ids = {r['paper']['arxiv_id'] for r in cards}
            expected_ids = {normalize_arxiv(c.get('arxiv_id')) for c in selected}
            if reported_ids != expected_ids:
                raise ValueError('daily report cards disagree with selected run candidates')
        runs.append(dict(run, counts=counts))
    for run in runs:
        predecessors = [r for r in runs if r['task_type'] == run['task_type'] and r['status'] == 'success' and
                        timestamp(r['completed_at']) < timestamp(run['started_at'])]
        if predecessors:
            previous = max(timestamp(r['coverage_end']) for r in predecessors)
            if run.get('previous_successful_coverage_end') is None or timestamp(run['previous_successful_coverage_end']) != previous:
                raise ValueError('run does not reference the actual previous successful coverage position')
    rows('metadata/run_index.jsonl', runs)
    # All history remains immutable; current indexes use dates, never historical issue numbers.
    daily = sorted((root / 'digests').glob('PDE-FM-*.md'), reverse=True)
    weekly = sorted((root / 'digests/published').glob('*.md'), reverse=True)
    recovered = {}
    recovery = root / 'metadata/recovery_20260912.json'
    if recovery.exists():
        obj = json.loads(recovery.read_text())
        for entry in obj.get('recovered_digests', []):
            path = entry['restored_path']
            if path: recovered[path] = entry
    cards = digest_records(root); dates_by_id = collections.defaultdict(list)
    for card in cards:
        dates_by_id[card['paper']['arxiv_id']].append(card['paper']['first_seen'])
    repeated = {k: sorted(set(v)) for k, v in dates_by_id.items() if len(set(v)) > 1}
    index = ['# 日报与周报索引', '', '> 按日期排序；历史期数与原始正文保留。补档来源见恢复报告。', '', '## 日报', '', '| 日期 | 日报 | 原报告入选数 |', '|---|---|---:|']
    for path in daily:
        date = path.stem[-8:]; text = path.read_text(); m = re.search(r'本期新增入选[：:]\s*(\d+)', text)
        index.append(f'| {date[:4]}-{date[4:6]}-{date[6:]} | [{path.name}](../{path.relative_to(root)}) | {m[1] if m else "unknown"} |')
    index += ['', '## 正式发表周报', ''] + [f'- [{p.stem}](../{p.relative_to(root)})' for p in weekly]
    index += ['', '[旧方向档案](../digests/archive-ai-for-pde/README.md)', '']
    result['docs/DIGEST_INDEX.md'] = '\n'.join(index)
    # A searchable offline catalog requires no network/library runtime.
    catalog = ['# 论文目录', '', '> 此页由注册表生成。legacy_unverified 表示历史记录尚未重新核验；unknown 不推断补全。', '', '| 论文 | arXiv / DOI | 日报方向 | 报告状态 | 核验 |', '|---|---|---|---|---|']
    for p in papers:
        title = escape(p['title'] or p['title_zh_summary'] or p['paper_id'])
        url = p['arxiv_url'] or ('https://doi.org/' + p['doi'] if p['doi'] else None)
        label = p['arxiv_id'] or p['doi'] or p['paper_id']
        catalog.append(f'| {title} | [{label}]({url}) | {escape(p["daily_directions"])} | {p["status"]} | {p["verification"]} |' if url else f'| {title} | {label} | {escape(p["daily_directions"])} | {p["status"]} | {p["verification"]} |')
    result['docs/PAPER_CATALOG.md'] = '\n'.join(catalog) + '\n'
    landmark_ids = set(ARXIV.findall((root / 'docs/LANDMARK_MODELS.md').read_text()))
    comparison = ['# 重点论文证据对照', '', '> 仅展示仓库已有证据，不把摘要描述补写成已验证的实验事实。详见来源记录。', '', '| 论文 | 模型层级 | 训练 PDE | 评测 PDE | 泛化轴 | 代码 | 核验 |', '|---|---|---|---|---|---|---|']
    for p in papers:
        if p['arxiv_id'] not in landmark_ids: continue
        link = f'[{escape(p["title"] or p["title_zh_summary"] or p["arxiv_id"])}]({p["arxiv_url"]})'
        code = f'[链接]({p["code_url"]})' if p['code_url'] else 'unknown'
        comparison.append('| ' + ' | '.join([link] + [escape(p[k]) for k in ['foundation_model_level','training_pdes','evaluation_pdes','generalization_axes']] + [code,p['verification']]) + ' |')
    comparison += ['', '后续核验字段：表征、条件输入、预训练预算、划分与基线、局限、数据/权重许可证。用带证据的 assessment 事件填写；不要从模型名称推断。', '']
    result['docs/RESEARCH_COMPARISON.md'] = '\n'.join(comparison)
    summary = {'schema_version': 1, 'papers': len(papers), 'selected_arxiv_ids': len(seen),
        'reported_formal': sum(p['status'] in FORMAL for p in papers), 'conflicts': len(conflicts),
        'legacy_unverified': sum(p['verification'] == 'legacy_unverified' for p in papers),
        'missing_title': sum(not p['title'] for p in papers), 'missing_authors': sum(not p['authors'] for p in papers),
        'daily_files': len(daily), 'weekly_files': len(weekly), 'structured_runs': len(runs),
        'historical_repeat_selections': repeated}
    result['metadata/build_summary.json'] = json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True) + '\n'
    prompt_files = ['CLAUDE.md', 'docs/ROUTINE.md', 'docs/ROUTINE_PUBLISHED.md', 'docs/ROUTINE_STATUS_UPDATE.md',
                    'docs/TAXONOMY.md', 'docs/PUBLISHED_CRITERIA.md', 'docs/OPERATIONS.md']
    prompt_hashes = {name: sha((root / name).read_bytes()) for name in prompt_files if (root / name).exists()}
    result['metadata/prompt_manifest.json'] = json.dumps({'schema_version': 1, 'files': prompt_hashes,
        'bundle_sha256': sha(dumps(prompt_hashes).encode()),
        'external_scheduler': {'status': 'unverified', 'checked_at': None, 'deployed_bundle_sha256': None}},
        ensure_ascii=False, indent=2, sort_keys=True) + '\n'
    report = ['# 数据归并质量报告', '', '> 离线归并当前可得证据；未重新联网核验全部历史论文。源快照有 SHA-256 校验，冲突不会丢弃。', '', '| 项目 | 数量 |', '|---|---:|']
    report += [f'| {k} | {v} |' for k,v in summary.items() if isinstance(v, int) and k != 'schema_version']
    report += ['', '## 待核验冲突', '', '完整机器记录见 [conflicts.jsonl](../../metadata/conflicts.jsonl)。当前选值保留主表优先级，不表示冲突已经解决。用 correction 事件明确 supersedes 源记录后才能消除冲突。', '', '| 论文 | 字段 | 处理 |', '|---|---|---|']
    report += [f'| {escape(c.get("paper_id") or c.get("doi"))} | {c["field"]} | pending |' for c in conflicts]
    report += ['', '## 历史重复入选', '', '| arXiv | 原始日期 |', '|---|---|']
    report += [f'| {k} | {", ".join(v)} |' for k,v in sorted(repeated.items())]
    report += ['', '重复出现的原始日报不改写；当前去重集只保留一个 ID。没有结构化运行证据的历史统计不转换成精确查询数量。', '']
    result['docs/reports/DATA_QUALITY.md'] = '\n'.join(report)
    readme = ['# PDE 基座模型与 AI for PDE 论文追踪', '', '追踪架构与预训练、数据与评测、下游适配，以及通用 AI 求解 PDE 方法。', '',
      '[论文目录](docs/PAPER_CATALOG.md) · [重点论文对照](docs/RESEARCH_COMPARISON.md) · [全部日报与周报](docs/DIGEST_INDEX.md) · [操作说明](docs/OPERATIONS.md)', '',
      f'当前注册表 **{len(papers)}** 条；去重集 **{len(seen)}** 个 arXiv ID；**{len(conflicts)}** 项待核验冲突。历史发表状态为记录中的声明，核验程度见各条目。', '',
      '## 最新日报', '', '<!-- DIGEST_START -->', '', '| 日期 | 报告 |', '|---|---|']
    for p in daily[:12]:
        d=p.stem[-8:];readme.append(f'| {d[:4]}-{d[4:6]}-{d[6:]} | [{p.name}]({p.relative_to(root)}) |')
    readme += ['', '<!-- DIGEST_END -->', '', '## 正式发表周报', '', '<!-- PUBLISHED_DIGEST_START -->', '']
    readme += [f'- [{p.stem}]({p.relative_to(root)})' for p in weekly[:12]]
    readme += ['', '<!-- PUBLISHED_DIGEST_END -->', '', '## 运行与数据质量', '',
      '- [遗漏日报恢复记录](docs/RECOVERY_20260912.md)：保留分支原始正文和提交来源。',
      '- [数据质量与冲突报告](docs/reports/DATA_QUALITY.md)：缺失字段、历史重复入选和待核验信息。',
      '- [历史运行日志](run_log.md)与[正式发表日志](run_log_published.md)：原始声明不重写；新运行使用结构化记录。',
      '- 状态回填尚无独立执行证据；本次离线归并不计作联网状态复查。',
      '- 外部调度器当前配置尚未核验。更新仓库提示词后须按操作说明同步部署，才能对后续定时任务生效。', '',
      '## 本地命令', '', '```bash', 'python scripts/papertrack.py build', 'python scripts/papertrack.py check',
      'python -m unittest discover -s tests -v', 'python scripts/papertrack.py search "foundation"',
      'python scripts/publish.py audit-branches', '```', '',
      '## 维护约定', '', '新增论文与修正写入 `metadata/inbox/*.jsonl`；主表、去重集和本页由程序生成。',
      '原始快照保存在 `metadata/history/2026-09-12/`，分周原始文件继续保留作证据。',
      '方向与评分见 [TAXONOMY](docs/TAXONOMY.md)，发表判定见 [PUBLISHED_CRITERIA](docs/PUBLISHED_CRITERIA.md)，发布只暂存明确列出的任务文件。', '']
    result['README.md'] = '\n'.join(readme)
    return result


def check(root):
    expected = outputs(root)
    errors = []
    for name, content in expected.items():
        path = root / name
        if not path.exists() or path.read_text() != content:
            errors.append(f'stale generated file: {name}; run build')
    for path in (root / 'metadata').rglob('*.jsonl'):
        jsonl(path)
    manifest = json.loads((root / SNAPSHOT / 'manifest.json').read_text())
    for entry in manifest['files']:
        original = entry.get('original_path', '')
        if re.fullmatch(r'metadata/(?:published_papers|paper_registry_updates)_\d{4}_W\d{2}\.jsonl', original):
            if sha((root / original).read_bytes()) != entry['sha256']:
                errors.append(f'legacy shard changed; use inbox correction: {original}')
    # Snapshot Markdown retains its original relative paths and is not a live navigation surface.
    for path in root.rglob('*.md'):
        if any(x in path.parts for x in ['.git', '.agents', '.codex', 'history']): continue
        for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^\s)]+)\)', path.read_text()):
            if '://' in target or target.startswith(('#','mailto:')): continue
            dest = path.parent / unquote(target.split('#')[0])
            if not dest.exists(): errors.append(f'broken link {path.relative_to(root)}: {target}')
    recovery = root / 'metadata/recovery_20260912.json'
    if recovery.exists():
        obj = json.loads(recovery.read_text())
        for entry in obj.get('recovered_digests', []):
            name = entry['restored_path']
            if sha((root / name).read_bytes()) != entry['sha256']: errors.append(f'recovered digest modified: {name}')
    if errors: raise ValueError('\n'.join(errors))
    return expected


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ['build', 'check']: sub.add_parser(name)
    search = sub.add_parser('search'); search.add_argument('query')
    coverage = sub.add_parser('coverage'); coverage.add_argument('--task', default='daily', choices=['daily','published','status']); coverage.add_argument('--at', required=True); coverage.add_argument('--overlap-hours', type=int, default=48)
    run = sub.add_parser('validate-run'); run.add_argument('path', type=Path)
    args = parser.parse_args(argv)
    try:
        root = args.root.resolve()
        if args.command == 'build':
            built = outputs(root)
            for name, content in built.items():
                path = root / name; path.parent.mkdir(parents=True, exist_ok=True)
                if not path.exists() or path.read_text() != content:
                    temp = path.with_suffix(path.suffix + '.tmp'); temp.write_text(content); temp.replace(path)
            print(f'Built {len(built)} deterministic views.')
        elif args.command == 'check':
            checked = check(root); print(f'PASS: {len(checked)} generated views, JSONL, snapshot hashes and local links.')
        elif args.command == 'search':
            for _, p in jsonl(root / 'metadata/papers.jsonl'):
                if args.query.casefold() in dumps(p).casefold():
                    print(dumps({k:p[k] for k in ['paper_id','title','title_zh_summary','status','verification','code_url','conflict_fields']}))
        elif args.command == 'validate-run':
            print(dumps(validate_run(json.loads(args.path.read_text()))))
        elif args.command == 'coverage':
            now = timestamp(args.at)
            if args.overlap_hours < 0: raise ValueError('overlap must be nonnegative')
            ends = []
            for path in (root / 'metadata/runs').glob('*.json'):
                item = json.loads(path.read_text()); validate_run(item)
                if item['status'] == 'success' and item['task_type'] == args.task and timestamp(item['coverage_end']) <= now:
                    ends.append(timestamp(item['coverage_end']))
            previous = max(ends) if ends else None
            print(dumps({'coverage_start': utc((previous or now)-dt.timedelta(hours=args.overlap_hours)), 'coverage_end': utc(now),
                         'previous_successful_coverage_end': utc(previous) if previous else None, 'bootstrap': previous is None}))
    except (ValueError, KeyError, OSError, TypeError) as error:
        print(f'ERROR: {error}', file=sys.stderr); return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
