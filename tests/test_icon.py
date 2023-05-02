import unittest

from items.icon_mapper import determine_icon


class TestIconMapper(unittest.TestCase):
    def test_bag_is_default_item(self):
        name = 'not an item'
        icon = determine_icon(name, 'armor')
        self.assertEqual(icon, 'icons/svg/item-bag.svg')
        icon = determine_icon(name, 'weapon')
        self.assertEqual(icon, 'systems/twodsix/assets/icons/default_weapon.png')

    def test_case_ignored(self):
        name = 'super Vacc Suit'
        icon = determine_icon(name, 'armor')
        self.assertEqual(icon, 'systems/twodsix/assets/icons/vacc-suit.svg')

    def test_multiple_spaces_ignored(self):
        name = 'super vacc  suit'
        icon = determine_icon(name, 'armor')
        self.assertEqual(icon, 'systems/twodsix/assets/icons/vacc-suit.svg')

    def test_spaces_in_word_honoured(self):
        name = 'super v acc  suit'
        icon = determine_icon(name, 'armor')
        self.assertEqual(icon, 'icons/svg/item-bag.svg')
