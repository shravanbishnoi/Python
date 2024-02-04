"""
This script contains a inverse_2_2 function that returns the 
inverse of any 2x2 matrix

Author: Shravan
Date: 30-01-2023
"""

lst = [[1, 2], [2, 2]]
def inverse_2_2(lst):
	"""Returns: inverse of a 2x2 matrix

	parameter lst: is a input list
	precondition: lst must only contain intergers or floats.
	"""
	# Initialize list
	row_1 = []
	for i in lst:
		for j in i:    # converting 2D list to 1D
			row_1.append(j)

	# Calculating determinant of the given matrix
	det = (row_1[0]*row_1[3]) - (row_1[2]*row_1[1])

	# Adjoint of given matrix
	row_2 = [row_1[3], -(row_1[1]), -(row_1[2]), row_1[0]]

	# checks if determinant is zero
	if det == 0:
		return 'Since det(A)=0 ;Matrix is not invertible'

	else:
		# Initialize list
		inverse = []
		for i in range(1):
			inverse.append([(row_2[0])/det, (row_2[1])/det]) # first row of inverted matrix

		for j in range(1):
			inverse.append([(row_2[2])/det, (row_2[3])/det]) # second row of inverted matrix
	return inverse

print(inverse_2_2(lst))