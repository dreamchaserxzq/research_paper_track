/* Local-only reading notebook, embedded after the host workbench's script. */
(() => {
  'use strict';
  const host = window.researchAtlas || window.researchHorizons;
  if (!host) return;
  const atlas = Boolean(window.researchAtlas);
  const workbench = atlas ? 'pde-atlas-2026-09-19' : 'research-horizons-2026-09-19';
  const storageKey = 'research-notebook:' + workbench;
  const schema = 'research-personal-notebook-v1';
  const maxNote = 4000;
  const statuses = { unread: '待读', reading: '阅读中', read: '已读' };
  const items = new Map((atlas ? host.data.papers : host.data.graph.nodes).map(p => [
    atlas ? p.paper_id : p.id,
    { id: atlas ? p.paper_id : p.id, title: atlas ? (p.title_display || p.title || p.paper_id) : p.label,
      type: atlas ? '论文 / 参考' : ({ source: '来源', concept: '概念', hypothesis: '研究问题' }[p.type] || '节点') }
  ]));
  const entries = new Map();
  let expectedRaw, storageConflict = false;
  let storageProblem = '', corruptStorage = false, activeId = '', lastFocus = null, undoId = '', pendingImport = null;
  const el = (tag, cls, value) => {
    const node = document.createElement(tag);
    if (cls) node.className = cls;
    if (value !== undefined) node.textContent = value;
    return node;
  };
  const button = (label, fn, cls = '') => {
    const node = el('button', cls, label); node.type = 'button'; node.addEventListener('click', fn); return node;
  };
  const dateNow = () => new Date().toISOString();
  const normalize = input => {
    if (!input || typeof input !== 'object' || input.schema_version !== schema || input.workbench !== workbench || !Array.isArray(input.entries)) {
      throw new Error('文件格式或工作台不匹配。请导入本工作台导出的 JSON。');
    }
    if (input.entries.length > items.size) throw new Error('条目数量超出本工作台范围。');
    const seen = new Set();
    return input.entries.map(row => {
      if (!row || typeof row !== 'object' || typeof row.id !== 'string' || !items.has(row.id) || seen.has(row.id)) throw new Error('包含未知或重复的条目 ID，未导入任何内容。');
      if (!Object.hasOwn(statuses, row.status) || typeof row.note !== 'string' || row.note.length > maxNote || typeof row.archived !== 'boolean') throw new Error('个人状态、笔记长度或归档字段无效，未导入任何内容。');
      for (const key of ['created_at', 'updated_at']) {
        if (typeof row[key] !== 'string' || row[key].length > 40 || !Number.isFinite(Date.parse(row[key]))) throw new Error('条目日期格式无效，未导入任何内容。');
      }
      seen.add(row.id);
      return { id: row.id, status: row.status, note: row.note, archived: row.archived, created_at: row.created_at, updated_at: row.updated_at };
    });
  };
  try {
    const saved = localStorage.getItem(storageKey);
    expectedRaw = saved;
    if (saved !== null) {
      try { normalize(JSON.parse(saved)).forEach(row => entries.set(row.id, row)); }
      catch (_) { corruptStorage = true; storageProblem = '检测到无法读取的本机清单，原始数据未覆盖。当前修改只保留在本次页面，请导出 JSON 备份。'; }
    }
  } catch (_) { storageProblem = '浏览器未允许读取本机存储。当前修改只保留在本次页面，请导出 JSON 备份。'; }
  const snapshot = () => ({ schema_version: schema, workbench, exported_at: dateNow(),
    boundary: 'Personal reading marks and notes only; not source verification or research evidence.',
    entries: [...entries.values()].map(row => ({ ...row, title: items.get(row.id).title })) });

  const openButton = button('', () => open(), 'notebook-open');
  openButton.id = 'notebook-open';
  openButton.setAttribute('aria-haspopup', 'dialog');
  (document.querySelector('.top-actions') || document.body).append(openButton);
  document.querySelector('.topbar')?.classList.add('has-notebook');
  const dialog = el('dialog', 'notebook-dialog');
  dialog.id = 'research-notebook';
  dialog.setAttribute('aria-labelledby', 'notebook-title');
  const layout = el('div', 'notebook-layout');
  const header = el('header', 'notebook-header');
  const titleBlock = el('div');
  titleBlock.append(el('span', 'notebook-kicker', 'MY RESEARCH / 个人阅读空间'));
  const title = el('h2', '', '阅读清单与笔记'); title.id = 'notebook-title'; titleBlock.append(title);
  const closeButton = button('关闭', () => dialog.close(), 'notebook-close'); closeButton.setAttribute('aria-label', '关闭阅读清单');
  header.append(titleBlock, closeButton);
  const boundary = el('p', 'notebook-boundary', '只记录在当前浏览器，后续版本沿用本知识库的清单；个人“已读”标记不改变来源核查证据。可导出备份。查看旧快照后，请回到新版继续编辑笔记。');
  const storageNotice = el('p', 'notebook-warning'); storageNotice.id = 'notebook-storage'; storageNotice.setAttribute('role', 'status');
  const tools = el('div', 'notebook-tools');
  const query = el('input'); query.type = 'search'; query.placeholder = '搜索标题、ID 或个人笔记…'; query.setAttribute('aria-label', '搜索个人清单'); query.id = 'notebook-query';
  const filter = el('select'); filter.id = 'notebook-filter'; filter.setAttribute('aria-label', '筛选个人阅读状态');
  for (const [value, label] of [['active', '当前清单'], ...Object.entries(statuses), ['archived', '已移出 · 保留笔记']]) {
    const option = el('option', '', label); option.value = value; filter.append(option);
  }
  tools.append(query, filter);
  const body = el('div', 'notebook-body');
  const list = el('div', 'notebook-list'); list.id = 'notebook-list'; list.setAttribute('aria-label', '个人清单条目');
  const editor = el('section', 'notebook-editor'); editor.id = 'notebook-editor';
  body.append(list, editor);
  const feedback = el('p', 'notebook-feedback'); feedback.id = 'notebook-feedback'; feedback.setAttribute('role', 'status');
  const undo = button('撤销移出', () => {
    const row = entries.get(undoId); if (!row) return;
    row.archived = false; row.updated_at = dateNow(); activeId = row.id; filter.value = 'active'; undoId = ''; undo.hidden = true;
    persist('已恢复到阅读清单。'); render(); editor.focus({ preventScroll: true });
  }); undo.id = 'notebook-undo'; undo.hidden = true;
  const importPreview = el('div', 'notebook-import'); importPreview.id = 'notebook-import-preview'; importPreview.hidden = true;
  const importText = el('p');
  const importConfirm = button('添加新条目，保留现有笔记', () => {
    if (!pendingImport) return;
    let added = 0;
    for (const row of pendingImport) if (!entries.has(row.id)) { entries.set(row.id, row); added++; }
    pendingImport = null; importPreview.hidden = true; persist('已添加 ' + added + ' 条；已有条目的状态与笔记完整保留。'); render(); query.focus({ preventScroll: true });
  }, 'notebook-primary'); importConfirm.id = 'notebook-import-confirm';
  importPreview.append(importText, importConfirm, button('取消', () => { pendingImport = null; importPreview.hidden = true; query.focus({ preventScroll: true }); }));
  const footer = el('footer', 'notebook-footer');
  const fileInput = el('input'); fileInput.type = 'file'; fileInput.accept = '.json,application/json'; fileInput.hidden = true; fileInput.id = 'notebook-import-file';
  footer.append(button('导出 JSON 备份', () => download('json'), 'notebook-export-json'),
    button('导出 Markdown', () => download('md'), 'notebook-export-md'), button('导入 JSON', () => fileInput.click()), fileInput);
  layout.append(header, boundary, storageNotice, tools, body, feedback, undo, importPreview, footer); dialog.append(layout); document.body.append(dialog);

  function notice(message) { feedback.textContent = message; }
  function persist(message) {
    let saved = false;
    if (!corruptStorage && !storageConflict && expectedRaw !== undefined) {
      try {
        const currentRaw = localStorage.getItem(storageKey);
        if (currentRaw !== expectedRaw) {
          storageConflict = true;
          storageProblem = '其他标签页已更新本机清单，本页已停止写入以避免覆盖。当前修改保留在本次页面；请先导出 JSON 备份，再刷新读取最新清单。';
        } else {
          const nextRaw = JSON.stringify(snapshot());
          localStorage.setItem(storageKey, nextRaw); expectedRaw = nextRaw; storageProblem = ''; saved = true;
        }
      } catch (_) { storageProblem = '无法读取或写入本机存储（可能被禁止或空间不足）。修改仅保留在本次页面；关闭或刷新前请导出 JSON 备份。'; }
    }
    storageNotice.textContent = storageProblem; storageNotice.hidden = !storageProblem;
    notice(saved ? message + ' 已存于当前浏览器。' : '修改已保留在本次页面，但未写入浏览器；请立即导出备份。');
    syncButtons(); return saved;
  }
  function add(id) {
    if (!items.has(id)) return;
    let row = entries.get(id);
    if (!row) { row = { id, status: 'unread', note: '', archived: false, created_at: dateNow(), updated_at: dateNow() }; entries.set(id, row); }
    else if (!row.archived) { open(id); return; }
    row.archived = false; row.updated_at = dateNow();
    persist('已加入个人阅读清单。'); open(id);
  }
  function syncButtons() {
    const count = [...entries.values()].filter(row => !row.archived).length;
    openButton.textContent = '阅读清单' + (count ? ' · ' + count : '');
    openButton.setAttribute('aria-label', '打开个人阅读清单，' + count + ' 条');
    for (const control of document.querySelectorAll('[data-notebook-add]')) {
      const row = entries.get(control.dataset.notebookAdd), saved = row && !row.archived;
      const label = saved ? '已在清单 · 写笔记' : '＋ 加入阅读清单';
      if (control.textContent !== label) control.textContent = label;
    }
  }
  function rowsShown() {
    const q = query.value.trim().toLocaleLowerCase();
    return [...entries.values()].filter(row => (filter.value === 'archived' ? row.archived : !row.archived && (filter.value === 'active' || row.status === filter.value))
      && (!q || [row.id, items.get(row.id).title, row.note].join('\n').toLocaleLowerCase().includes(q)))
      .sort((a, b) => b.updated_at.localeCompare(a.updated_at) || a.id.localeCompare(b.id));
  }
  function renderList() {
    const rows = rowsShown(); list.replaceChildren();
    if (!rows.length) list.append(el('p', 'notebook-empty', entries.size ? '没有匹配条目。可调整筛选，或在论文、来源和图谱详情中添加。' : '还没有阅读计划。从论文详情或图谱节点加入第一条，记录值得追问的问题。'));
    for (const row of rows) {
      const item = items.get(row.id), node = button('', () => { activeId = row.id; render(); editor.querySelector('h3')?.focus({ preventScroll: true }); }, 'notebook-item');
      node.dataset.notebookItem = row.id; node.setAttribute('aria-pressed', String(activeId === row.id));
      node.append(el('span', 'notebook-item-meta', item.type + ' · ' + (row.archived ? '已移出' : statuses[row.status])),
        el('strong', '', item.title), el('span', 'notebook-item-note', row.note ? row.note.slice(0, 78) : '写下你的问题、判断与下一步…'));
      list.append(node);
    }
  }
  function render() {
    const rows = rowsShown();
    if (!rows.some(row => row.id === activeId)) activeId = rows[0]?.id || '';
    renderList(); editor.replaceChildren();
    const row = entries.get(activeId); if (!row) { editor.append(el('div', 'notebook-editor-empty', '选择一条记录，整理自己的研究线索。')); return; }
    const item = items.get(row.id);
    editor.tabIndex = -1;
    editor.append(el('span', 'notebook-kicker', item.type + ' / PERSONAL NOTE'), el('h3', '', item.title), el('p', 'notebook-id', row.id));
    editor.querySelector('h3').tabIndex = -1;
    const rowActions = el('div', 'notebook-entry-actions');
    rowActions.append(button('回到条目 ↗', () => {
      dialog.close();
      if (atlas) {
        const paper = host.data.papers.find(p => p.paper_id === row.id);
        document.getElementById('topic').value = ''; document.getElementById('level').value = '';
        document.getElementById('scope').value = paper.scope;
        const search = document.getElementById('query'); search.value = row.id;
        search.dispatchEvent(new Event('input', { bubbles: true }));
        host.show('catalog'); host.choose(row.id);
      }
      else host.focusNode(row.id);
      const heading = document.querySelector(atlas ? '#catalog-detail h3' : '#node-detail h3');
      if (heading) { heading.tabIndex = -1; lastFocus = heading; heading.focus({ preventScroll: true }); }
    }));
    if (row.archived) rowActions.append(button('恢复到清单', () => { row.archived = false; row.updated_at = dateNow(); filter.value = 'active'; persist('已恢复。'); render(); editor.focus({ preventScroll: true }); }));
    else rowActions.append(button('移出清单', () => {
      row.archived = true; row.updated_at = dateNow(); undoId = row.id; undo.hidden = false;
      persist('已移出清单；笔记保留在“已移出”中，可随时恢复。'); render(); undo.focus({ preventScroll: true });
    }, 'notebook-remove'));
    editor.append(rowActions);
    const statusLabel = el('label', 'notebook-field', '我的阅读状态');
    const status = el('select'); status.id = 'notebook-status';
    for (const [value, label] of Object.entries(statuses)) { const option = el('option', '', label); option.value = value; status.append(option); }
    status.value = row.status; statusLabel.append(status); editor.append(statusLabel);
    status.addEventListener('change', () => { row.status = status.value; row.updated_at = dateNow(); persist('个人阅读状态已更新。'); renderList(); });
    const label = el('label', 'notebook-field', '个人笔记');
    const textarea = el('textarea'); textarea.id = 'notebook-note'; textarea.value = row.note; textarea.maxLength = maxNote; textarea.rows = 8;
    textarea.placeholder = '例如：核心机制是什么？与自己的问题如何联系？还需要回查哪些证据？'; label.append(textarea); editor.append(label);
    const hint = el('p', 'notebook-note-hint'); hint.textContent = row.note.length + ' / ' + maxNote + ' 字符 · 输入即尝试保存'; editor.append(hint);
    textarea.addEventListener('input', () => {
      row.note = textarea.value.slice(0, maxNote); row.updated_at = dateNow();
      hint.textContent = row.note.length + ' / ' + maxNote + ' 字符 · 输入即尝试保存';
      persist('个人笔记已更新。'); renderList();
    });
    editor.append(el('p', 'notebook-evidence-note', '这里是你的工作笔记。原始文献、综述结论和核查等级保持独立。'));
  }
  function open(id) {
    if (!dialog.open) { lastFocus = document.activeElement; dialog.showModal(); document.body.classList.add('notebook-modal-open'); }
    if (id) { activeId = id; filter.value = entries.get(id)?.archived ? 'archived' : 'active'; query.value = ''; }
    storageNotice.textContent = storageProblem; storageNotice.hidden = !storageProblem;
    render(); query.focus({ preventScroll: true });
  }
  dialog.addEventListener('close', () => { document.body.classList.remove('notebook-modal-open'); if (lastFocus?.isConnected) lastFocus.focus({ preventScroll: true }); });
  // Native dialog handles Escape and the inert background; keep Tab within the controls.
  dialog.addEventListener('keydown', event => {
    if (event.key !== 'Tab') return;
    const controls = [...dialog.querySelectorAll('button:not([disabled]),a[href],input:not([disabled]):not([type=hidden]),select:not([disabled]),textarea:not([disabled]),[tabindex]:not([tabindex="-1"])')].filter(node => node.getClientRects().length && !node.closest('[hidden]'));
    if (!controls.length) { event.preventDefault(); return; }
    const first = controls[0], last = controls[controls.length - 1], focused = document.activeElement;
    if (event.shiftKey && (focused === first || !controls.includes(focused))) { event.preventDefault(); last.focus(); }
    else if (!event.shiftKey && (focused === last || !controls.includes(focused))) { event.preventDefault(); first.focus(); }
  });
  query.addEventListener('input', render); filter.addEventListener('change', render);
  const markdownText = value => value.replace(/[\\`*_{}\[\]()#+.!<>|~-]/g, '\\$&');
  function download(format) {
    const data = snapshot();
    const content = format === 'json' ? JSON.stringify(data, null, 2) + '\n' : '# 个人阅读清单与笔记\n\n工作台：' + workbench + '\n\n个人标记不代表原始来源核查或研究验证；包含已移出条目以保留笔记。\n\n' + data.entries.map(row =>
      '## ' + markdownText(row.title) + '\n\nID：' + markdownText(row.id) + '\n\n个人状态：' + statuses[row.status] + (row.archived ? '（已移出清单）' : '') + '\n\n' + (row.note ? markdownText(row.note) : '暂无个人笔记。') + '\n').join('\n');
    const blob = new Blob([content], { type: format === 'json' ? 'application/json;charset=utf-8' : 'text/markdown;charset=utf-8' });
    const url = URL.createObjectURL(blob), anchor = el('a'); anchor.href = url; anchor.download = workbench + '-personal-notes.' + format;
    document.body.append(anchor); anchor.click(); anchor.remove(); setTimeout(() => URL.revokeObjectURL(url), 2000);
    notice('已发起下载；请确认文件已保存。备份包含已移出条目的笔记。');
  }
  fileInput.addEventListener('change', async () => {
    const file = fileInput.files?.[0]; fileInput.value = ''; pendingImport = null; importPreview.hidden = true;
    if (!file) return;
    try {
      if (file.size > 16 * 1024 * 1024) throw new Error('文件超过 16 MB，无法导入。');
      const rows = normalize(JSON.parse(await file.text()));
      pendingImport = rows;
      const existing = rows.filter(row => entries.has(row.id)).length;
      importText.textContent = '待导入 ' + rows.length + ' 条：新增 ' + (rows.length - existing) + ' 条，已有 ' + existing + ' 条。已有条目的状态、归档状态和笔记均保留；导入不会覆盖或拼接。';
      importPreview.hidden = false; importConfirm.disabled = rows.length === existing;
      notice('已校验文件，尚未写入。确认后只添加新条目。');
    } catch (error) { notice('导入失败：' + (error instanceof SyntaxError ? 'JSON 格式无效；未修改现有清单。' : error.message)); }
  });

  function attach(container, id) {
    if (!container || !items.has(id) || container.querySelector('[data-notebook-add]')) return;
    const control = button('', () => add(id), 'notebook-add'); control.dataset.notebookAdd = id;
    const heading = container.querySelector('h3'); if (heading) heading.after(control); else container.append(control);
  }
  function enhance(target) {
    if (atlas) { const id = target.querySelector('[data-export-paper]')?.dataset.exportPaper; attach(target, id); }
    else if (target.id === 'node-detail') {
      const id = target.dataset.nodeId || [...target.children].find(node => node.matches('p.small'))?.textContent.trim(); attach(target, id);
    } else for (const card of target.querySelectorAll('.source-card[data-source]')) attach(card, card.dataset.source);
    syncButtons();
  }
  const targets = atlas ? ['network-detail', 'catalog-detail'] : ['node-detail', 'source-list', 'year-list'];
  for (const id of targets) {
    const target = document.getElementById(id); if (!target) continue;
    enhance(target);
    new MutationObserver(() => enhance(target)).observe(target, { childList: true });
  }
  syncButtons();
})();
