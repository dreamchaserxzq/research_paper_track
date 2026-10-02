// Build-only renderer: no JavaScript or CDN is needed to display the formulas.
const fs = require('node:fs');
const katex = require('./vendor/katex/dist/katex.min.js');
const equations = JSON.parse(fs.readFileSync(0, 'utf8'));
try {
  const rendered = equations.map(({tex, display}) => {
    try {
      return katex.renderToString(tex, {
        displayMode: display,
        output: 'htmlAndMathml',
        throwOnError: true,
        trust: false,
        maxExpand: 1000,
        strict: code => code === 'unicodeTextInMathMode' ? 'ignore' : 'warn',
      });
    } catch (error) {
      throw new Error(`${tex}\n${error.message}`);
    }
  });
  process.stdout.write(JSON.stringify(rendered));
} catch (error) {
  process.stderr.write(error.message + '\n');
  process.exitCode = 1;
}
