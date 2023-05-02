import argparse
import csv
import importlib
import json


def main ():
    arg_parser = argparse.ArgumentParser(description='Mongoose csv to twodsix db')
    arg_parser.add_argument('type')
    arg_parser.add_argument('csv')
    arg_parser.add_argument('db')

    args = arg_parser.parse_args()

    converter = importlib.import_module(f'items.{args.type}')

    csv_filename = args.csv
    db_filename = args.db
    with open(csv_filename, 'rt', encoding='utf-8') as csv_file:
        with open(db_filename, 'wt', encoding='utf-8') as db_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                db_entry = converter.create_item(row)
                db_file.write(json.dumps(db_entry) + "\n")


if __name__ == "__main__":
    main()
