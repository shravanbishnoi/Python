def sortTuple(tup):
    """Returns the tuple list sorted on the basis of second item of each tuple."""
    for i in range(len(tup)):
        for j in range(0, len(tup)-i-1):
            if tup[j][1] > tup[j+1][1]:
                temp = tup[j]
                tup[j] = tup[j+1]
                tup[j+1] = temp
    return tup
tup = [('for', 24), ('is', 10), ('Geeks', 28), ('Geeksforgeeks', 5), ('portal', 20), ('a', 15)]
sortedTup = sortTuple(tup)
print(sortTuple)