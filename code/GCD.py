"""
This script contains a function to calculate GCD
of two numbers.

Author: Shravan
Date: 01-02-2023
"""

count_frame = 0  # counting the frames 
def Cal_GCD(a,b):
	"""
	returns GCD(Greatest common diviser) of a and b 
	GCD of two and more numbers is the greatest common
	factor number that divides them, exactly.

	parameter a: is a input integer
	precondition: a must be positive integer

	parameter b: is a input integer
	precondition: b must be positive integer.
	"""
	global count_frame
	assert type(a) and type(b) == int, repr(a) + ',' + str(b) + ' is not integer'
	assert a or b >= 0, str(a) + ',' + repr(b) + ' is not positive integer'

	# checks if zero is an input
	if a == 0:
		return b
	elif b == 0:
		return a

	# Handling small data
	if a%b == 0:
		return b

	# recursive calls
	right = Cal_GCD(b, a%b)
	count_frame += 1  # increamenting counting variable
	return right

print(Cal_GCD(2, 20))
print(count_frame)
