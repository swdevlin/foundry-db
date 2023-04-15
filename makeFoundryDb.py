import csv
import json
from pathlib import Path

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
            "target": {
                "value": None,
                "width": None,
                "units": "m",
                "type": "none"
            },
            "range": "0",
            "damage": "",
            "damageBonus": 0,
            "magazineSize": 0,
            "ammo": "100",
            "useConsumableForAttack": "",
            "magazineCost": 0,
            "type": "weapon",
            "lawLevel": 0,
            "rangeBand": "",
            "weaponType": "",
            "damageType": "NONE",
            "rateOfFire": "1",
            "recoil": False,
            "features": "",
            "armorPiercing": 0,
            "handlingModifiers": ""
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
        "_id": "JMVP1GTuRWbeR9Uh"
    }
    if type == "armor":
        record['type'] = 'armor'
        record['system']['armor'] = 0
        record['system']['secondaryArmor']['value'] = 0
        record['system']['secondaryArmor']['protectionTypes'] = []
        record['system']['radiationProtection']['value'] = 0
    if type == "weapon":
        record['type'] = 'weapons'
        record['system']['armor'] = 0
        record['system']['secondaryArmor']['value'] = 0
        record['system']['secondaryArmor']['protectionTypes'] = []
        record['system']['radiationProtection']['value'] = 0
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

def makeOutputRecord(csvData:dict, type:str)->dict:
    if type == 'armor':
        # process as armor
        outputRecord = setDbRecord(type)
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
