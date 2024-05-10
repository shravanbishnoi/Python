def power(x, n):
	"""Returns: result of x^n

	parameter x: is the input base number
	precondition: x must be a number.

	parameter n: is the input power number
	precondition: n must be a number.

	Testcases:
	>>> power(10,3)
	1000
	>>> power(-1,3)
	-1
	>>> power(0,3)
	0
	>>> power(0,0)
	1
	>>> power(0,-3)
	'Not defined'
	"""

	if x==0 and n<0:
		return 'Not defined'
	return x**n
print(power(0,0))