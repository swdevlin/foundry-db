import re


def parse(line):
    match = re.search(r'([^\d]+)\s+(\d+?)\s+(\d+?)\s+(.+?)\s+(.+?)\s+(.+?)\s+(.+?)\s+(.+?)\s+(.+)', line)
    tokens = []
    for i in range(9):
        tokens.append(match.group(i+1))
    return tokens


def columns():
    return [
        'Weapon',
        'TL',
        'Range',
        'Damage',
        'Kg',
        'Cost',
        'Magazine',
        'Mag Cost',
        'Traits',
    ]
