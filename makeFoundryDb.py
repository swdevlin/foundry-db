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
                "shortdescr": "",
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
                "isPowered": false
            },
            "effects": [],
            "flags": {
                "twodsix": {
                    "newItem": true
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
            "folder": null,
            "sort": 0,
            "ownership": {
                "default": 0,
                "OK9YthkIIxCpCkT0": 3
            },
            "_id": "bmMpPYi1MEHTx7mh"
        }
        outputRecord['img'] = "icons/svg/item-bag.svg"
        outputRecord['name'] = csvData['name']
        outputRecord['system']['techLevel'] = csvData['techlevel']
        outputRecord['system']['quantity'] = csvData['quantity']
        outputRecord['system']['wieght'] = csvData['weight']
        outputRecord['system']['price'] = csvData['price']
        outputRecord['system']['armor'] = csvData['armor']
        outputRecord['system']['secondaryArmor']['value'] = csvData['secondary']
        outputRecord['system']['radiationProtection']['value'] = csvData['radiation']
        for t in csvData['secondarytypes'].split(":"):
            outputRecord['system']['secondaryArmor']['protectionTypes'].append(t)
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
            print(f"processing armor file {f.name}")
            with open(Path(outputFolder, foundryPrefix+armorFile+outputSuffix), 'w') as dbFile:
                with open(f, newline='') as csvfile:
                    csvInput = csv.DictReader(csvfile)
                    for row in csvInput:
                        dbFile.write(makeOutputRecord(row, 'armor'))
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
