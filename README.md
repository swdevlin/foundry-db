Python program to convert weapons and armor infomration into Foundary compatible DB files

Assumes an input folder with files named as "armor.csv", "weapon,csv", "ammo.csv" and "item.csv"
Puts JSON/DB files into the output directory using the filename format as defined in the code

Foundry db files are multi-record files using /n separation. Each record is a single line of valid JSON, but the file as a whole is not JSON (improper record separator)
