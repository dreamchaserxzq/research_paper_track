#!/usr/bin/env python3
"""Build a deterministic, offline evidence graph of the local research corpus.

No registry mutation, network access, model inference, or citation inference. Every
registry identity is retained, including unresolved and content-free identities.
"""
from __future__ import annotations

import argparse
import collections
import csv
import difflib
import hashlib
import io
import json
import re
import subprocess
from pathlib import Path

SNAPSHOT_DATE = '2026-10-02'
OUTPUT = Path('docs/research_synthesis') / SNAPSHOT_DATE
ARXIV = re.compile(r'(?<![\d.])(\d{4}\.\d{4,5})(?:v\d+)?(?!\d)')
CONTENT_FIELDS = ['title', 'title_zh_summary', 'abstract', 'method_summary',
                  'contribution_summary', 'research_relation', 'representation',
                  'conditioning', 'pretraining', 'training_pdes', 'evaluation_pdes',
                  'generalization_axes', 'evaluation', 'limitations']
# These are retrieval rules, not claims that a paper implemented/evaluated a method.
TOPICS = [
 ('representation', '物理场表示与编码', '网格、点云、潜空间、token与压缩表示', r'token|patch|latent|representation|表征|表示|编码|压缩|点云|网格'),
 ('operator_learning', '神经算子与函数空间', '函数到函数映射及谱域/积分算子', r'neural operator|operator learning|DeepONet|\bFNO\b|算子学习|神经算子|Fourier'),
 ('multiphysics_pretraining', '多物理基座与预训练', '多任务联合训练、基座模型与预训练线索', r'foundation model|pre.train|multi.physics|基座|基础模型|预训练|多物理'),
 ('symbolic_conditioning', '方程符号与条件化', '方程结构、参数、初边值条件的显式输入', r'symbolic|equation.condition|PDE.condition|PDEformer|PROSE|符号|方程条件|PDE条件|元信息|条件编码'),
 ('in_context', '上下文算子学习', '利用输入示例推断任务或算子', r'in.context|\bICON\b|\bVICON\b|DeepOSets|上下文|示例对'),
 ('physics_constraints', '物理约束与守恒', 'PDE残差、边界、守恒及物理知情学习', r'physics.informed|\bPINNs?\b|\bPINO\b|conserv|物理约束|物理信息|物理知情|残差|守恒|边界条件'),
 ('geometry', '几何网格与拓扑', '非规则几何、网格、边界与拓扑迁移', r'geometr|mesh|topolog|几何|网格|拓扑|非规则|不规则'),
 ('multiscale', '多尺度与频谱', '空间/时间尺度、频率分解及谱偏差', r'multi.scale|spectral|frequency|Fourier|多尺度|频率|频谱|谱偏差|小尺度'),
 ('long_time', '长时演化与稳定性', '时间推进、rollout误差、稳定性与动力系统', r'long.time|long.horizon|rollout|stabilit|autoregress|长时|稳定性|自回归|误差累积'),
 ('generative', '生成式求解', '扩散、流匹配、生成建模及去噪', r'diffusion model|flow.match|generative|denois|生成式|生成模型|扩散模型|流匹配|去噪'),
 ('uncertainty', '不确定性与统计推断', '概率、贝叶斯、置信区间与随机PDE', r'uncertainty|Bayes|stochastic|confidence|SPDE|不确定|贝叶斯|置信|随机PDE|渐近正态|统计推断'),
 ('data_evaluation', '数据集与评测协议', '数据集、基准、划分、评估与可恢复性', r'benchmark|dataset|PDEBench|PDEArena|The Well|基准|数据集|评测|可恢复|划分'),
 ('adaptation', '迁移适配与泛化', '少样本、微调、OOD与条件泛化', r'adapt|transfer|generaliz|fine.tun|few.shot|zero.shot|LoRA|泛化|迁移|微调|适配|少样本|零样本|分布外'),
 ('hybrid_solvers', '混合求解与模块组合', '经典数值方法和学习模块的耦合/组合', r'hybrid|compositional|multigrid|closure|numerical.solver|混合求解|数值.学习|可微分|组合算子|闭合|数值子|求解器耦合'),
 ('plasma', '等离子体与动力学', '等离子体、聚变、粒子动力学及MHD', r'plasma|tokamak|Vlasov|gyrokinetic|magnetohydro|等离子体|托卡马克|聚变|磁流体|漂移动力'),
 ('radiation_euv', '激光辐射与EUV', '激光等离子体、辐射输运、EUV及原子物理', r'\bEUV\b|radiat|laser|opacity|极紫外|辐射|激光|原子|不透明度'),
 ('theory', '逼近理论与误差分析', '逼近/泛化保证、误差界和可辨识性', r'theorem|theoretical|approximation|convergence|error.bound|理论|定理|误差界|逼近|收敛|可辨识'),
 ('transformers', 'Transformer与序列架构', '注意力、状态空间、Mamba及轴向结构', r'transformer|attention|Mamba|state.space|注意力|状态空间|轴向'),
 ('optimization', '训练优化与采样', '损失平衡、优化器、主动学习与采样策略', r'optimiza|optimizer|sampling|active.learning|loss.weight|训练优化|优化器|损失平衡|主动学习|自适应采样'),
 ('inverse_control', '反问题辨识与控制', '参数反演、系统辨识、同化与最优控制', r'inverse|identification|optimal.control|assimilat|反问题|反演|辨识|同化|最优控制'),
 ('efficiency', '效率与计算扩展', '计算/显存/参数效率与硬件扩展', r'efficien|scalab|memory|speedup|\bcompress(?:ion|ed|ing)?\b|accelerat|效率|显存|加速|稀疏|参数高效'),
 ('scaling', '缩放规律与数据配比', '数据、参数、算力缩放和配比实验', r'scaling.law|data.mixture|compute.optimal|缩放律|缩放规律|数据配比|训练配比|算力最优'),
]


def dump(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + '\n'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def flatten(value):
    if isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=False, sort_keys=True) if value else ''


def norm_title(title):
    return re.sub(r'[^\w\u4e00-\u9fff]+', ' ', (title or '').lower()).strip()


def load_jsonl(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def csv_text(rows, columns):
    buffer = io.StringIO(newline='')
    writer = csv.DictWriter(buffer, fieldnames=columns, extrasaction='ignore', lineterminator='\n')
    writer.writeheader()
    for row in rows:
        writer.writerow({k: json.dumps(row.get(k), ensure_ascii=False, sort_keys=True)
                         if isinstance(row.get(k), (list, dict)) else row.get(k) for k in columns})
    return buffer.getvalue()


def source_ref(root, record, fallback):
    ref = record.get('source_path') or record.get('source_id') or fallback
    if '#' in ref and ref.split('#')[0].endswith('.txt'):
        filename, ident = ref.split('#', 1)
        path = root / filename
        if path.exists():
            for number, line in enumerate(path.read_text().splitlines(), 1):
                if line.strip() == ident:
                    return f'{filename}:{number}'
    return ref if re.search(r':\d+$', ref) else fallback


def provenance_for(card, field, resolved):
    original = card.get('provenance', {}).get(field)
    return {'source_ref': card['registry_ref'], 'underlying_source_ref': resolved.get(original),
            'source_id': original}


def tag_texts(fields):
    tags = []
    for slug, label, definition, pattern in TOPICS:
        evidence = []
        for field, value, provenance in fields:
            text = flatten(value)
            match = re.search(pattern, text, re.I)
            if match:
                evidence.append({'field': field, 'matched_text': match.group(), 'pattern': pattern,
                                 'excerpt': text[max(0, match.start()-65):match.end()+105], **provenance})
        if evidence:
            tags.append({'id': f'topic:{slug}', 'label': label, 'assignment': 'automated_tag',
                         'certainty': 'inferred', 'matched_evidence': evidence[:5]})
    return tags


def title_candidates(cards):
    result = []
    for i, left in enumerate(cards):
        a = norm_title(left['title'])
        if len(a) < 12:
            continue
        for right in cards[i+1:]:
            b = norm_title(right['title'])
            if len(b) < 12 or min(len(a), len(b))/max(len(a), len(b)) < .5:
                continue
            # Quick upper bounds avoid expensive matching on unrelated titles.
            matcher = difflib.SequenceMatcher(None, a, b, autojunk=False)
            if matcher.real_quick_ratio() < .87 or matcher.quick_ratio() < .87:
                continue
            ratio = matcher.ratio()
            ta, tb = set(a.split()), set(b.split())
            jaccard = len(ta & tb) / len(ta | tb)
            if ratio >= .90 or (jaccard >= .82 and len(ta & tb) >= 5):
                result.append({'left': left['paper_id'], 'right': right['paper_id'],
                               'left_title': left['title'], 'right_title': right['title'],
                               'title_similarity': round(ratio, 4), 'token_jaccard': round(jaccard, 4),
                               'relation': 'possible_same_work', 'certainty': 'inferred',
                               'decision': 'not_merged', 'provenance': [left['registry_ref'], right['registry_ref']]})
    return result


def build(root):
    inputs = sorted(set([p for p in (root/'metadata').rglob('*') if p.is_file()] +
                        list((root/'digests').rglob('*.md')) +
                        [root/x for x in ['CLAUDE.md', 'README.md', 'run_log.md', 'run_log_published.md',
                         'docs/TAXONOMY.md', 'docs/PUBLISHED_CRITERIA.md', 'docs/LANDMARK_MODELS.md',
                         'scripts/papertrack.py', 'scripts/build_research_graph.py']]))
    inventory = [{'path': str(path.relative_to(root)), 'bytes': path.stat().st_size,
                  'sha256': sha(path.read_bytes()), 'lines': len(path.read_text().splitlines())} for path in inputs]
    papers = load_jsonl(root/'metadata/papers.jsonl')
    records = load_jsonl(root/'metadata/source_records.jsonl')
    conflicts = load_jsonl(root/'metadata/conflicts.jsonl')
    records_by_id = {record['source_id']: record for record in records}
    resolved = {record['source_id']: source_ref(root, record, f'metadata/source_records.jsonl:{i}')
                for i, record in enumerate(records, 1)}
    record_lines = {record['source_id']: f'metadata/source_records.jsonl:{i}' for i, record in enumerate(records, 1)}
    head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
    digest_paths = sorted((root/'digests').rglob('*.md'))
    aliases = collections.defaultdict(set)
    for paper in papers:
        for ident in paper.get('identifier_aliases', {}).get('arxiv', []):
            aliases[ident].add(paper['paper_id'])
        if paper['arxiv_id']:
            aliases[paper['arxiv_id']].add(paper['paper_id'])
    mentions = collections.defaultdict(list)
    report_inventory = []
    unregistered = collections.defaultdict(list)
    for path in digest_paths:
        rel = str(path.relative_to(root))
        lines = path.read_text().splitlines()
        registered_here, unregistered_here = set(), set()
        for number, line in enumerate(lines, 1):
            for ident in sorted(set(ARXIV.findall(line))):
                if ident in aliases:
                    for pid in sorted(aliases[ident]):
                        mentions[pid].append({'source_ref': f'{rel}:{number}', 'path': rel,
                                              'identifier': ident, 'excerpt': line[:600],
                                              'kind': 'identifier_mention', 'certainty': 'observed_in_local_text'})
                        registered_here.add(pid)
                else:
                    unregistered[ident].append({'source_ref': f'{rel}:{number}', 'excerpt': line[:400]})
                    unregistered_here.add(ident)
            for paper in papers:
                if paper.get('doi') and paper['doi'].lower() in line.lower():
                    mentions[paper['paper_id']].append({'source_ref': f'{rel}:{number}', 'path': rel,
                            'identifier': paper['doi'], 'excerpt': line[:600], 'kind': 'doi_mention',
                            'certainty': 'observed_in_local_text'})
                    registered_here.add(paper['paper_id'])
        report_inventory.append({'path': rel, 'lines': len(lines),
                                 'kind': 'historical_daily' if '/daily/' in rel else 'published_weekly' if '/published/' in rel
                                 else 'pde_fm_daily' if path.name.startswith('PDE-FM-') else 'archive_summary',
                                 'registered_paper_ids_mentioned': sorted(registered_here),
                                 'unregistered_arxiv_ids_mentioned': sorted(unregistered_here)})
    cards = []
    for number, paper in enumerate(papers, 1):
        card = dict(paper)
        card['registry_ref'] = f'metadata/papers.jsonl:{number}'
        card['title_display'] = paper['title'] or paper['title_zh_summary'] or f'标题缺失 [{paper["paper_id"]}]'
        card['resolved_provenance'] = {field: resolved.get(sid) for field, sid in paper['provenance'].items()}
        card['source_records'] = [{'source_id': sid, 'source_ref': resolved[sid],
                                   'source_record_ref': record_lines[sid],
                                   'kind': records_by_id[sid]['source_kind']} for sid in paper['sources']]
        card['local_mentions'] = sorted(mentions[paper['paper_id']], key=lambda x: (x['source_ref'], x['identifier']))
        card['historical_reading_status'] = paper['reading_status']
        card['synthesis_reading_level'] = 'local_record_and_digest_text_only'
        card['content_missing'] = [field for field in CONTENT_FIELDS if not paper.get(field)]
        card['content_coverage'] = 'no_descriptive_content' if not any(paper.get(f) for f in CONTENT_FIELDS[1:]) else 'local_summary_available'
        card['semantic_topics'] = tag_texts([(field, paper.get(field), provenance_for(card, field, resolved))
                                             for field in CONTENT_FIELDS if paper.get(field)])
        card['topic_ids'] = [tag['id'] for tag in card['semantic_topics']]
        arxiv = paper['arxiv_id']
        if arxiv and re.match(r'^\d{4}\.\d{4,5}$', arxiv) and 1 <= int(arxiv[2:4]) <= 12:
            card['timeline'] = {'value': f'20{arxiv[:2]}-{arxiv[2:4]}', 'precision': 'month',
                    'basis': 'arxiv_id_month_inferred', 'is_publication_date': False,
                    'source_ref': card['registry_ref'],
                    'uncertainty': '由注册表arXiv编号推断提交年月；本次未逐篇核验编号与标题对应，不能代替正式发表时间。'}
        elif paper['publication_date']:
            card['timeline'] = {'value': paper['publication_date'], 'precision': 'recorded',
                    'basis': 'publication_date_recorded_unverified', 'is_publication_date': True,
                    'source_ref': card['resolved_provenance'].get('publication_date') or card['registry_ref'],
                    'uncertainty': '沿用本地发表日期，存在冲突时未裁决；未外部复验。'}
        else:
            card['timeline'] = {'value': None, 'precision': None, 'basis': 'unknown', 'is_publication_date': None,
                    'source_ref': card['registry_ref'], 'uncertainty': '缺少可用提交/发表年代；first_seen仅为采集时间。'}
        card['assessment_taxonomy'] = []
        for assessment in paper['assessments']:
            sid = assessment['source_id']
            rec = records_by_id[sid]
            era = 'current_pde_fm' if (rec['source_kind'] == 'event' or
                rec['paper'].get('registry_schema_version') == 'pde-fm-daily') else 'historical_or_scheme_specific'
            card['assessment_taxonomy'].append({**assessment, 'taxonomy_era': era, 'source_ref': resolved[sid]})
        card['conflicts'] = [x for x in conflicts if x['paper_id'] == paper['paper_id']]
        card['knowledge_limit'] = '本卡是已有本地摘要/日报陈述的汇集；自动主题仅供检索，不证明作者实施、跨PDE能力或实验结论。历史阅读状态不提升。'
        cards.append(card)
    duplicate_candidates = title_candidates(cards)
    landmark_rows = []
    for number, line in enumerate((root/'docs/LANDMARK_MODELS.md').read_text().splitlines(), 1):
        found = ARXIV.findall(line)
        if line.startswith('|') and found:
            columns = [x.strip() for x in line.strip('|').split('|')]
            ident = found[0]
            linked = sorted(aliases.get(ident, []))
            title_aliases = []
            names = re.sub('[🏗️📊📈]', '', columns[0]).strip()
            for card in cards:
                title = (card['title'] or '').lower()
                key = names.split('（')[0].strip().lower()
                if key and len(key) >= 4 and re.match(r'^'+re.escape(key)+r'(?:\s*[:：\-(]|$)', title) and card['paper_id'] not in linked:
                    title_aliases.append(card['paper_id'])
            landmark_rows.append({'name': names, 'description': columns[1], 'arxiv_id': ident,
                                   'source_ref': f'docs/LANDMARK_MODELS.md:{number}',
                                   'linked_registry_ids': linked, 'possible_same_work': title_aliases,
                                   'verification': 'historical_landmark_statement_unverified'})
    source_nodes = {}
    def add_source(ref):
        match = re.match(r'^(.*):(\d+)$', ref)
        if not match:
            raise ValueError(f'Unresolved source ref: {ref}')
        path = match[1]
        if path not in source_nodes:
            source_nodes[path] = {'id': 'source:'+path, 'type': 'source', 'label': path, 'path': path,
                                  'certainty': 'local_file_exists'}
        return 'source:'+path
    for report in report_inventory:
        add_source(report['path']+':1')
    nodes = [{'id': f'topic:{slug}', 'type': 'topic', 'label': label, 'definition': definition,
              'classification': 'automated_rule_v1', 'pattern': pattern} for slug, label, definition, pattern in TOPICS]
    edges = []
    for card in cards:
        nodes.append({'id': card['paper_id'], 'type': 'paper', 'label': card['title_display'],
                      'arxiv_id': card['arxiv_id'], 'doi': card['doi'], 'timeline': card['timeline'],
                      'reading_status': card['reading_status'], 'verification': card['verification'],
                      'registry_ref': card['registry_ref'], 'topics': card['topic_ids']})
        for tag in card['semantic_topics']:
            edges.append({'source': card['paper_id'], 'target': tag['id'], 'type': 'tagged_with',
                          'certainty': 'inferred', 'assignment': 'automated_tag',
                          'provenance': tag['matched_evidence']})
        grouped = collections.defaultdict(list)
        for occurrence in card['local_mentions']:
            grouped[occurrence['path']].append(occurrence)
        for path, occurrences in sorted(grouped.items()):
            edges.append({'source': card['paper_id'], 'target': add_source(path+':1'), 'type': 'mentioned_in',
                          'certainty': 'observed_in_local_text', 'provenance': occurrences})
        for record in card['source_records']:
            edges.append({'source': card['paper_id'], 'target': add_source(record['source_ref']), 'type': 'recorded_in',
                          'certainty': 'registry_provenance', 'provenance': [record]})
    for landmark in landmark_rows:
        related = landmark['linked_registry_ids'] or ['reference:arxiv:'+landmark['arxiv_id']]
        if not landmark['linked_registry_ids']:
            fields = [('landmark_description', landmark['description'], {'source_ref': landmark['source_ref']}),
                      ('landmark_name', landmark['name'], {'source_ref': landmark['source_ref']})]
            tags = tag_texts(fields)
            nodes.append({'id': related[0], 'type': 'reference_work', 'label': landmark['name'],
                          'description': landmark['description'], 'arxiv_id': landmark['arxiv_id'],
                          'registry_identity': None, 'certainty': 'historical_landmark_statement_unverified',
                          'possible_same_work': landmark['possible_same_work'], 'topics': [tag['id'] for tag in tags],
                          'timeline': {'value': f'20{landmark["arxiv_id"][:2]}-{landmark["arxiv_id"][2:4]}',
                                       'basis': 'arxiv_id_month_inferred', 'is_publication_date': False}})
            for tag in tags:
                edges.append({'source': related[0], 'target': tag['id'], 'type': 'tagged_with',
                              'certainty': 'inferred', 'assignment': 'automated_tag', 'provenance': tag['matched_evidence']})
            for candidate in landmark['possible_same_work']:
                edges.append({'source': related[0], 'target': candidate, 'type': 'possible_same_work',
                              'certainty': 'inferred_title_alias', 'provenance': [{'source_ref': landmark['source_ref'],
                                  'registry_ref': next(c['registry_ref'] for c in cards if c['paper_id']==candidate),
                                  'rule': 'landmark short name equals leading title name followed by punctuation; no merge'}]})
        for pid in related:
            edges.append({'source': pid, 'target': add_source(landmark['source_ref']), 'type': 'listed_as_landmark',
                          'certainty': 'observed_in_local_text', 'provenance': [landmark]})
    for candidate in duplicate_candidates:
        edges.append({'source': candidate['left'], 'target': candidate['right'], 'type': 'possible_same_work',
                      'certainty': 'inferred_title_similarity', 'provenance': candidate['provenance'],
                      'similarity': candidate['title_similarity'], 'decision': 'not_merged'})
    nodes += list(source_nodes.values())
    # Recorded_in edges can repeat endpoints when multiple rows support an identity;
    # preserve each source row, but assign a deterministic distinct edge identity.
    for edge in edges:
        edge['id'] = 'edge:'+sha(json.dumps(edge, ensure_ascii=False, sort_keys=True).encode())[:24]
    edges = sorted({e['id']: e for e in edges}.values(), key=lambda e: (e['type'], e['source'], e['target'], e['id']))
    nodes.sort(key=lambda n: n['id'])
    graph = {'schema_version': 'research-knowledge-graph-v1', 'snapshot_date': SNAPSHOT_DATE, 'source_head': head,
             'semantics': {'tagged_with': '词面规则命中；inferred，可能只是讨论或对比，不代表实现证据。',
                           'mentioned_in': '报告正文出现身份标识；不等于入选或引用。',
                           'recorded_in': '当前主表保留的来源记录。',
                           'listed_as_landmark': '本地里程碑表陈述；不增加全文核验等级。',
                           'possible_same_work': '标题近似或别名线索，未合并身份。',
                           'citation_edges': 'none; no citation extraction or common-topic-as-citation inference'},
             'nodes': nodes, 'edges': edges}
    stats = {
        'registry_identities': len(cards), 'identity_kinds': dict(collections.Counter(c['paper_id'].split(':')[0] for c in cards)),
        'source_records': len(records), 'source_record_kinds': dict(collections.Counter(r['source_kind'] for r in records)),
        'report_file_ranges': {kind: {'first_path': min(r['path'] for r in report_inventory if r['kind'] == kind), 'last_path': max(r['path'] for r in report_inventory if r['kind'] == kind)} for kind in sorted({r['kind'] for r in report_inventory})},
        'reports': len(report_inventory), 'report_kinds': dict(collections.Counter(r['kind'] for r in report_inventory)),
        'reading_status': dict(collections.Counter(c['reading_status'] or 'null' for c in cards)),
        'verification': dict(collections.Counter(c['verification'] for c in cards)),
        'reported_status': dict(collections.Counter(c['status'] for c in cards)),
        'current_daily_directions_nonexclusive': dict(collections.Counter(d for c in cards for d in c['daily_directions'])),
        'current_direction_labeled_identities': sum(bool(c['daily_directions']) for c in cards),
        'content_present': {f: sum(bool(c.get(f)) for c in cards) for f in CONTENT_FIELDS},
        'missing_title_ids': [c['paper_id'] for c in cards if not c['title']],
        'no_descriptive_content_ids': [c['paper_id'] for c in cards if c['content_coverage']=='no_descriptive_content'],
        'conflicts': len(conflicts), 'identities_with_conflicts': len({x['paper_id'] for x in conflicts}),
        'approximate_title_duplicate_candidates': len(duplicate_candidates),
        'landmark_rows': len(landmark_rows), 'landmark_rows_with_registered_arxiv': sum(bool(x['linked_registry_ids']) for x in landmark_rows),
        'landmark_reference_nodes': sum(n['type']=='reference_work' for n in nodes),
        'unregistered_arxiv_mentions': len(unregistered),
        'topic_counts_nonexclusive': {tag['id']: sum(tag['id'] in c['topic_ids'] for c in cards) for tag in nodes if tag['type']=='topic'},
        'untagged_identities': [c['paper_id'] for c in cards if not c['topic_ids']],
        'timeline_basis': dict(collections.Counter(c['timeline']['basis'] for c in cards)),
        'graph_nodes': len(nodes), 'graph_edges': len(edges),
        'graph_node_types': dict(collections.Counter(n['type'] for n in nodes)),
        'graph_edge_types': dict(collections.Counter(e['type'] for e in edges)),
        'latest_first_seen': max((c['first_seen'] for c in cards if c['first_seen']), default=None),
        'latest_registered_arxiv_month': max((c['timeline']['value'] for c in cards if c['timeline']['basis']=='arxiv_id_month_inferred'), default=None),
    }
    manifest = {'schema_version': 'research-corpus-manifest-v1', 'snapshot_date': SNAPSHOT_DATE,
                'source_head': head, 'scope': f'All {len(cards)} identities in current metadata/papers.jsonl; all {len(report_inventory)} local digests read as UTF-8 text; all metadata files hashed. This graph build does not acquire full texts or execute scientific code.',
                'source_of_truth': 'metadata/papers.jsonl identities; source_records and digests for local statements; TAXONOMY for current direction definitions.',
                'input_inventory': inventory, 'input_inventory_sha256': sha(dump(inventory).encode()),
                'statistics': stats, 'report_inventory': report_inventory, 'landmark_records': landmark_rows,
                'unregistered_arxiv_mentions': [{'arxiv_id': ident, 'occurrences': refs} for ident, refs in sorted(unregistered.items())],
                'approximate_title_duplicate_candidates': duplicate_candidates, 'unresolved_conflicts': conflicts,
                'boundaries': ['No deduplication beyond registry identities; candidates are not merges.',
                               'Historical A/B/C/D and scoring schemes are not recast as current PDE-FM directions.',
                               'first_seen is a collection date, never a publication date.',
                               'Local summaries are historical statements, not independent reproduction or full-text validation.',
                               'Only origin/main corpus identities are included; prior unmerged-branch material is historical context, not additional corpus entries.'],
                'output_hashes': {}}
    markdown = [f'# 全量论文证据卡（{len(cards)} 个主表身份）', '',
        '> 本文逐身份保留现有记录，摘要、方法、贡献和研究关联均是已有本地资料的陈述，不代表本次全文核验。缺失项保持“未记录”。',
        '> 自动主题只表示词面命中，可能来自比较对象或未来展望；禁止据此断言论文实现了该技术。历史 A/B/C/D 不换算为 2026-07-22 后方向。',
        '> 时间轴优先由 arXiv 编号推断提交年月；采集时间 first_seen 与发表时间分列。标题近似候选未合并。', '',
        f'数据来源：`metadata/papers.jsonl`；基准 HEAD `{head}`。完整字段与证据见 [paper_cards.jsonl](paper_cards.jsonl)，审计见 [corpus_audit.md](corpus_audit.md)。', '',
        '## 索引', '']
    for i, card in enumerate(cards, 1):
        markdown.append(f'{i}. [{card["title_display"]}](#paper-{i:03d}) — `{card["paper_id"]}`')
    field_labels = {'abstract':'摘要/已有简述', 'method_summary':'方法要点', 'contribution_summary':'贡献陈述',
                    'research_relation':'与研究主线关联', 'representation':'表示', 'conditioning':'条件化', 'pretraining':'预训练',
                    'training_pdes':'训练 PDE', 'evaluation_pdes':'评测 PDE', 'generalization_axes':'泛化轴',
                    'evaluation':'评测协议', 'limitations':'局限'}
    for i, card in enumerate(cards, 1):
        markdown.extend(['', f'<a id="paper-{i:03d}"></a>', f'## {i:03d}. {card["title_display"]}', '',
                         f'- 身份：`{card["paper_id"]}`；主表位置：`{card["registry_ref"]}`。',
                         f'- 外部入口：{card["arxiv_url"] or card["official_url"] or ("https://doi.org/"+card["doi"] if card["doi"] else "未记录")}。',
                         f'- 作者：{flatten(card["authors"]) or card["author_statement"] or "未记录"}。',
                         f'- 本地状态：`{card["status"]}` / `{card["verification"]}`；历史阅读状态：`{card["reading_status"] or "null"}`；本次仅汇编本地文本。',
                         f'- 年代：{card["timeline"]["value"] or "未知"}（`{card["timeline"]["basis"]}`）；记录发表时间：{card["publication_date"] or "未记录"}；采集时间：{card["first_seen"] or "未记录"}。',
                         f'- 当前日报方向：{"/".join(card["daily_directions"]) or "未记录"}；历史评分方向见机器卡 assessment_taxonomy，未混用。',
                         f'- 主题（automated_tag / inferred）：{"；".join(t["label"] for t in card["semantic_topics"]) or "无规则命中"}。'])
        for field, label in field_labels.items():
            value = flatten(card.get(field))
            ref = card['resolved_provenance'].get(field) or card['registry_ref']
            markdown.extend(['', f'**{label}**：{value or "未记录；不从标题推断。"}' + (f'（来源 `{ref}`）' if value else '')])
        if card['conflicts']:
            markdown.extend(['', '**待核验冲突**：' + '；'.join(f'{x["field"]}: '+flatten(x['alternatives']) for x in card['conflicts'])])
        markdown.extend(['', '**原始来源**：'+'；'.join(f'`{x["source_ref"]}`' for x in card['source_records'])])
        if card['semantic_topics']:
            markdown.extend(['', '**主题命中证据举例**：'])
            for tag in card['semantic_topics']:
                evidence = tag['matched_evidence'][0]
                markdown.append(f'- {tag["label"]} ← `{evidence["field"]}`：{evidence["excerpt"]}（`{evidence.get("underlying_source_ref") or evidence["source_ref"]}`；仅词面关联）。')
    audit = ['# 全量语料审计与知识图谱边界', '', f'快照日期：{SNAPSHOT_DATE}；源代码/语料 HEAD：`{head}`。', '',
        f'本次完整读取主表 **{len(cards)} 个身份**、**{len(records)} 条来源记录**与 **{len(report_inventory)} 份本地 Markdown 报告**；逐字节 SHA-256 覆盖 {len(inventory)} 个输入文件。这里的“全量”指本地登记与报告文本，不是全量论文正文精读或实验复现。', '',
        '已同步 origin/main；同步前后提交见 remote_sync.json。本图以当前 main 登记身份为准，未合并分支不自动并入。旧版的远程补充日报仅保留为历史上下文。', '',
        '## 身份、阅读与内容覆盖', '', '| 项目 | 数量 |', '|---|---:|',
        f'| 主表身份 | {len(cards)} |', f'| arXiv / DOI / unresolved | {stats["identity_kinds"]} |',
        f'| 历史阅读状态 | {stats["reading_status"]} |', f'| 核验标记 | {stats["verification"]} |',
        f'| 本地报告类别 | {stats["report_kinds"]} |', f'| 冲突字段 / 涉及身份 | {len(conflicts)} / {stats["identities_with_conflicts"]} |',
        f'| 近似标题重复候选（未合并） | {len(duplicate_candidates)} |', '',
        f'报告类别计数：{stats["report_kinds"]}。现行PDE-FM日报路径范围：{stats["report_file_ranges"].get("pde_fm_daily")}。目录日期跨度不表示逐日无缺口；检索降级与缺失日见 research_update.md / search_coverage.json。', '',
        '| 字段 | 有记录 | 缺失 |', '|---|---:|---:|']
    for field, count in stats['content_present'].items():
        audit.append(f'| {field} | {count} | {len(cards)-count} |')
    audit.extend(['', '缺失标题与描述的身份：'+', '.join(f'`{x}`' for x in stats['no_descriptive_content_ids'])+'。仅 seen 记录不能提供论文内容，未补写虚构摘要。', '',
        '## 分类与年代', '',
        f'当前日报方向仅使用 daily_directions（已按现行规则保留）：{stats["current_daily_directions_nonexclusive"]}；共 {stats["current_direction_labeled_identities"]} 个身份有现行方向，多标签计数不相加当总数。',
        '2026-07-22 前 A/B/C/D 代表旧 AI-for-PDE×等离子体/EUV 方向；历史 published/legacy 的字母和评分保留为 historical_or_scheme_specific，不映射成现行 A/B/C/D，不跨评分方案排名。',
        f'年代证据：{stats["timeline_basis"]}。arXiv 编号年月标记 arxiv_id_month_inferred；DOI 记录只能沿用其未复验 publication_date；缺失时 null。first_seen 永远只是采集时间。',
        f'最新采集记录为 {stats["latest_first_seen"]}；最新登记 arXiv 月份为 {stats["latest_registered_arxiv_month"]}，均不证明论文实际发表状态。', '',
        '## 里程碑及未入库线索', '',
        f'里程碑表 {len(landmark_rows)} 行：{stats["landmark_rows_with_registered_arxiv"]} 行按 arXiv 标识链接主表，另建 {stats["landmark_reference_nodes"]} 个 reference_work 节点。这 {stats["landmark_reference_nodes"]} 个是“标识未匹配”，不能宣称独立新增论文；如 The Well/PDEArena 可能已使用 DOI/unresolved 身份登记，possible_same_work 边只提示别名。',
        f'全部报告出现 {len(unregistered)} 个未匹配主表的 arXiv 标识，详见 corpus_manifest.json 的 unregistered_arxiv_mentions。它们可含未入选候选、基线、里程碑与检索线索；不计入主表身份总数，不默认新论文。', '',
        '## 知识图谱关系语义', '',
        f'共 {len(nodes)} 节点、{len(edges)} 边。节点类型：{stats["graph_node_types"]}；关系类型：{stats["graph_edge_types"]}。',
        '- tagged_with：透明正则规则产生 automated_tag / inferred，保存匹配字段、文本片段与原始行。提及术语不证明实施了方法。',
        '- mentioned_in：报告出现身份编号或 DOI，不等于入选。recorded_in：当前主表的原始记录来源。',
        '- listed_as_landmark：里程碑表明确列出该工作，仍沿用历史未核验等级。',
        '- possible_same_work：近似标题/短名匹配候选，未合并。',
        '- 本图没有 citation、extends 或 outperforms 边；共同主题、年代先后或日报评价不构成论文引用、继承或同协议性能证据。', '',
        '| 自动主题 | 主表身份数（非互斥） |', '|---|---:|'])
    for slug, label, _, _ in TOPICS:
        audit.append(f'| {label} | {stats["topic_counts_nonexclusive"]["topic:"+slug]} |')
    audit.extend(['', '## 近似标题重复候选（保持原身份）', '', '仅字符串相似检索；候选可能只是相近命名的不同方法（例如 PINO 与 Laplace 算子），不是重复判定。', ''])
    if duplicate_candidates:
        for candidate in duplicate_candidates:
            audit.append(f'- `{candidate["left"]}` ↔ `{candidate["right"]}`；标题相似度 {candidate["title_similarity"]}：{candidate["left_title"]} / {candidate["right_title"]}。')
    else:
        audit.append('当前确定性规则未找到候选；这不构成无重复证明。')
    audit.extend(['', '## 待核验冲突', ''])
    for conflict in conflicts:
        audit.append(f'- `{conflict["paper_id"]}` / `{conflict["field"]}`：{flatten(conflict["alternatives"])}。')
    audit.extend(['', '## 可重复生成与检查', '', '```bash', 'python scripts/build_research_graph.py',
                  'python scripts/build_research_graph.py --check', '```', '',
                  f'--check 离线重建并逐字节比较所有七个输出，验证{len(cards)}身份一对一覆盖、来源路径/行号、图边端点、节点/边ID唯一性、原始输入哈希，以及无引用边。输入或HEAD改变将要求显式重建；不修改正式registry。', '',
                  f'阅读层次：本次全量工作是逐条汇编与文本扫描；主表历史阅读状态为{stats["reading_status"]}，不表示本次逐篇重读。新旧原文核验由独立 evidence 文件与访问日期记录，未写回主表。', ''])
    outputs = {
        'paper_cards.jsonl': ''.join(json.dumps(card, ensure_ascii=False, sort_keys=True)+'\n' for card in cards),
        'knowledge_graph.json': dump(graph),
        'nodes.csv': csv_text(nodes, ['id', 'type', 'label', 'arxiv_id', 'doi', 'timeline', 'reading_status', 'verification', 'path', 'topics']),
        'edges.csv': csv_text(edges, ['id', 'source', 'target', 'type', 'certainty', 'assignment', 'provenance']),
        'ALL_PAPERS.md': '\n'.join(markdown)+'\n', 'corpus_audit.md': '\n'.join(audit)+'\n'}
    manifest['output_hashes'] = {name: sha(content.encode()) for name, content in sorted(outputs.items())}
    outputs['corpus_manifest.json'] = dump(manifest)
    validate(root, cards, graph, manifest)
    return outputs, stats


def validate(root, cards, graph, manifest):
    registered = [x['paper_id'] for x in load_jsonl(root/'metadata/papers.jsonl')]
    assert sorted(registered) == sorted(c['paper_id'] for c in cards), 'registry coverage mismatch'
    assert len({c['paper_id'] for c in cards}) == len(cards), 'duplicate paper identities'
    node_ids = [n['id'] for n in graph['nodes']]
    assert len(node_ids) == len(set(node_ids)), 'duplicate node IDs'
    edge_ids = [e['id'] for e in graph['edges']]
    assert len(edge_ids) == len(set(edge_ids)), 'duplicate edge IDs'
    node_set = set(node_ids)
    for edge in graph['edges']:
        assert edge['source'] in node_set and edge['target'] in node_set, 'dangling endpoint'
        assert edge.get('provenance'), 'missing edge provenance'
        assert edge['type'] not in {'cites', 'citation', 'extends', 'outperforms'}, 'unsupported claim edge'
    inventory = manifest['input_inventory']
    counts = {}
    for item in inventory:
        path = root/item['path']
        assert sha(path.read_bytes()) == item['sha256'], 'input changed while building'
        counts[item['path']] = item['lines']
    def walk(value):
        if isinstance(value, dict):
            for key, val in value.items():
                if (key.endswith('source_ref') or key in {'registry_ref', 'source_record_ref'}) and val:
                    match = re.match(r'^(.*):(\d+)$', val)
                    assert match and match[1] in counts and 1 <= int(match[2]) <= counts[match[1]], f'invalid source location {val}'
                walk(val)
        elif isinstance(value, list):
            for val in value:
                walk(val)
    walk(cards)
    walk(graph)
    assert sha(dump(inventory).encode()) == manifest['input_inventory_sha256']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Rebuild in memory; validate and compare committed/local artifacts without writing.')
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    outputs, stats = build(root)
    directory = root/OUTPUT
    if args.check:
        mismatches = [name for name, content in outputs.items() if not (directory/name).exists() or (directory/name).read_bytes() != content.encode()]
        if mismatches:
            raise SystemExit('Stale or missing outputs: '+', '.join(mismatches))
        print(f'PASS: {stats["registry_identities"]} identities; {stats["reports"]} reports; {stats["graph_nodes"]} nodes; {stats["graph_edges"]} edges; input hashes, references, uniqueness, endpoint and deterministic-output checks.')
    else:
        directory.mkdir(parents=True, exist_ok=True)
        for name, content in outputs.items():
            (directory/name).write_text(content)
        print(json.dumps(stats, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
