/* Online transport and independently packaged offline data share one UI. */
window.researchAssets = (() => {
  const config = JSON.parse(document.getElementById('research-delivery').textContent);
  const status = document.getElementById('delivery-status');
  let initialized = false, queuedButton = null, noticeTimer;
  const capture = event => {
    const button = event.target.closest('button,[data-read],[data-view]');
    if (!initialized && button) {
      event.preventDefault(); event.stopImmediatePropagation(); queuedButton = button;
    }
  };
  document.addEventListener('click', capture, true);
  const decode = encoded => Uint8Array.from(atob(encoded), c => c.charCodeAt(0));
  async function inflate(bytes) {
    if (!window.DecompressionStream) throw new Error('请使用新版 Edge、Chrome、Firefox 或 Safari 打开此离线文件。');
    return new Response(new Blob([bytes]).stream().pipeThrough(new DecompressionStream('gzip'))).arrayBuffer();
  }
  async function verify(bytes, expected) {
    if (window.crypto?.subtle) {
      const sum = Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', bytes)), x => x.toString(16).padStart(2, '0')).join('');
      if (sum !== expected) throw new Error('资料版本不一致，请刷新页面后重试。');
    }
    return bytes;
  }
  async function fetchBytes(url) {
    const response = await fetch(url, {signal: AbortSignal.timeout(30000)});
    if (!response.ok) throw new Error('资料加载失败（HTTP ' + response.status + '），请检查连接后重试。');
    return response.arrayBuffer();
  }
  const notice = message => {
    clearTimeout(noticeTimer); status.replaceChildren(document.createTextNode(message)); status.hidden = false;
  };
  function fail(error) {
    console.error(error);
    notice(location.protocol === 'file:' && !config.offline
      ? '这是在线入口文件。请通过网站上的“下载完整离线版”保存可独立打开的版本。'
      : '未能载入研究资料。' + (error.message || '请检查连接后重试。'));
    const retry = document.createElement('button'); retry.textContent = '重新加载'; retry.onclick = () => location.reload();
    status.append(retry); initialized = true; document.removeEventListener('click', capture, true);
  }
  async function loadData() {
    let bytes;
    if (config.offline) bytes = await inflate(decode(config.embedded));
    else if (window.DecompressionStream) bytes = await inflate(await fetchBytes(config.src));
    else bytes = await fetchBytes(config.fallback);
    await verify(bytes, config.sha256);
    const data = JSON.parse(new TextDecoder().decode(bytes));
    delete config.embedded;
    // Give the static overview a paint opportunity before initializing interactive UI.
    await new Promise(resolve => setTimeout(resolve, 0));
    return data;
  }
  async function download(name) {
    const item = config.downloads[name];
    if (!item) return;
    notice('正在准备下载 ' + name + '…');
    try {
      const bytes = config.offline ? await inflate(decode(item.embedded))
        : await fetchBytes(encodeURIComponent(name) + '?v=' + item.sha256.slice(0, 16));
      await verify(bytes, item.sha256);
      const url = URL.createObjectURL(new Blob([bytes]));
      const link = document.createElement('a'); link.href = url; link.download = name;
      document.body.append(link); link.click(); link.remove();
      setTimeout(() => URL.revokeObjectURL(url), 10000);
      notice('已准备好 ' + name); noticeTimer = setTimeout(() => {status.hidden = true;}, 3000);
    } catch (error) {
      notice('下载未完成：' + error.message + ' 请再次点击下载按钮重试。');
    }
  }
  function ready() {
    initialized = true; status.hidden = true; document.removeEventListener('click', capture, true);
    window.researchReadyAt = performance.now(); performance.mark('research-ready');
    queuedButton?.click(); queuedButton = null;
  }
  return {loadData, download, ready, fail};
})();
