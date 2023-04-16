import argparse
import csv

from armor_parser import parse_armor


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mongoose Item Text File Parser')
    parser.add_argument('filename')
    parser.add_argument('csvfilename')
    args = parser.parse_args()
    with open(args.csvfilename, 'wt', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([
            'Armour Type',
            'Protection',
            'Secondary',
            'Secondary Type',
            'TL',
            'Rad',
            'Kg',
            'Cost',
            'Required Skill'
        ])
        with open(args.filename, 'rt') as items:
            for line in items:
                line = line.strip()
                item = parse_armor(line)
                writer.writerow(item)

