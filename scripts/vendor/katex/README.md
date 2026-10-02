# Vendored KaTeX

Pinned version: **0.19.0**. Official npm tarball URL and SHA-512 integrity are
recorded in `provenance.json`; the downloaded tarball was checked against that
integrity before extracting the distribution, fonts, package metadata and license.

The research site builders call `render_research_math.cjs` using Node.js. They
embed the resulting HTML/MathML and WOFF2 font data in each standalone page;
the browser does not load KaTeX JavaScript or request a CDN. The original
upstream CSS is kept here, with WOFF2-only font embedding applied at build time.
The MIT license is retained here and included in the generated page's CSS.

Official documentation: https://katex.org/docs/node and https://katex.org/docs/options

Do not edit minified distribution files. When updating the pinned dependency,
verify the release integrity, preserve its license and rerun formula/browser
checks (including offline file URLs).
