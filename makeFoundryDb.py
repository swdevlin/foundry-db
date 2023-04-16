import csv
import json
from pathlib import Path
import secrets

# import random
# import string   

# def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
#         return ''.join(random.choice(chars) for _ in range(size))   

def setDbRecord(type:str)->dict:
    record = {
        "name": "",
        "type": "",
        "img": "",
        "system": {
            "name": "",
            "techLevel": 0,
            "description": "",
            "shortdescr": "",
            "quantity": 0,
            "weight": 0,
            "price": 0,
            "traits": [],
            "consumables": [],
            "skillModifier": 0,
            "skill": "",
            "associatedSkillName": "",
            "equipped": "",
            "docReference": "",
            "pdfReference": {
                "type": "",
                "href": "",
                "label": ""
            },
        },
        "effects": [],
        "flags": {
            "twodsix": {
                "newItem": True
            },
            "core": {
                "sourceId": "Item.viNh0N8Fw28bpV2e"
            }
        },
        "_stats": {
            "systemId": "twodsix",
            "systemVersion": "2.27.3",
            "coreVersion": "10.291",
            "createdTime": 1681493070337,
            "modifiedTime": 1681493265527,
            "lastModifiedBy": "OK9YthkIIxCpCkT0"
        },
        "folder": None,
        "sort": 0,
        "ownership": {
            "default": 0,
            "OK9YthkIIxCpCkT0": 3
        },
        "_id": ""
    }
    if type == "armor":
        record['type'] = 'armor'
        record['system']['armor'] = 0
        record['system']['secondaryArmor'] = {
            'value': 0,
            'protectionTypes': []
        }
        record['system']['radiationProtection'] = {
            'value': 0
        }
    if type == "weapon":
        record['type'] = 'weapons'
        record['system']['target'] = {
            "value": None,
            "width": None,
            "units": "m",
            "type": "none"
        }
        record['system']['range'] = "0"
        record['system']['damage'] = "0"
        record['system']['damageBonus'] = 0
        record['system']['magazineSize'] = 0
        record['system']['ammo'] = "0"
        record['system']['lawLevel'] = 0
        record['system']['magazineCost'] = 0
        record['system']['rangeBand'] = ""
        record['system']['weaponType'] = ""
        record['system']['damageType'] = ""
        record['system']['rateOfFire'] = "1"
        record['system']['recoil'] = False
        record['system']['armorPiercing'] = 0
        record['system']['handlingModifiers'] = ""
    return record

def makeOutputRecord(csvData:dict, type:str, listFolders:list)->dict:
    imgRoot = 'systems/twodsix/assets/icons/'
    if type == 'armor':
        # process as armor
        outputRecord = setDbRecord(type)
        outputRecord["_id"] = secrets.token_hex(8)
        outputRecord['img'] = imgRoot+csvData['image']
        outputRecord['system']['folder'] = None
        if int(csvData['techlevel']) < 10:
            suffixTL = " (TL  "+csvData['techlevel']+")"
        else:
            suffixTL = " (TL "+csvData['techlevel']+")"
        outputRecord['name'] = csvData['name']+" (TL "+csvData['techlevel']+")"
        outputRecord['system']['name'] = csvData['name']
        if csvData['shortdescription']:
            outputRecord['system']['shortdescr'] = csvData['shortdescription']
        if csvData['description']:
            outputRecord['system']['description'] = csvData['description']
        outputRecord['system']['skill'] = csvData['skill']
        outputRecord['system']['techLevel'] = int(csvData['techlevel'])
        outputRecord['system']['quantity'] = int(csvData['quantity'])
        outputRecord['system']['weight'] = int(csvData['weight'])
        outputRecord['system']['price'] = int(csvData['price'])
        outputRecord['system']['armor'] = int(csvData['armor'])
        if csvData['secondaryarmor'] != '':
            outputRecord['system']['secondaryArmor']['value'] = int(csvData['secondaryarmor'])
            for t in csvData['secondarytypes'].split(":"):
                outputRecord['system']['secondaryArmor']['protectionTypes'].append(t)
        if csvData['radiation'] != '':
            outputRecord['system']['radiationProtection']['value'] = int(csvData['radiation'])
        return outputRecord
    else:
        print(f"{type} type not yet supported")
        return {}


def main ():
    inputFolder = "input"
    outputFolder = "output"
    weaponFile = "weapon"
    armorFile = "armor"
    itemFile = "item"
    ammoFile = "ammo"
    inputSuffix = ".csv"
    outputSuffix = ".db"
    foundryPrefix = "mtg2-"

    inputPath = Path('./'+inputFolder)
    listInputFiles = list(inputPath.glob('*'+inputSuffix))
    listFolders = []
    for f in listInputFiles:
        if f.name == armorFile+inputSuffix:
            # process as armor
            print(f"Start processing armor file {f.name}")
            with open(Path(outputFolder, foundryPrefix+armorFile+outputSuffix), 'w') as dbFile:
                with open(f, newline='') as csvfile:
                    csvInput = csv.DictReader(csvfile)
                    for row in csvInput:
                        dbFile.write(json.dumps(makeOutputRecord(row, 'armor', listFolders))+"\n")
            print(f"Complete processing armor file {f.name}")
        if f.name == weaponFile+inputSuffix:
            # process as wepon
            print(f"Start processing weapon file {f.name}")
        if f.name == itemFile+inputSuffix:
            # process as item
            print(f"Start processing item file {f.name}")
        if f.name == ammoFile+inputSuffix:
            # process as ammo
            print(f"Start processing ammo file {f.name}")
    return True

if __name__ == "__main__":
    main()
