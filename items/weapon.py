import secrets

from items.helpers import timestamp, tl_in_name, cost
from items.icon_mapper import determine_icon


def parse_traits(text):
    traits = {
        'ap': 0,
        'zero-g': False,
        'auto': None,
        'fire': None,
        'blast': None,
        'traits': [],
    }
    tokens = text.split(',')
    for token in tokens:
        t = token.strip().lower()
        if t == 'fire':
            traits['fire'] = True
        elif t == 'zero-g':
            traits['zero-g'] = True
        elif t.startswith('ap '):
            traits['ap'] = int(t.split(' ')[-1])
        elif t.startswith('auto '):
            traits['auto'] = f"1/{t[5:]}"
        elif t.startswith('blast '):
            traits['blast'] = int(t.split(' ')[-1])
        else:
            traits['traits'].append(t)
    return traits


def create_item(record):
    traits = parse_traits(record['Traits'])
    return {
        "name": f"{record['Weapon']}{tl_in_name(record['TL'])}",
        "type": "weapon",
        "img": determine_icon(record['Weapon'], 'weapon'),
        "system": {
            "name": "",
            "techLevel": '' if record['TL'] == '' else int(record['TL']),
            "description": "",
            "shortdescr": "",
            "quantity": 1,
            "weight": 0 if record['Kg'] == '-' else float(record['Kg']),
            "price": cost(record['Cost']),
            "traits": [],
            "consumables": [],
            "skillModifier": 0,
            "skill": "",
            "associatedSkillName": "",
            "equipped": "backpack",
            "docReference": "",
            "pdfReference": {
                "type": "",
                "href": "",
                "label": ""
            },
            "target": {
                "value": traits['blast'],
                "width": None,
                "units": "m",
                "type": "none" if traits['blast'] is None else "radius"
            },
            "range": record['Range'],
            "damage": record['Damage'],
            "damageBonus": 0,
            "magazineSize": record['Magazine'],
            "ammo": record['Magazine'],
            "useConsumableForAttack": "",
            "magazineCost": cost(record['Mag Cost']),
            "type": "weapon",
            "lawLevel": 0,
            "rangeBand": "",
            "weaponType": "",
            "damageType": "NONE",
            "rateOfFire": traits['auto'],
            "recoil": traits['zero-g'] is True,
            "features": ', '.join(traits['traits']),
            "armorPiercing": traits['ap'],
            "handlingModifiers": ""
        },
        "effects": [],
        "flags": {
            "twodsix": {},
            "core": {
                "sourceId": "Item.q21aqTzFu2knzopT"
            }
        },
        "_stats": {
            "systemId": "twodsix",
            "systemVersion": "2.31.0",
            "coreVersion": "10.291",
            "createdTime": timestamp(),
            "modifiedTime": timestamp(),
            "lastModifiedBy": "X7Zc9wesNGsI137g"
        },
        "folder": None,
        "sort": 0,
        "ownership": {
            "default": 0,
            "OK9YthkIIxCpCkT0": 3
        },
        "_id": secrets.token_hex(8)
    }
