import re
import secrets

from items.helpers import timestamp, tl_in_name
from items.icon_mapper import determine_icon


def secondary_value(value):
    if value == '½':
        return 0.5
    elif value == '':
        return 0
    else:
        return int(value)


def radiation_value(value):
    if value == '-':
        return 0
    elif value == '':
        return 0
    else:
        return int(value)


def secondary_protection_types(text):
    tokens = re.split(r'(?:and|,)', text)
    types = []
    for token in tokens:
        if token == '':
            continue
        token = token.lower().strip()
        if token == 'lasers':
            token = 'laser'
        elif token == 'psi':
            token = 'psionic'
        types.append(token)
    return sorted(types)


def create_item(record):
    return {
        "name": f"{record['Armour Type']}{tl_in_name(record['TL'])}",
        "type": "armor",
        "img": determine_icon(record['Armour Type'], 'armor'),
        "system": {
            "name": None,
            "techLevel": '' if record['TL'] == '' else int(record['TL']),
            "description": "",
            "shortdescr": "",
            "quantity": 1,
            "weight": 0 if record['Kg'] == '-' else int(record['Kg']),
            "price": int(record['Cost'].lower().lstrip('cr')),
            "traits": [],
            "consumables": [],
            "skillModifier": 0,
            "skill": "",
            "associatedSkillName": record['Required Skill'],
            "equipped": "",
            "docReference": "",
            "pdfReference": {
                "type": "",
                "href": "",
                "label": ""
            },
            "armor": int(record['Protection']),
            "secondaryArmor": {
                "value": secondary_value(record['Secondary']),
                "protectionTypes": secondary_protection_types(record['Secondary Type']),
            },
            "radiationProtection": {
                "value": radiation_value(record['Rad'])
            },
            "type": "armor",
            "useConsumableForAttack": "",
            "isPowered": False,
            "folder": None
        },
        "effects": [],
        "flags": {
            "twodsix": {},
            "core": {
                "sourceId": "Item.viNh0N8Fw28bpV2e"
            },
            "cf": {
                "id": "temp_njmyjcao2vm"
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
