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

    currPath = Path('.')
    listInputFiles = list(currPath.glob('*'+inputSuffix))
    print(listInputFiles)
    return True

if __name__ == "__main__":
    main()
