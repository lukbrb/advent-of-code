with open('input') as f:
    data = f.readlines()


h = len(data)
w = len(data[0]) - 1 # -1 car on enleve '\n'

matrice = [[c for c in line.replace('\n', '')] for line in data]

# for i in range(h):
#     for j in range(w):
#         if j == 0 or i == 0:
#             j += 1
#         if all([matrice[i-1][j-1], matrice[i][j-1], matrice[i][j+1], matrice[i+1][j], matrice[i+1][j+1])
#             print(matrice[i][j])