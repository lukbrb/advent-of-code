with open('input') as f:
    data = f.readlines()

tot_value = 0
for line in data:
    carte = int(line.split(':')[0].split()[1])
    win_nums = list(map(int, line.split(':')[1].split('|')[0].split()))
    my_nums = list(map(int, line.split(':')[1].split('|')[1].split()))

    value_card = 0
    for n in my_nums:
        if n in win_nums:
            if value_card == 0:
                value_card += 1
            else:
                value_card *= 2
    tot_value += value_card
            
print(tot_value)