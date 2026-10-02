"""Check real math layout, Markdown boundaries and standalone asset packaging."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from research_math import render_md, math_styles


class ResearchMathTests(unittest.TestCase):
    def test_four_delimiters_and_accessible_tex(self):
        result = render_md(r'行内 $u_i^2$ 与 \(\alpha\)。' + '\n\n' +
                           r'\[\frac{\partial u}{\partial t}=\Delta u\]' + '\n\n' +
                           r'$$\int_\Omega u\,dx$$')
        self.assertEqual(result.count('class="research-math research-math-inline"'), 2)
        self.assertEqual(result.count('class="research-math research-math-display"'), 2)
        self.assertEqual(result.count('encoding="application/x-tex"'), 4)
        self.assertIn('<mfrac>', result)
        self.assertIn('class="katex-html" aria-hidden="true"', result)

    def test_code_and_escaped_currency_are_unchanged(self):
        source = ('`$x$` and ``\\(y\\)`` and \\$5 / \\$10\n\n'
                  '```tex\n$$z$$\n```\n\n    $w$\n\nReal: $v$.')
        result = render_md(source)
        self.assertEqual(result.count('class="research-math '), 1)
        self.assertIn('<code>$x$</code>', result)
        self.assertIn('$$z$$', result)
        self.assertIn('$w$', result)
        self.assertIn('$5 / $10', result)

    def test_indented_multiline_equation_and_table_pipes(self):
        result = render_md('\\[\n    \\begin{aligned}\n    a&=b\\\\\n    c&=d\n'
                           '    \\end{aligned}\n\\]\n\n'
                           '| Object | Definition |\n|---|---|\n| Norm | $|u|$ |')
        self.assertIn('<mtable', result)
        self.assertIn('<table>', result)
        self.assertEqual(result.count('<td>'), 2)
        self.assertNotIn('RESEARCHSTASH', result)

    def test_invalid_tex_fails_build_instead_of_silently_showing_source(self):
        with self.assertRaisesRegex(ValueError, 'Formula rendering failed'):
            render_md(r'$\notARealTexCommand{x}$')

    def test_tex_cannot_introduce_trusted_links(self):
        result = render_md(r'$\href{javascript:alert(1)}{x}$')
        self.assertNotIn('href=', result)
        self.assertNotIn('<script', result)

    def test_legacy_plain_text_is_escaped_and_commands_are_readable(self):
        result = render_md(r'<img src=x onerror=alert(1)> $\\theta\\in[-\\tau,0]$', plain_text=True)
        self.assertIn('&lt;img', result)
        self.assertNotIn('<img', result)
        self.assertIn('<mi>θ</mi>', result)
        self.assertIn('<mi>τ</mi>', result)

    def test_styles_contain_embedded_fonts_and_license_only(self):
        css = math_styles()
        self.assertIn('data:font/woff2;base64,', css)
        self.assertNotIn('url(fonts/', css)
        self.assertIn('Permission is hereby granted', css)


if __name__ == '__main__':
    unittest.main()
