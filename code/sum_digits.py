n = 5345
def sum_digits(n):
	"""Returns: the sum of digits of a input number n

	Parameter n: is the input
	Precondition: n should be a positive integer.

	Testcases:
	>>> sum_digits(5)
	1
	>>> sum_digits(12345)
	15
	"""
 
	sum_digits = 0
	loop_var = True
	while loop_var:
		if len(str(n))==1:
			sum_digits += int(n)
			loop_var = False
		else:
			n = str(n)
			sum_digits += int(n[0])
			n = int(n[1:])
	return sum_digits
print(sum_digits(n))