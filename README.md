# About
A set of tools to generate Foundry twodsix compendium files. twodsix does not ship with Mongoose Traveller (MgT) data. Using 
these tools one can create MgT compendiums of items.

To use the tools you will need to be able to access the file
system of the Foundry host.

# Generating Compendium Files

Create placeholder Compendium files for each item type.

## Text to CSV
If you already have CSV files you can skip this step. If you
are copy/pasting from the PDFs you might find it easier to create
text files and use the `parser.py` script to convert them to CSV.

For text files, for example

```
Shot Pistol 5 2 3D 0.5 Cr60 1 Cr5 -
Snub Pistol 8 5 3D-3 - Cr150 6 Cr10 Zero-G
```

use `python parse.py {type} {infile} {outfile}` to convert the text to CSV.

* `type` is the type of data being converted. Options are: armor, gun
* `infile` is the name of the text file
* `outfile` is the name of the CSV file to generate

Sample CSV
```
Weapon,TL,Range,Damage,Kg,Cost,Magazine,Mag Cost,Traits
Shot Pistol,5,2,3D,0.5,Cr60,1,Cr5,-
Snub Pistol,8,5,3D-3,-,Cr150,6,Cr10,Zero-G
```

Alternately you can just start with CSV files.

## CSV to db

If you are creating your own CSV files, note that each item type has its own columns. See the examples in the repo.

use `python generate_db.py {type} {infile} {outfile}` to convert the CSV file to a Foundry .db file.

* `type` is the type of data being converted. Options are: armor, weapon
* `infile` is the name of the CSV file
* `outfile` is the name of the .db file to generate

Sample:
```json lines
{"name": "Shot Pistol (TL 5)", "type": "weapon", "img": "systems/twodsix/assets/icons/gun-combat-slug-pistol.svg", "system": {"name": "", "techLevel": 5, "description": "", "shortdescr": "", "quantity": 1, "weight": 0.5, "price": 60.0, "traits": [], "consumables": [], "skillModifier": 0, "skill": "", "associatedSkillName": "", "equipped": "backpack", "docReference": "", "pdfReference": {"type": "", "href": "", "label": ""}, "target": {"value": null, "width": null, "units": "m", "type": "none"}, "range": "2", "damage": "3D", "damageBonus": 0, "magazineSize": "1", "ammo": "1", "useConsumableForAttack": "", "magazineCost": 5.0, "type": "weapon", "lawLevel": 0, "rangeBand": "", "weaponType": "", "damageType": "NONE", "rateOfFire": "None", "recoil": false, "features": "-", "armorPiercing": 0, "handlingModifiers": ""}, "effects": [], "flags": {"twodsix": {}, "core": {"sourceId": "Item.q21aqTzFu2knzopT"}}, "_stats": {"systemId": "twodsix", "systemVersion": "2.31.0", "coreVersion": "10.291", "createdTime": 1684417563354, "modifiedTime": 1684417563354, "lastModifiedBy": "X7Zc9wesNGsI137g"}, "folder": null, "sort": 0, "ownership": {"default": 0, "OK9YthkIIxCpCkT0": 3}, "_id": "58c19ca3f14bdb8d"}
{"name": "Snub Pistol (TL 8)", "type": "weapon", "img": "systems/twodsix/assets/icons/gun-combat-slug-pistol.svg", "system": {"name": "", "techLevel": 8, "description": "", "shortdescr": "", "quantity": 1, "weight": 0, "price": 150.0, "traits": [], "consumables": [], "skillModifier": 0, "skill": "", "associatedSkillName": "", "equipped": "backpack", "docReference": "", "pdfReference": {"type": "", "href": "", "label": ""}, "target": {"value": null, "width": null, "units": "m", "type": "none"}, "range": "5", "damage": "3D-3", "damageBonus": 0, "magazineSize": "6", "ammo": "6", "useConsumableForAttack": "", "magazineCost": 10.0, "type": "weapon", "lawLevel": 0, "rangeBand": "", "weaponType": "", "damageType": "NONE", "rateOfFire": "None", "recoil": true, "features": "", "armorPiercing": 0, "handlingModifiers": ""}, "effects": [], "flags": {"twodsix": {}, "core": {"sourceId": "Item.q21aqTzFu2knzopT"}}, "_stats": {"systemId": "twodsix", "systemVersion": "2.31.0", "coreVersion": "10.291", "createdTime": 1684417563354, "modifiedTime": 1684417563354, "lastModifiedBy": "X7Zc9wesNGsI137g"}, "folder": null, "sort": 0, "ownership": {"default": 0, "OK9YthkIIxCpCkT0": 3}, "_id": "2c7c0013e2d99a8f"}
```

Copy the contents of the .db file generated to the Foundry .db placeholder file you created.

It is best to copy the .db file when Foundry is not running.