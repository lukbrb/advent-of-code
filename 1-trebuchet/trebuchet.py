with open('input') as f:
    lines = f.readlines()

# Note: le type str a déjà une méthode 'is_digit()'
def is_digit(item):
    try:
        int(item)  # pas besoin de le changer en int, pour pouvoir concatener à la fin
        return True
    except Exception as e:
        return False

def extract_line_digit(ligne):
    some_digits = []
    for item in ligne:
        if is_digit(item):
            some_digits.append(item)
    if some_digits:  # si liste non vide
        value = some_digits[0] + some_digits[-1]
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
    digits = []
    nums_found = []
    overlap = False
    for key, num in digitnames.items():
        start_idx = ligne.find(key)
        if start_idx == -1:
            continue
        end_idx = start_idx + len(key)
        digits.append(start_idx)
        digits.append(end_idx)
        nums_found.append(key)
     
    if len(digits) != len(set(digits)):
        overlap = True
        
    for num in nums_found:
        if overlap:
            ligne = ligne.replace(ligne[start_idx:end_idx], str(num))
        else:
            ligne = ligne.replace(key, str(num))
    return ligne.strip()


# def replace_name_by_digits(ligne):
#     for key, val in digitnames.items():
#         if key in ligne:
#             ligne = ligne.replace(key, str(val)).strip()

#     return ligne

somme = 0
for line in lines:
    print(line.strip())

    line = replace_name_by_digits(line)
    print(line)
    # somme += extract_line_digit(line)
# print(somme)
