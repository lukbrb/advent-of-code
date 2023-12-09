def solve_part1():
    with open("input") as f:
        temps, distances = f.readlines()

    temps = list(map(int, temps.split(':')[1].split()))
    distances = list(map(int, distances.split(':')[1].split()))

    sol = 1
    for t, d in zip(temps, distances):
        count = 0
        for i in range(t):
            dist = i * (t - i)
            if dist > d:
                count += 1
        sol *= count
    print(sol)

with open("input") as f:
    temps, distances = f.readlines()

temps = int(temps.split(':')[1].replace(' ', ''))
distance = int(distances.split(':')[1].replace(' ', ''))

count = 0
for i in range(temps):
    dist = i * (temps - i)
    if dist > distance:
        count += 1

print(count)