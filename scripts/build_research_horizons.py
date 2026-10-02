#!/usr/bin/env python3
"""Build the fixed broad-horizons review and an offline, self-contained reader.

Requires Python-Markdown and Node.js; vendored KaTeX renders formulas offline.
"""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import io
import json
import subprocess
from pathlib import Path

import markdown
from research_math import render_md, math_styles, math_inputs, VERSION as KATEX_VERSION
from research_delivery import package_pages, delivery_inputs, as_bytes

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/research_synthesis/2026-10-02-broader-horizons'
NOTEBOOK_JS = ROOT / 'scripts/research_notebook.js'
NOTEBOOK_CSS = ROOT / 'scripts/research_notebook.css'
TEMPLATE = ROOT / 'scripts/research_horizons.html'
DATE = '2026-10-02'
TRACKS = ['ai_foundations', 'ai_reasoning_systems', 'pde_numerics', 'bridge']
NAMES = {'ai_foundations': 'AI 基础与生成', 'ai_reasoning_systems': 'AI 推理与行动',
         'pde_numerics': 'PDE 数值方法', 'bridge': '跨域机制与学科背景'}
LEVELS = {'fulltext_sections': '正文相关章节', 'book_sections': '书籍部分章节',
          'abstract': '仅摘要', 'official_documentation': '官方文档或目录'}
CHAPTERS = [
    ('research_update.md', '本轮更新与机制连接'),
    ('RESEARCH_HORIZONS.zh-CN.md', '总览与研究地图'),
    ('ai_foundations.md', 'AI 基础与生成'),
    ('ai_reasoning_systems.md', 'AI 推理与行动系统'),
    ('pde_numerics.md', '传统 PDE 数值方法'),
    ('cross_domain.md', '九个跨领域研究问题'),
    ('learning_roadmap.md', '学习与追踪路线'),
    ('coverage.md', '证据、范围与缺口'),
]
# Connections are review hypotheses, never inferred citation relationships.
BRIDGES = [
    ('X1', 'adaptive_compute', '误差驱动的计算分配', ['ai:test_time_compute', 'ai:process_verification'],
     ['num:aposteriori_dwr', 'num:krylov'], '同容差下，自适应修正能否降低总成本与失败尾部？',
     '纯数值、模型初值加固定修正、手写后验规则、自适应策略。', '小残差大误差未识别，或监测开销抵消收益。'),
    ('X2', 'structure_representation', '保留物理结构的表示', ['ai:self_supervised_representation', 'ai:multimodal_alignment'],
     ['num:compatible_feec', 'num:geometry_mesh'], '跨采样一致性能否在新网格上保留物理量与动力学？',
     '同容量：重构、多视图一致性、结构约束；加入仅平滑的负对照。', '重构变好但通量、能谱或跨网格演化变差。'),
    ('X3', 'solver_components', '求解器内部的共享预训练', ['ai:scaling_laws', 'ai:selective_state_space'],
     ['num:preconditioning', 'num:multigrid'], '不同任务能否复用难消除误差模式与粗空间？',
     'AMG/ILU、学习初值、逐任务预条件、共享预训练；匹配适配预算。', '迭代数下降但总耗时增加，或未见家族失效。'),
    ('X4', 'closed_loop', '适应自身误差的闭环', ['ai:world_models', 'ai:embodied_policies'],
     ['num:time_integration', 'num:conservation_entropy'], '交互训练能否降低部署时的分布漂移？',
     'teacher forcing、噪声增强、可微闭环；匹配训练计算和物理时长。', '仅以过度耗散避免爆炸，或对积分器过拟合。'),
    ('X5', 'compositional_physics', '按物理机制组合专家', ['ai:sparse_experts', 'ai:causal_representation'],
     ['num:domain_decomposition', 'num:stiffness_imex'], '专家承担物理子机制，还是只识别数据集？',
     '数据集路由、物理项路由、稠密模型、数值分裂；留出耦合组合。', '接口破坏守恒，或交换/删除物理项不能改变专家行为。'),
    ('X6', 'probabilistic_inverse', '有明确含义的概率预测', ['ai:diffusion', 'ai:flow_matching', 'ai:calibrated_uncertainty'],
     ['num:inverse_adjoint', 'num:uq'], '条件生成能否刻画可检验的后验与目标量不确定性？',
     '小问题MCMC/集合对照；评分、区间宽度、联合覆盖及物理可行性。', '过宽区间换覆盖，或样本违反物理约束。'),
    ('X7', 'data_error_budget', '数据价值与数值误差预算', ['ai:data_curation', 'ai:scaling_laws'],
     ['num:amr', 'num:multiscale_ap'], '更多数据带来新信息，还是重复了同一求解器偏差？',
     '同生成加训练成本的随机混合、区间平衡和误差课程；跨求解器测试。', '收益仅由更贵标签或泄漏解释。'),
    ('X8', 'algorithm_discovery', '可审查的算法发现', ['ai:symbolic_search_planning', 'ai:tool_agents', 'ai:execution_evaluation'],
     ['num:finite_volume', 'num:conservation_entropy'], '受限程序搜索能否发现通过独立检验的数值组件？',
     '随机/进化/贝叶斯搜索与LLM引导；匹配评估预算，冻结终测反例。', '钻验证器漏洞，或新CFL/间断/硬件条件下失败。'),
    ('X9', 'gradient_interface', '从前向预测到逆设计', ['ai:world_models', 'ai:generalization_theory'],
     ['num:inverse_adjoint', 'num:newton'], '前向准确能否转化为可信梯度和真实设计收益？',
     '方向导数步长扫描、伴随检查、纯数值/冻结代理/混合修正对照。', '代理优化成功但真实求解器目标退化。'),
]


def encode(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2) + '\n'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def csv_text(rows, fields):
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator='\n')
    writer.writeheader()
    for row in rows:
        writer.writerow({k: json.dumps(row.get(k), ensure_ascii=False) if isinstance(row.get(k), (list, dict))
                         else row.get(k, '') for k in fields})
    return stream.getvalue()


def build():
    inputs, sources, concepts, relations, track_stats = {}, {}, {}, [], {}
    for track in TRACKS:
        path = OUT / (track + '_evidence.json')
        inputs[str(path.relative_to(ROOT))] = digest(path.read_bytes())
        data = json.loads(path.read_text())
        track_stats[track] = collections.Counter(s['reading_level'] for s in data['sources'])
        for item in data['sources']:
            for key in ('id', 'title', 'year', 'url', 'accessed_at', 'reading_level', 'locators',
                        'supported_points', 'limitations', 'concept_ids'):
                assert key in item, (path.name, key)
            assert item['reading_level'] in LEVELS
            assert item['accessed_at'] <= DATE
            assert item['year'] is None or 1800 <= item['year'] <= 2026
            assert item['url'].startswith(('http://', 'https://'))
            assert item['locators'] and item['limitations']
            # Duplicate source identities are preserved as reading records, not double-counted works.
            if item['id'] not in sources:
                sources[item['id']] = dict(item, tracks=[track], reading_records=[dict(item, track=track)])
            else:
                sources[item['id']]['tracks'].append(track)
                sources[item['id']]['reading_records'].append(dict(item, track=track))
        for item in data['concepts']:
            assert item['id'] not in concepts, ('duplicate concept', item['id'])
            concepts[item['id']] = dict(item, type='concept', track=track)
        for edge in data['relations']:
            # Reviewed paraphrases can include interpretation; avoid blanket author attribution.
            certainty = 'reviewed_source_summary' if edge['certainty'] == 'source_supported' else edge['certainty']
            relations.append(dict(edge, certainty=certainty, provenance=path.name))

    nodes = list(concepts.values())
    for item in sources.values():
        nodes.append(dict(id=item['id'], label=item['title'], type='source', domain='source',
                          summary='；'.join(item['supported_points']), year=item['year'],
                          reading_level=item['reading_level'], url=item['url']))
        for cid in sorted({c for r in item['reading_records'] for c in r['concept_ids']}):
            assert cid in concepts, (item['id'], cid)
            if not any(e['source'] == item['id'] and e['target'] == cid for e in relations):
                relations.append(dict(source=item['id'], target=cid, type='reviewed_topic',
                                      claim='本次阅读记录涉及该机制；不声称该文首创该概念。',
                                      evidence_ids=[item['id']], certainty='reviewed_source_summary',
                                      provenance='evidence_catalog.json'))

    ideas = []
    for xid, bridge, title, ai, num, question, experiment, failure in BRIDGES:
        bid = 'bridge:' + bridge
        connected = ai + num
        ev = sorted(sid for sid, s in sources.items()
                    if any(set(r['concept_ids']) & set([bid] + connected) for r in s['reading_records']))
        assert ev
        idea = dict(id='hypothesis:' + xid, short_id=xid, type='hypothesis', domain='hypothesis',
                    label=title, summary=question, question=question, experiment=experiment,
                    failure=failure, bridge_id=bid, ai_ids=ai, numerics_ids=num,
                    evidence_ids=ev, status='untested', novelty='not_established')
        ideas.append(idea)
        nodes.append(idea)
        for cid in connected:
            relations.append(dict(source=cid, target=bid, type='cross_domain_analogy',
                                  claim='将此机制与“' + title + '”连接是综述提出的研究类比；成立条件见跨域专题。',
                                  evidence_ids=ev, certainty='synthesis_inference', provenance='cross_domain.md#' + xid))
        relations.append(dict(source=bid, target=idea['id'], type='motivates_hypothesis',
                              claim=question, evidence_ids=ev, certainty='synthesis_inference',
                              provenance='cross_domain.md#' + xid))

    node_ids = {n['id'] for n in nodes}
    assert len(node_ids) == len(nodes)
    for index, edge in enumerate(relations, 1):
        assert edge['source'] in node_ids and edge['target'] in node_ids, edge
        assert edge['evidence_ids'] and set(edge['evidence_ids']) <= sources.keys(), edge
        edge['id'] = f'edge:{index:04d}'
        edge['citation_relation'] = False
        edge['independently_reproduced'] = False
    counts = collections.Counter(s['reading_level'] for s in sources.values())
    recent = [s for s in sources.values() if s['year'] == 2026]
    graph = dict(schema_version='research-horizons-graph-v1', snapshot_date=DATE, nodes=nodes, edges=relations,
                 semantics={'reviewed_source_summary': '选择性原文或官方材料支持的综述概括，不是逐字作者声明。',
                            'synthesis_inference': '综述归纳、跨域类比或待验证假说；不是引用关系或已证因果。',
                            'time': 'year沿用所核对版本的书目年；首发与正式出版可能不同；访问日期不冒充发表日期。',
                            'replication': '未运行来源代码或科学实验；阅读正文相关章节不等于逐页精读。'})
    catalog = dict(schema_version='research-horizons-evidence-v1', snapshot_date=DATE,
                   source_count=len(sources), reading_record_count=sum(len(s['reading_records']) for s in sources.values()),
                   reading_levels=dict(counts), sources=list(sources.values()))
    coverage = ['# 证据、范围与缺口', '', f'研究快照：{DATE}。累计共 {len(sources)} 个唯一来源，'
                f'{catalog["reading_record_count"]} 条阅读记录；图谱 {len(nodes)} 个节点、{len(relations)} 条关系。', '',
                '来源包括论文、作者讲义/书籍及官方文档，不把它们统称为同等深度的论文精读。', '',
                '| 阅读范围 | 唯一来源数 |', '|---|---:|']
    coverage += [f'| {LEVELS[level]} | {counts[level]} |' for level in LEVELS]
    coverage += ['', '| 专题 | 来源记录 | 正文相关节 | 书籍部分章 | 摘要 | 官方文档/目录 |', '|---|---:|---:|---:|---:|---:|']
    for track, stats in track_stats.items():
        coverage.append('| ' + NAMES[track] + ' | ' + ' | '.join(str(v) for v in
                        [sum(stats.values())] + [stats[k] for k in LEVELS]) + ' |')
    coverage += ['', '## 本轮与沿用证据', '',
                 f'- 本轮访问日期为 {DATE} 的唯一来源：{sum(any(r["accessed_at"][:10] == DATE for r in item["reading_records"]) for item in sources.values())}。其余来源保留原访问日期，不宣称本轮重读。',
                 '- 精确检索窗口、真实查询与访问限制见 [search_coverage.json](search_coverage.json)。新增来源包含体系补读，不全是本期发表。',
                 '', '## 边界', '',
                 '- 正文阅读指来源清单里明确标出的机制、实验或讨论章节；未逐页核对所有附录、证明和结果表。',
                 '- 没有复现论文、训练模型或对作者代码作全面审计；X1—X9 都是未验证研究问题，新颖性未确立。',
                 '- 原64个来源的09-19访问日期和阅读范围沿用；本轮新增与复核范围见 research_update.md。PDE主表456个登记身份独立计数，不把登记或继承证据算作本轮重读。',
                 '- 截止日期表示本次调研时间，不表示截至当天的新文献已经穷尽；2026年材料是按问题选取的样本。',
                 '- 年份可能是首发年、正式出版年或书籍版本年；以来源的版本说明为准。动态文档未确证出版年时留空。',
                 '- 实时搜索结果曾出现打不开的全文；降级为摘要/官方目录的来源保留访问限制，不用检索摘要代替正文。',
                 '- 图谱边是知识组织与证据链接；没有提取全体文献的真实引用网络。',
                 '- 现有注册表、历史评分与定时任务未因此扩展；新成果本地生成，未提交或远程发布。', '',
                 '## 2026年来源', '',
                 '以下按本次来源记录列出；这不是“2026最新工作”的完整排行榜。', '']
    for s in recent:
        coverage.append(f'- [{s["title"]}]({s["url"]})：{LEVELS[s["reading_level"]]}；' + '；'.join(s['locators']))
    coverage += ['', '## 逐项可回查清单', '', '| 来源 | 年份 | 核查日期 | 阅读范围 | 实际位置 |', '|---|---:|---|---|---|']
    for s in sources.values():
        locators = '；'.join(s['locators']).replace('|', '\\|')
        coverage.append(f'| [{s["title"].replace("|", "/")}]({s["url"]}) | {s["year"] or "未确定"} | {s["accessed_at"]} | {LEVELS[s["reading_level"]]} | {locators} |')
    coverage += ['', '主要未深读方向及下一轮补充顺序见 [学习与追踪路线](learning_roadmap.md)。', '']
    coverage_text = '\n'.join(coverage)
    chapters = []
    for filename, title in CHAPTERS:
        if filename == 'coverage.md':
            raw = coverage_text
        else:
            path = OUT / filename
            raw = path.read_text()
            inputs[str(path.relative_to(ROOT))] = digest(path.read_bytes())
        chapters.append(dict(filename=filename, title=title, html=render_md(raw)))
    stats = dict(sources=len(sources), concepts=len(concepts), hypotheses=len(ideas), nodes=len(nodes),
                 edges=len(relations), levels=dict(counts), tracks={k: dict(v) for k, v in track_stats.items()})
    update = json.loads((OUT / 'update_manifest.json').read_text())
    assert update['date'] == DATE
    assert all(item['id'] in node_ids for item in update['items'])
    for name in ('update_manifest.json', 'search_coverage.json'):
        path = OUT / name
        inputs[str(path.relative_to(ROOT))] = digest(path.read_bytes())
    payload = dict(date=DATE, update=update, stats=stats, graph=graph, sources=catalog['sources'], ideas=ideas,
                   chapters=chapters, levels=LEVELS, tracks=NAMES)
    template = TEMPLATE.read_text()
    assert template.count('__HORIZONS_DATA__') == 1
    outputs = {
        'coverage.md': coverage_text,
        'evidence_catalog.json': encode(catalog),
        'knowledge_graph.json': encode(graph),
        'nodes.csv': csv_text(nodes, ['id', 'label', 'type', 'domain', 'year', 'summary']),
        'edges.csv': csv_text(relations, ['id', 'source', 'target', 'type', 'claim', 'certainty', 'evidence_ids', 'provenance']),
    }
    payload['downloads'] = {k: v for k, v in outputs.items() if k.endswith(('.json', '.csv'))}
    payload['downloads'].update({name: (OUT / name).read_text() for name in ('update_manifest.json', 'search_coverage.json')})
    safe_data = json.dumps(payload, ensure_ascii=False).replace('<', '\\u003c').replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
    template = template.replace('</head>', math_styles() + '<style>\n' + NOTEBOOK_CSS.read_text() + '</style>\n</head>')
    template = template.replace('</body>', '<script>\n' + NOTEBOOK_JS.read_text() + '</script>\n</body>')
    outputs.update(package_pages(template.replace('__HORIZONS_DATA__', safe_data), payload, 'horizons-data'))
    for path in [TEMPLATE, NOTEBOOK_JS, NOTEBOOK_CSS, Path(__file__).resolve()] + math_inputs() + delivery_inputs():
        inputs[str(path.relative_to(ROOT))] = digest(path.read_bytes())
    head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    manifest = dict(schema_version='research-horizons-build-v1', snapshot_date=DATE, source_head=head,
                    inputs=inputs, outputs={k: digest(as_bytes(v)) for k, v in outputs.items()},
                    delivery='Small online shell, compressed versioned reader data, on-demand downloads; standalone offline.html',
                    stats=stats, dependencies={'Python-Markdown': markdown.__version__, 'KaTeX': KATEX_VERSION},
                    boundary='Local snapshot; no registry changes, publication, experiment or replication implied.')
    outputs['build_manifest.json'] = encode(manifest)
    return outputs, stats


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='verify deterministic outputs without writing')
    args = parser.parse_args()
    outputs, stats = build()
    stale = []
    for name, content in outputs.items():
        path = OUT / name
        if args.check:
            if not path.exists() or path.read_bytes() != as_bytes(content):
                stale.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(as_bytes(content))
    if stale:
        raise SystemExit('Missing or stale outputs: ' + ', '.join(stale))
    print(json.dumps(dict(status='checked' if args.check else 'built', **stats), ensure_ascii=False))


if __name__ == '__main__':
    main()
