"""Small online entry point plus a complete, self-contained offline edition."""
import base64
import gzip
import hashlib
import json
import re
from pathlib import Path

from research_math import math_styles, VENDOR

HERE = Path(__file__).resolve().parent


def as_bytes(value):
    return value if isinstance(value, bytes) else value.encode('utf-8')


def delivery_inputs():
    return [Path(__file__).resolve(), HERE / 'research_delivery.js', HERE / 'research_delivery.css']


def package_pages(page, payload, data_id):
    """Separate download-only archives; keep identical reader data in both editions."""
    downloads = payload['downloads']
    data = {**payload, 'downloads': {name: True for name in downloads}}
    raw = json.dumps(data, ensure_ascii=False, separators=(',', ':')).encode()
    packed = gzip.compress(raw, compresslevel=9, mtime=0)
    digest = hashlib.sha256(raw).hexdigest()
    filename = 'site-data.' + digest[:16] + '.json'
    outputs = {filename: raw, filename + '.gz': packed}
    metadata = {name: {'sha256': hashlib.sha256(as_bytes(text)).hexdigest()}
                for name, text in downloads.items()}
    config = {'src': filename + '.gz', 'fallback': filename, 'sha256': digest,
              'downloads': metadata, 'offline': False}
    scripts = re.findall(r'<script>(.*?)</script>', page, re.S)
    assert len(scripts) == 2, 'Expected the workbench and personal notebook scripts'
    page = re.sub(r'<script>(.*?)</script>', '', page, flags=re.S)
    pattern = r'<script id="' + data_id + r'" type="application/json">.*?</script>'
    page, count = re.subn(pattern, '__DELIVERY_CONFIG__', page, flags=re.S)
    assert count == 1
    source = '\n'.join(scripts)
    original = "JSON.parse(document.getElementById('" + data_id + "').textContent)"
    assert original in source
    source = source.replace(original, 'await window.researchAssets.loadData()')
    runtime = (HERE / 'research_delivery.js').read_text()
    bootstrap = '<script>\n' + runtime + '\nwindow.researchReady=(async()=>{\n' + source + (
        '\nwindow.researchAssets.ready();\n})().catch(window.researchAssets.fail);\n</script>\n')
    page = page.replace('</head>', '<style>' + (HERE / 'research_delivery.css').read_text() + '</style></head>')
    status = '<div id="delivery-status" class="delivery-status" role="status">正在载入研究资料…</div>'
    page = page.replace('</body>', status + '\n' + bootstrap + '</body>')

    def edition(settings, offline=False):
        result = page
        if not offline:
            result = result.replace(math_styles(), math_styles(embed_fonts=False))
        safe = json.dumps(settings, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
        result = result.replace('__DELIVERY_CONFIG__', '<script id="research-delivery" type="application/json">' + safe + '</script>')
        link = ('<span class="offline-download">完整离线版 · 阅读资料已包含</span>' if offline else
                '<a class="offline-download" href="offline.html" download="' + data_id + '-offline.html">下载完整离线版 ↓</a>')
        result = result.replace('<div class="sidebar-bottom">', '<div class="sidebar-bottom">' + link)
        result = result.replace('</footer>', '<div class="delivery-footer">' + link + '</div></footer>')
        return result

    outputs['index.html'] = edition(config)
    offline = {**config, 'offline': True, 'embedded': base64.b64encode(packed).decode(),
               'downloads': {name: {**metadata[name], 'embedded': base64.b64encode(
                   gzip.compress(as_bytes(text), compresslevel=9, mtime=0)).decode()}
                             for name, text in downloads.items()}}
    outputs['offline.html'] = edition(offline, offline=True)
    outputs.update({'math-fonts/' + p.name: p.read_bytes() for p in sorted((VENDOR / 'dist/fonts').glob('*.woff2'))})
    return outputs
