"""
This script contains a function
which take an int and returns a
list of all square numbers less than n

Author: Shravan
Date: 15-01-2023
"""


def ListOfSquares(n):
	"""Returns: a list of all squares less than n.
	
	Parameter n: is the number
	Precondition: n must be a integer"""
	assert type(n)==int, f'{n} is not a integer'
	# Using list comprehension
	# lst = [i*i for i in range(n) if i*i<n]

	# using while loop
	i = 0  # Loop variable
	lst=[] # intializer
	while i*i<n:
		lst.append(i*i)
		i += 1
	return lst

print(ListOfSquares(26))