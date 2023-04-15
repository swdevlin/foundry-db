import csv
import json
from pathlib import Path

def makeOutputRecord(csvData:dict, type:str)->dict:
    if type == 'armor':
        # process as armor
        outputRecord = {
            "name": "",
            "type": "armor",
            "img": "",
            "system": {
                "name": "",
                "techLevel": 0,
                "description": "Armor",
                "shortdescr": "Armor",
                "quantity": 1,
                "weight": 1,
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
                "armor": 0,
                "secondaryArmor": {
                    "value": 0,
                    "protectionTypes": []
                },
                "radiationProtection": {
                    "value": 0
                },
                "type": "armor",
                "useConsumableForAttack": "",
                "isPowered": False            },
            "effects": [],
            "flags": {
                "twodsix": {
                    "newItem": True
                },
                "core": {
                    "sourceId": "Item.kHeev9TUmoxCl1uD"
                }
            },
            "_stats": {
                "systemId": "twodsix",
                "systemVersion": "2.27.3",
                "coreVersion": "10.291",
                "createdTime": 1681494327937,
                "modifiedTime": 1681494395684,
                "lastModifiedBy": "OK9YthkIIxCpCkT0"
            },
            "folder": "",
            "sort": 0,
            "ownership": {
                "default": 0,
                "OK9YthkIIxCpCkT0": 3
            },
            "_id": "bmMpPYi1MEHTx7mh"
        }
        outputRecord['img'] = "icons/svg/item-bag.svg"
        outputRecord['system']['folder'] = None
        outputRecord['name'] = csvData['name']+" ("+csvData['techlevel']+")"
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
    print(listInputFiles)
    for f in listInputFiles:
        if f.name == armorFile+inputSuffix:
            # process as armor
            print(f"Start processing armor file {f.name}")
            with open(Path(outputFolder, foundryPrefix+armorFile+outputSuffix), 'w') as dbFile:
                with open(f, newline='') as csvfile:
                    csvInput = csv.DictReader(csvfile)
                    for row in csvInput:
                        dbFile.write(json.dumps(makeOutputRecord(row, 'armor'))+"\n")
            print(f"Complete processing armor file {f.name}")
        if f.name == weaponFile+inputSuffix:
            # process as wepon
            print(f"processing weapon file {f.name}")
        if f.name == itemFile+inputSuffix:
            # process as item
            print(f"processing item file {f.name}")
        if f.name == ammoFile+inputSuffix:
            # process as ammo
            print(f"processing ammo file {f.name}")
    return True

if __name__ == "__main__":
    main()
