with open('input') as f:
    lines = f.readlines()


def is_digit(item):
    try:
        int(item)  # pas besoin de le changer en int, pour pouvoir concatener à la fin
        return True
    except Exception as e:
        return False

def extract_line_digit(ligne):
    digits = []
    for item in ligne:
        if is_digit(item):
            digits.append(item)
    if digits:  # si liste non vide
        value = digits[0] + digits[-1]
    else: value = 0
    return int(value)


def solve_part1():
    somme = 0
    for line in lines:
        somme += extract_line_digit(line)
    print(somme)

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

def replace_name_by_digits(ligne):
    print(ligne)
    digits = []
    nums_found = []
    overlap = False
    for num in digitnames.keys():
        start_idx = ligne.find(num)
        if start_idx == -1:
            continue
        end_idx = start_idx + len(num)
        digits.append(start_idx)
        digits.append(end_idx)
        nums_found.append(num)
     
    if len(digits) != len(set(digits)):
        overlap = True
        
    for num in nums_found:
        if overlap:
            ligne = ligne.replace(num[:-1], str(digitnames[num]))
        else:
            ligne = ligne.replace(num, str(digitnames[num]))
    print(ligne)

        

for line in lines:
    replace_name_by_digits(line)

