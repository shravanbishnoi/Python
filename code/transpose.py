table = [[1, 2], [3, 4], [5, 6]]
def transpose(table):
	"""Returns: copy of table with rows and columns swapped

	Precondition: table is a (non-ragged)2d list"""
	numrows = len(table) # counts the no. of elements in rows
	numcols = len(table[0])  # counts the no. of elements in columns
	# initialise list
	result = []
	for i in range(numcols):
		# initialise list
		row_1 = []
		for j in range(numrows):
			row_1.append(table[j][i])
		result.append(row_1)
	return result
print(transpose(table))

