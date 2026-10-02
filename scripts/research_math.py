"""Build-time TeX rendering shared by the two standalone research readers."""
from __future__ import annotations

import base64
import hashlib
import html
import json
import re
import subprocess
from functools import lru_cache
from pathlib import Path

import markdown

HERE = Path(__file__).resolve().parent
VENDOR = HERE / 'vendor/katex'
VERSION = json.loads((VENDOR / 'package.json').read_text())['version']


def math_inputs():
    return [Path(__file__).resolve(), HERE / 'render_research_math.cjs',
            HERE / 'research_math.css', *sorted(p for p in VENDOR.rglob('*') if p.is_file())]


@lru_cache(maxsize=2)
def math_styles(embed_fonts=True):
    """Inline WOFF2 fonts so a downloaded HTML needs no network or sibling files."""
    css = (VENDOR / 'dist/katex.min.css').read_text()
    # WOFF2 is supported by current desktop/mobile browsers; omit legacy fallbacks.
    css = re.sub(r'src:([^;}]+)', lambda m: 'src:' + next(
        part for part in m.group(1).split(',') if '.woff2)' in part), css)

    def font(match):
        path = VENDOR / 'dist' / match.group(1)
        if not embed_fonts:
            return 'url(math-fonts/' + path.name + ')'
        data = base64.b64encode(path.read_bytes()).decode('ascii')
        return 'url(data:font/woff2;base64,' + data + ')'

    css = re.sub(r'url\((fonts/[^)]+\.woff2)\)', font, css)
    if 'url(fonts/' in css:
        raise ValueError('Unexpected external font reference in KaTeX CSS')
    return '<!-- KaTeX ' + VERSION + ' (MIT); license embedded below. -->\n<style>\n/*\n' + (
        VENDOR / 'LICENSE').read_text().replace('*/', '* /') + '\n*/\n' + css + '\n' + (
        HERE / 'research_math.css').read_text() + '\n</style>\n'


def render_md(raw, *, plain_text=False):
    """Preserve TeX through Markdown, excluding code and escaped dollar signs."""
    prefix = 'RESEARCHSTASH' + hashlib.sha256(raw.encode()).hexdigest()[:16].upper()
    while prefix in raw:
        prefix += 'X'
    code, formulas = [], []

    def protect_code(match):
        token = prefix + 'CODE' + str(len(code)) + 'END'
        code.append((token, match.group(0)))
        return token

    def protect_math(tex, display=False):
        if plain_text and not display:
            # Some historical JSON summaries double-escaped TeX control words.
            # Normalize their presentation only; retain the original source/export.
            tex = re.sub(r'\\\\(?=[a-zA-Z])', r'\\', tex)
        token = prefix + 'MATH' + str(len(formulas)) + 'END'
        formulas.append({'token': token, 'tex': tex.strip(), 'display': display})
        return '\n\n' + token + '\n\n' if display else token

    # One pass: code cannot consume indented lines *inside* an already open formula,
    # and TeX delimiters inside a code example cannot start a formula.
    pattern = re.compile(
        r'(?P<code>^ {0,3}(?P<fence>`{3,}|~{3,})[^\n]*\n[\s\S]*?^ {0,3}(?P=fence)[ \t]*$'
        r'|(?:^(?: {4}|\t)[^\n]*(?:\n|$))+'
        r'|(?<!`)(?P<ticks>`+)(?!`)[\s\S]*?(?<!`)(?P=ticks)(?!`))'
        r'|(?<!\\)\\\[(?P<bracket>[\s\S]*?)\\\]'
        r'|(?<!\\)\$\$(?P<display>[\s\S]*?)(?<!\\)\$\$'
        r'|(?<!\\)\\\((?P<paren>[\s\S]*?)\\\)'
        r'|(?<![\\$])\$(?P<inline>(?:\\[^\n]|[^\n$\\])+?)(?<!\\)\$(?!\$)', re.M)

    def protect(match):
        if match.group('code') is not None:
            return protect_code(match)
        for name in ('bracket', 'display', 'paren', 'inline'):
            if match.group(name) is not None:
                return protect_math(match.group(name), name in ('bracket', 'display'))

    raw = pattern.sub(protect, raw)
    for token, source in reversed(code):
        raw = raw.replace(token, source)
    if plain_text:
        rendered = html.escape(raw)
    else:
        md = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc'])
        md.ESCAPED_CHARS = [*md.ESCAPED_CHARS, '$']
        rendered = md.convert(raw)
    if not formulas:
        return rendered
    result = subprocess.run(['node', str(HERE / 'render_research_math.cjs')],
                            input=json.dumps(formulas), text=True, capture_output=True)
    if result.returncode:
        raise ValueError('Formula rendering failed: ' + result.stderr.strip())
    outputs = json.loads(result.stdout)
    assert len(outputs) == len(formulas)
    for item, equation in zip(formulas, outputs):
        tag = 'div' if item['display'] else 'span'
        kind = 'display' if item['display'] else 'inline'
        attrs = ' tabindex="0" role="group" aria-label="数学公式，可横向滚动"' if item['display'] else ''
        markup = (f'<{tag} class="research-math research-math-{kind}" '
                  f'data-tex="{html.escape(item["tex"], quote=True)}"{attrs}>'
                  f'{equation}</{tag}>')
        token = item['token']
        rendered = rendered.replace('<p>' + token + '</p>', markup).replace(token, markup)
    return rendered
