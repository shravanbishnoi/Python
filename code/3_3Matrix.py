import itertools

possible = []
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if (i!=j!=k):
                if (i+j+k)==15:
                    num = str(i)+str(j)+str(k)
                    possible.append(num)
print(possible)
def is_magic_square(matrix):
    target_sum = 15
    for row in matrix:
        if sum(row) != target_sum:
            return False
    for col in range(3):
        col_sum = sum(matrix[row][col] for row in range(3))
        if col_sum != target_sum:
            return False

    diagonal1 = matrix[0][0] + matrix[1][1] + matrix[2][2]
    diagonal2 = matrix[0][2] + matrix[1][1] + matrix[2][0]
    
    if diagonal1 != target_sum or diagonal2 != target_sum:
        return False
    return True

def getMatrix(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if ((lst[j][0] not in lst[i]) and (lst[j][1] not in lst[i]) and (lst[j][2] not in lst[i])):
                num = lst[i] + lst[j]
                for k in range(j, len(lst)):
                    if ((lst[k][0] not in num) and (lst[k][1] not in num) and (lst[k][2] not in num)):
                        number = num+lst[k]
                        matrix = [int(i) for i in number]
                        permutations = list(itertools.permutations(matrix))
                        for permutation in permutations:
                            perm_matrix = [list(permutation[i:i + 3]) for i in range(0, 9, 3)]
                            if is_magic_square(perm_matrix):
                                return perm_matrix
print(getMatrix(possible))