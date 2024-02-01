def removeTuple(lst, k):
    """Removes tuples with k length from the lst"""
    i = 0
    while i<len(lst):
        if len(lst[i])==k:
            lst.pop(i)
        else:
            i += 1
    return lst
lst = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
modifiedlst = removeTuple(lst, 1)
print(modifiedlst)