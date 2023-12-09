with open('input') as f:
    data = f.readlines()

max_rouge = 12
max_vert = 13
max_bleu = 14

solution1 = 0
solution2 = 0
for line in data:
    game_id = int(line.strip().split(':')[0].split()[1])
    pioches = line.strip().split(':')[1].split(';')
    records = {'id': game_id, 'blue':0, 'red': 0, 'green': 0}
    for pioche in pioches:
        for cube in pioche.split(','):
            num, color = cube.split()
            num = int(num)
            if records[color] < num: records[color] = num

    if records['red'] <= 12 and records['green'] <= 13 and records['blue'] <= 14:
        solution1 += records['id']
    power = records['red'] * records['green'] * records['blue']
    solution2 += power


print(solution2)
    