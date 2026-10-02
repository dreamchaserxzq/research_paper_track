"""Archive bytes, deterministic bundles, and online/offline delivery contracts."""
import base64
import gzip
import hashlib
import json
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from research_delivery import package_pages, as_bytes
from research_math import math_styles


class DeliveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = {'chapters': [{'html': '<p>α & β</p>'}],
                    'downloads': {'example.json': '{"original": "α"}\n', 'notes.md': '# 原文\n\n$x$\n'}}
        page = ('<!doctype html><head>' + math_styles() + '</head><body>'
                '<div class="sidebar-bottom"></div><footer></footer>'
                '<script id="atlas-data" type="application/json">{}</script>'
                '<script>const DATA=JSON.parse(document.getElementById(\'atlas-data\').textContent);</script>'
                '<script>window.notebookTest=true;</script></body>')
        cls.page = page
        cls.outputs = package_pages(page, cls.data, 'atlas-data')

    def config(self, name):
        return json.loads(re.search(r'<script id="research-delivery" type="application/json">(.*?)</script>',
                                    self.outputs[name], re.S).group(1))

    def test_online_starts_without_archives_or_font_payloads(self):
        config = self.config('index.html')
        self.assertFalse(config['offline'])
        self.assertNotIn('embedded', config)
        self.assertNotIn('data:font/woff2', self.outputs['index.html'])
        self.assertIn('href="offline.html"', self.outputs['index.html'])
        raw = gzip.decompress(self.outputs[config['src']])
        data = json.loads(raw)
        self.assertEqual(data['chapters'], self.data['chapters'])
        self.assertEqual(data['downloads'], {'example.json': True, 'notes.md': True})
        self.assertEqual(raw, self.outputs[config['fallback']])
        self.assertEqual(hashlib.sha256(raw).hexdigest(), config['sha256'])

    def test_offline_contains_exact_individually_compressed_downloads(self):
        config = self.config('offline.html')
        self.assertTrue(config['offline'])
        self.assertIn('data:font/woff2', self.outputs['offline.html'])
        self.assertEqual(gzip.decompress(base64.b64decode(config['embedded'])), self.outputs[config['fallback']])
        for name, original in self.data['downloads'].items():
            raw = gzip.decompress(base64.b64decode(config['downloads'][name]['embedded']))
            self.assertEqual(raw, original.encode())
            self.assertEqual(hashlib.sha256(raw).hexdigest(), config['downloads'][name]['sha256'])

    def test_all_online_font_urls_exist_in_outputs(self):
        fonts = re.findall(r'url\((math-fonts/[^)]+)\)', self.outputs['index.html'])
        self.assertGreater(len(fonts), 0)
        for name in fonts:
            self.assertTrue(self.outputs[name].startswith(b'wOF2'))

    def test_rebuild_is_deterministic(self):
        again = package_pages(self.page, self.data, 'atlas-data')
        self.assertEqual({k: as_bytes(v) for k, v in self.outputs.items()},
                         {k: as_bytes(v) for k, v in again.items()})


if __name__ == '__main__':
    unittest.main()
