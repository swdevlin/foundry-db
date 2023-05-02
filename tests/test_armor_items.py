import unittest

from items.armor import secondary_protection_types, create_item


class TestArmorItem(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.source = {
            'Armour Type': 'Ballistic Vest',
            'Protection': "4",
            'Secondary': "",
            'Secondary Type': " ",
            'TL': "8",
            'Rad': "-",
            'Kg': "1",
            'Cost': "Cr500",
            'Required Skill': None
        }

    def test_secondary_with_and(self):
        items = secondary_protection_types('fire, Lasers and energy')
        self.assertEqual(items, ['energy', 'fire', 'laser'])

    def test_lasers_is_laser(self):
        items = secondary_protection_types('lasers')
        self.assertEqual(items, ['laser'])

    def test_psi_is_psionics(self):
        items = secondary_protection_types('Psi')
        self.assertEqual(items, ['psionic'])

    def test_secondary(self):
        items = secondary_protection_types('fire, laser')
        self.assertEqual(items, ['fire', 'laser'])

    def test_secondary_empty(self):
        items = secondary_protection_types('')
        self.assertEqual(items, [])

    def test_protection_is_int(self):
        item = create_item(self.source)
        self.assertEqual(item['system']['armor'], 4)

    def test_secondary_defaults_to_0(self):
        item = create_item(self.source)
        self.assertEqual(item['system']['secondaryArmor']['value'], 0)

    def test_secondary_value(self):
        self.source['Secondary'] = "7"
        item = create_item(self.source)
        self.assertEqual(item['system']['secondaryArmor']['value'], 7)

    def test_price_is_int(self):
        item = create_item(self.source)
        self.assertEqual(item['system']['price'], 500)

    def test_dash_weight_is_0(self):
        self.source['Kg'] = '-'
        item = create_item(self.source)
        self.assertEqual(item['system']['weight'], 0)

    def test_weight_is_int(self):
        item = create_item(self.source)
        self.assertEqual(item['system']['weight'], 1)

    def test_half(self):
        self.source['Secondary'] = "½"
        item = create_item(self.source)
        self.assertEqual(item['system']['secondaryArmor']['value'], 0.5)

    def test_tl_is_int(self):
        item = create_item(self.source)
        self.assertEqual(item['system']['techLevel'], 8)

    def test_blank_tl(self):
        self.source['TL'] = ""
        item = create_item(self.source)
        self.assertEqual(item['system']['techLevel'], '')

    def test_tl_in_name(self):
        item = create_item(self.source)
        self.assertEqual(item['name'], 'Ballistic Vest (TL 8)')

        self.source['TL'] = '12'
        item = create_item(self.source)
        self.assertEqual(item['name'], 'Ballistic Vest (TL12)')

        self.source['TL'] = ""
        item = create_item(self.source)
        self.assertEqual(item['name'], 'Ballistic Vest')
