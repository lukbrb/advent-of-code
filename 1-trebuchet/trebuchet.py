with open('input') as f:
    lines = f.readlines()

# Note: le type str a déjà une méthode 'is_digit()'
def is_digit(item):
    try:
        int(item)  # pas besoin de le changer en int, pour pouvoir concatener à la fin
        return True
    except Exception as e:
        return False

digitnames = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def extract_line_digit(ligne):
    some_digits = []
    for i, item in enumerate(ligne):
        if is_digit(item):
            some_digits.append(item)
        for key, val in digitnames.items():
            if ligne[i:].startswith(key):
                some_digits.append(str(val))
    if some_digits:  # si liste non vide
        value = some_digits[0] + some_digits[-1]
    else: value = 0
    return int(value)


def solve_part1():
    somme = 0
    for line in lines:
        somme += extract_line_digit(line)
    print(somme)


solve_part1()