import csv
import json
from pathlib import Path

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
            with open(f, newline='') as csvfile:
                csvInput = csv.reader(csvfile, delimiter=' ', quotechar='"')
                for row in csvInput:
                    print(', '.join(row))
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
