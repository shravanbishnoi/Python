l = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

# Q-1
for i in l:
    for j in range(1):
        print(i[j], i[j+1], i[j+2])

# Q-2
for i in range(len(l[0])):
    for j in range(len(l)-2):
        print(l[j][i], l[j+1][i], l[j+2][i])

