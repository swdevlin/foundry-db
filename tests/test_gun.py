import unittest

from parsers.gun import parse


class TestGunParser(unittest.TestCase):
    def test_standard(self):
        line = 'Personal Defence Laser 13 25 3D+3 3 Cr6000 25 Cr100 Auto 2, Zero-G'
        expected = [
            'Personal Defence Laser',
            '13',
            '25',
            '3D+3',
            '3',
            'Cr6000',
            '25',
            'Cr100',
            'Auto 2, Zero-G',
        ]
        tokens = parse(line)
        self.assertEqual(expected, tokens)

    def test_hyphen_in_entry(self):
        line = 'Snub Pistol 8 5 3D-3 - Cr150 6 Cr10 Zero-G'
        expected = [
            'Snub Pistol',
            '8',
            '5',
            '3D-3',
            '-',
            'Cr150',
            '6',
            'Cr10',
            'Zero-G',
        ]
        tokens = parse(line)
        self.assertEqual(expected, tokens)


if __name__ == '__main__':
    unittest.main()