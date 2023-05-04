import unittest

from items.weapon import parse_traits, convert_damage


class TestWeaponItem(unittest.TestCase):
    def test_fire_trait(self):
        traits = parse_traits('Auto 3')
        self.assertFalse(traits['fire'])

        traits = parse_traits('Fire')
        self.assertTrue(traits['fire'])

        traits = parse_traits('Aut0 4, Fire')
        self.assertTrue(traits['fire'])

    def test_zerog_trait(self):
        traits = parse_traits('Auto 3')
        self.assertFalse(traits['zero-g'])

        traits = parse_traits('Zero-G')
        self.assertTrue(traits['zero-g'])

        traits = parse_traits('Aut0 4, Zero-G')
        self.assertTrue(traits['zero-g'])

    def test_ap_trait(self):
        traits = parse_traits('Auto 3')
        self.assertEqual(traits['ap'], 0)

        traits = parse_traits('AP 4')
        self.assertEqual(traits['ap'], 4)

        traits = parse_traits('Ap 3, Fire')
        self.assertTrue(traits['ap'], 3)

    def test_auto_trait(self):
        traits = parse_traits('AP 3')
        self.assertIsNone(traits['auto'])

        traits = parse_traits('Auto 4')
        self.assertEqual(traits['auto'], "1/4")

        traits = parse_traits('auto 3, Fire')
        self.assertTrue(traits['auto'], "1/3")

    def test_traits(self):
        traits = parse_traits('Auto 3')
        self.assertEqual(traits['traits'], [])

        traits = parse_traits('Ap 3, Fire')
        self.assertEqual(traits['traits'], [])

        traits = parse_traits('Ap 3, Fire, Auto 2, Scope, Bulky')
        self.assertEqual(traits['traits'], ['scope', 'bulky'])

    def test_blast(self):
        traits = parse_traits('Fire')
        self.assertEqual(traits['blast'], None)

        traits = parse_traits('Blast 2')
        self.assertEqual(traits['blast'], 2)

    def test_convert_damage(self):
        text = '3D'
        d = convert_damage(text)
        self.assertEqual(d, '3d6')

        text = '3D-3'
        d = convert_damage(text)
        self.assertEqual(d, '3d6-3')

        text = '4'
        d = convert_damage(text)
        self.assertEqual(d, '4')