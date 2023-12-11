with open('input') as f:
    data = f.readlines()

for line in data:
    cartes, pari = line.split()
    print(cartes, pari)