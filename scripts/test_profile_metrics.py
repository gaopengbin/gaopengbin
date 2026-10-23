import copy
import json
import unittest
import xml.etree.ElementTree as ET
from unittest.mock import patch
import profile_metrics as metrics


class ProfileMetricsTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((metrics.ROOT/'assets/profile-metrics.json').read_text(encoding='utf-8'))

    def test_svg_and_totals(self):
        self.assertEqual(len(self.data['products']), 6)
        self.assertEqual(self.data['downloads'], sum(p['downloads'] for p in self.data['products']))
        for result in (metrics.metrics(self.data), metrics.activity(self.data)):
            self.assertEqual(ET.fromstring(result).attrib['width'], '1200')
        days = [d for w in self.data['calendar']['weeks'] for d in w['contributionDays']]
        self.assertEqual(len(days), len({d['date'] for d in days}))
        self.assertEqual(sum(d['contributionCount'] for d in days), self.data['calendar']['totalContributions'])

    def test_zero_values_do_not_break_chart(self):
        data = copy.deepcopy(self.data)
        for product in data['products']:
            product['stars'] = 0
        for week in data['calendar']['weeks']:
            for day in week['contributionDays']:
                day['contributionCount'] = 0
        ET.fromstring(metrics.metrics(data))
        ET.fromstring(metrics.activity(data))

    def test_pagination(self):
        with patch.object(metrics, 'api', side_effect=[[{}]*100, [{}]*2]) as api:
            self.assertEqual(len(metrics.pages('test?type=owner')), 102)
            self.assertIn('page=2', api.call_args.args[0])

    def test_each_card_matches_product_data(self):
        readme = (metrics.ROOT/'README.md').read_text(encoding='utf-8')
        for p in self.data['products']:
            svg = metrics.product_badges(p, self.data['updated'])
            root = ET.fromstring(svg)
            self.assertEqual(root.attrib['width'], '460')
            self.assertIn(f'{p["stars"]} Stars, {p["forks"]} Forks, {p["downloads"]} GitHub', svg)
            self.assertIn(f'img.shields.io/github/stars/gaopengbin/{p["name"]}?', readme)
            self.assertIn(f'img.shields.io/github/forks/gaopengbin/{p["name"]}?', readme)
            if p['name'] == 'wechat-dialog-generator':
                self.assertIn('img.shields.io/badge/Web-Open%20App-brightgreen', readme)
            else:
                self.assertIn(f'img.shields.io/github/downloads/gaopengbin/{p["name"]}/total?', readme)

    def test_failed_api_preserves_previous_files(self):
        paths = [metrics.ROOT/'assets'/name for name in ('metrics.svg', 'activity.svg', 'profile-metrics.json')]
        paths += sorted((metrics.ROOT/'assets/product-stats').glob('*.svg'))
        before = [p.read_bytes() for p in paths]
        with patch.object(metrics, 'collect', side_effect=RuntimeError('test network failure')):
            with patch('sys.argv', ['profile_metrics.py']):
                with self.assertRaises(RuntimeError):
                    metrics.main()
        self.assertEqual(before, [p.read_bytes() for p in paths])


if __name__ == '__main__':
    unittest.main()
