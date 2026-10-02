#!/usr/bin/env python3
"""Build a self-contained research atlas from the fixed review snapshot.

Requires Python-Markdown and Node.js; vendored KaTeX renders formulas offline.
"""
from __future__ import annotations

import argparse
import hashlib
import json

import markdown
from research_math import render_md, math_styles, math_inputs, VERSION as KATEX_VERSION
from research_delivery import package_pages, delivery_inputs, as_bytes
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = '2026-10-02'
OUT = ROOT / 'docs/research_synthesis' / DATE
NOTEBOOK_JS = ROOT / 'scripts/research_notebook.js'
NOTEBOOK_CSS = ROOT / 'scripts/research_notebook.css'
TEMPLATE = ROOT / 'scripts/research_atlas.html'
REQUIRED = ('paper_id', 'title', 'scope', 'urls', 'accessed_at', 'evidence_level',
            'source_locators', 'mechanism', 'supported_claims', 'limitations', 'verification_notes')
CHAPTERS = [
    ('research_update.md', '本轮更新与研究线索', '新增身份、原文复核、覆盖缺口与可检验的问题'),
    ('RESEARCH_SYNTHESIS.zh-CN.md', '综合研究总结', '学习对象、发展脉络、研究判断与阅读路线'),
    ('architecture_review.md', '架构与预训练', '从算子到共享预训练、符号与上下文、异构接口'),
    ('evaluation_review.md', '数据与泛化评测', '基准、目标信息、六类迁移轴与最新五篇'),
    ('domain_review.md', '领域与混合求解', '闭合、辐射、EUV、动理学与真实求解接口'),
    ('innovation_agenda.md', '创新问题', '八个假说：机制、控制变量、对照与失败标准'),
    ('corpus_audit.md', '语料与证据审计', '覆盖范围、缺失项、重复候选与输入身份'),
]
STAGES = [
    ('operator', '学习对象', '从解函数到解算子', '把一次求解变为可重复查询的映射；检查离线成本与训练分布。'),
    ('pretrain', '共享训练', '从单族到多物理', '预训练是否提供新任务可复用的结构，需要从零训练和留出任务对照。'),
    ('condition', '任务信息', '符号与上下文', '问题通过方程、参数或示例给出；不同目标信息对应不同能力协议。'),
    ('heterogeneity', '物理接口', '几何、维度与变量', '共享主干不代表输入输出完全共享；统一形状不代表统一语义。'),
    ('reliability', '可信演化', '长时、物理量与分布', '稳定、准确和统计可信分别评测，不能只看一步误差。'),
    ('evaluation', '能力边界', '分轴迁移与总成本', '固定目标信息、预算、指标与物理时长，才能判断何时值得复用。'),
]
IDEAS = [
    ('H1', '跨采样一致性', '统一表示能否在未见采样上保留物理信息？', '固定动力学容量，比较同网格重构、跨采样一致性和物理量约束。', '改善若仅来自平滑或高频损失，假说不成立。'),
    ('H2', '方程与示例的互补性', '模型究竟使用了哪些任务信息？', '符号条件 × 上下文示例 2×2 对照，加错误条件与打乱示例干预。', '条件打乱不影响结果，说明条件未有效使用。'),
    ('H3', '可迁移任务配比', '哪些源任务贡献正迁移，哪些互相干扰？', '等样本、等计算、留出目标家族；比较相关子集与随机子集。', '收益若由目标同源样本增多解释，不能称跨方程复用。'),
    ('H4', '长时物理可信度', '稳定时长是否以牺牲动力学为代价？', '同主干比较多步训练、直接噪声、结构噪声与约束。', '平均场不爆炸却丢失能谱和事件，不算成功。'),
    ('H5', '按误差分配求解', '残差是否足以决定适配和数值回退？', '预测、固定修正、自适应修正与纯数值同容差比较。', '小残差大误差无法识别，则不能宣称可靠控制。'),
    ('H6', '跨物理区间结构', '无量纲条件与极限约束能否支持区间外推？', '留出连续尺度区间，对齐数值误差并比较四类结构。', '仅极限附近正确不能代表有限参数区间也准确。'),
    ('H7', '概率预测的含义', '不确定性来自噪声、观测还是模型失准？', '固定观测、多次参考实现，比较严格评分规则和物理样本。', '靠扩大区间获得覆盖或样本不物理都不成立。'),
    ('H8', '可组合领域模块', '领域机制能否通过明确接口迁移？', '两个相关但不同来源任务，比较逐任务、混合与模块共享。', '离线改善但闭环退化，不能支持模块迁移。'),
]


def encode(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + '\n'


def mechanism_text(value):
    labels = {'representation': '表示', 'conditioning': '条件信息',
              'pretraining_objective': '训练目标', 'generalization_protocol': '泛化协议'}
    if isinstance(value, dict):
        return '；'.join(labels.get(k, k) + '：' + mechanism_text(v) for k, v in value.items())
    if isinstance(value, list):
        return '；'.join(mechanism_text(v) for v in value)
    return '' if value is None else str(value)


def build():
    cards = [json.loads(line) for line in (OUT / 'paper_cards.jsonl').read_text().splitlines()]
    graph = json.loads((OUT / 'knowledge_graph.json').read_text())
    manifest = json.loads((OUT / 'corpus_manifest.json').read_text())
    corpus_ids = {c['paper_id'] for c in cards}
    assert len(corpus_ids) == len(cards)
    reviews = []
    input_names = ['paper_cards.jsonl', 'knowledge_graph.json', 'corpus_manifest.json', 'remote_sync.json']
    for name in ('architecture_evidence.json', 'evaluation_evidence.json', 'domain_evidence.json', 'incremental_evidence.json'):
        input_names.append(name)
        rows = json.loads((OUT / name).read_text())
        assert isinstance(rows, list)
        for record in rows:
            assert all(k in record for k in REQUIRED), (name, record.get('paper_id'))
            assert record['scope'] in ('corpus', 'background')
            assert record['scope'] != 'corpus' or record['paper_id'] in corpus_ids, record['paper_id']
            assert record['evidence_level'] in ('primary_fulltext', 'primary_abstract', 'unavailable')
            assert isinstance(record['urls'], list) and record['urls']
            assert record['accessed_at'][:10] <= DATE
            assert all(u.startswith('https://') for u in record['urls'])
            reviews.append(dict(record, evidence_id=f"review:{len(reviews)+1:03d}", review_file=name))
    # Preserve independent reading records rather than overwriting their differences.
    primary = {'schema_version': 'primary-reading-evidence-v1', 'snapshot_date': DATE,
               'source_head': graph['source_head'], 'record_count': len(reviews),
               'unique_work_ids': len({r['paper_id'] for r in reviews}),
               'reading_boundary': 'Selected methods/evaluation/discussion sections; not page-by-page reading, code review or replication.',
               'records': reviews}
    semantic_nodes, semantic_edges = {}, []
    for r in reviews:
        pid = r['paper_id']
        semantic_nodes[pid] = {'id': pid, 'type': 'paper' if pid in corpus_ids else 'reference_work', 'label': r['title']}
        for kind, values, relation in [('mechanism', [r['mechanism']], 'described_mechanism'),
                                       ('claim', r['supported_claims'], 'reviewed_claim'),
                                       ('limitation', r['limitations'], 'review_scope_limit')]:
            for i, value in enumerate(values):
                cid = f"{r['evidence_id']}:{kind}:{i}"
                semantic_nodes[cid] = {'id': cid, 'type': kind, 'label': mechanism_text(value), 'structured_value': value}
                semantic_edges.append({'source': pid, 'target': cid, 'type': relation,
                                       'certainty': 'review_interpretation' if kind == 'limitation' else 'reviewed_source_summary',
                                       'evidence_id': r['evidence_id'], 'evidence_level': r['evidence_level'],
                                       'urls': r['urls'], 'locators': r['source_locators'],
                                       'independently_reproduced': False})
    for i, (sid, label, title, desc) in enumerate(STAGES):
        nid = 'concept:' + sid
        semantic_nodes[nid] = {'id': nid, 'type': 'concept', 'label': title, 'description': desc}
        if i:
            semantic_edges.append({'source': 'concept:' + STAGES[i-1][0], 'target': nid,
                                   'type': 'conceptual_progression', 'certainty': 'synthesis_inference',
                                   'provenance': 'RESEARCH_SYNTHESIS.zh-CN.md#3', 'citation_relation': False})
    for hid, title, question, experiment, failure in IDEAS:
        nid = 'hypothesis:' + hid
        semantic_nodes[nid] = dict(id=nid, type='hypothesis', label=title, question=question,
                                   experiment=experiment, failure_criterion=failure, status='untested')
        semantic_edges.append({'source': 'concept:evaluation', 'target': nid,
                               'type': 'motivates_question', 'certainty': 'synthesis_inference',
                               'provenance': 'innovation_agenda.md', 'citation_relation': False})
    semantic = {'schema_version': 'research-semantic-graph-v1', 'nodes': list(semantic_nodes.values()),
                'edges': semantic_edges, 'semantics': {
                    'reviewed_source_summary': 'Evidence-backed review summary; may combine author descriptions and reviewer interpretation. Not a verbatim or exclusively author-attributed claim.',
                    'review_interpretation': 'Scope limit identified during selective reading; not necessarily an explicit author statement.',
                    'synthesis_inference': 'Reviewer conceptual connection or untested hypothesis; not a citation or proven causal relationship.',
                    'replication': 'No scientific experiments or source code were executed for these claims.'}}
    assert len(semantic_nodes) == len(semantic['nodes'])
    assert all(e['source'] in semantic_nodes and e['target'] in semantic_nodes for e in semantic_edges)
    evidence_by_id = {}
    for r in reviews:
        evidence_by_id.setdefault(r['paper_id'], []).append(r)
    compact = []
    for c in cards:
        row = {k: c.get(k) for k in ('paper_id', 'title', 'title_display', 'method_summary', 'contribution_summary',
                                    'research_relation', 'abstract', 'sources', 'reading_status', 'verification',
                                    'topic_ids', 'semantic_topics', 'timeline', 'registry_ref', 'arxiv_url',
                                    'official_url', 'first_seen', 'publication_date', 'daily_directions')}
        row['scope'] = 'corpus'
        row['reviews'] = evidence_by_id.get(c['paper_id'], [])
        compact.append(row)
    for node in graph['nodes']:
        if node['type'] == 'reference_work':
            arxiv_id = node['id'].removeprefix('reference:')
            compact.append({'paper_id': node['id'], 'title': node['label'], 'title_display': node['label'],
                            'scope': 'background', 'topic_ids': [], 'semantic_topics': [],
                            'reviews': evidence_by_id.get(arxiv_id, []),
                            'arxiv_url': 'https://arxiv.org/abs/' + arxiv_id.removeprefix('arxiv:'),
                            'sources': ['docs/LANDMARK_MODELS.md'], 'timeline': {'value': None},
                            'verification': 'landmark_reference_only'})
    # Any reviewed background item outside landmark IDs stays visible and separately counted.
    visible = {c['paper_id'].removeprefix('reference:') for c in compact}
    for pid, rs in evidence_by_id.items():
        if pid not in visible:
            compact.append({'paper_id': pid, 'title_display': rs[0]['title'], 'title': rs[0]['title'],
                            'scope': 'background', 'topic_ids': [], 'semantic_topics': [], 'reviews': rs,
                            'sources': [], 'timeline': {'value': None}, 'verification': 'review_reference_only'})
    topics = [{'id': n['id'], 'label': n['label']} for n in graph['nodes'] if n['type'] == 'topic']
    chapters = [dict(filename=filename, title=title, description=description,
                     html=render_md((OUT / filename).read_text()))
                for filename, title, description in CHAPTERS]
    # Keep downloads byte-for-byte equal to their fixed snapshot sources, including
    # the full JSONL evidence fields that are intentionally absent in compact UI data.
    download_names = ['paper_cards.jsonl', 'knowledge_graph.json', 'nodes.csv', 'edges.csv',
                      'corpus_manifest.json', 'remote_sync.json', 'remote_20260916_digest.txt',
                      'architecture_evidence.json', 'evaluation_evidence.json', 'domain_evidence.json',
                      'incremental_evidence.json', 'search_coverage.json', 'update_manifest.json']
    downloads = {name: (OUT / name).read_text() for name in download_names}
    downloads.update({name: (OUT / name).read_text() for name, _, _ in CHAPTERS})
    downloads.update({'primary_evidence.json': encode(primary), 'semantic_graph.json': encode(semantic)})
    input_names = sorted(set(input_names + download_names))
    update = json.loads((OUT / 'update_manifest.json').read_text())
    assert update['date'] == DATE
    assert all(item['id'] in {p['paper_id'] for p in compact} for item in update['items'])
    data = {'date': DATE, 'update': update, 'papers': compact, 'topics': topics, 'primary': primary, 'stages': STAGES, 'ideas': IDEAS,
            'chapters': CHAPTERS, 'articles': chapters, 'downloads': downloads, 'graph_nodes': len(graph['nodes']), 'graph_edges': len(graph['edges']),
            'source_head': graph['source_head'], 'statistics': manifest['statistics']}
    # Presentation-only markup; evidence strings and downloadable sources stay exact.
    math_text = {}
    for paper in compact:
        texts = [paper.get(k) for k in ('method_summary', 'contribution_summary', 'research_relation', 'abstract')]
        texts += [m.get('excerpt') for t in paper.get('semantic_topics', []) for m in t.get('matched_evidence', [])]
        for text in texts:
            if isinstance(text, str) and any(marker in text for marker in ('$', '\\(', '\\[')):
                markup = render_md(text, plain_text=True)
                if 'class="research-math ' in markup:
                    math_text[text] = markup
    data['math_text'] = math_text
    safe_json = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c').replace('&', '\\u0026')
    page = TEMPLATE.read_text().replace('__ATLAS_DATA__', safe_json)
    page = page.replace('</head>', math_styles() + '<style>\n' + NOTEBOOK_CSS.read_text() + '</style>\n</head>')
    page = page.replace('</body>', '<script>\n' + NOTEBOOK_JS.read_text() + '</script>\n</body>')
    outputs = {'primary_evidence.json': encode(primary), 'semantic_graph.json': encode(semantic),
               **package_pages(page, data, 'atlas-data')}
    sources = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
               for p in [OUT/n for n in input_names] + [OUT/c[0] for c in CHAPTERS] + [TEMPLATE, NOTEBOOK_JS, NOTEBOOK_CSS, Path(__file__)] + math_inputs() + delivery_inputs()}
    build_manifest = {'schema_version': 'research-site-build-v1', 'inputs_sha256': sources,
                      'outputs_sha256': {k: hashlib.sha256(as_bytes(v)).hexdigest() for k, v in outputs.items()},
                      'dependencies': {'Python-Markdown': markdown.__version__, 'KaTeX': KATEX_VERSION},
                      'embedded_chapters': len(chapters), 'offline_embedded_downloads': len(downloads),
                      'delivery': 'Small online shell, compressed versioned reader data, on-demand downloads; standalone offline.html',
                      'snapshot_date': DATE, 'corpus_count': len(cards), 'background_count': len(compact)-len(cards),
                      'review_records': len(reviews), 'review_unique_work_ids': primary['unique_work_ids'],
                      'semantic_nodes': len(semantic_nodes), 'semantic_edges': len(semantic_edges),
                      'validation': 'Unique corpus coverage; typed evidence; scoped paper identities; semantic endpoints; deterministic bytes.'}
    outputs['site_build_manifest.json'] = encode(build_manifest)
    return outputs, build_manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    outputs, manifest = build()
    for name, text in outputs.items():
        path = OUT / name
        if args.check:
            if not path.exists() or path.read_bytes() != as_bytes(text):
                raise SystemExit(f'STALE: {path.relative_to(ROOT)}; run python scripts/build_research_site.py')
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(as_bytes(text))
    print(('PASS' if args.check else 'BUILT') + f": {manifest['corpus_count']} corpus identities, "
          f"{manifest['review_records']} reading records, {manifest['semantic_edges']} semantic edges; {len(outputs)} outputs.")


if __name__ == '__main__':
    main()
