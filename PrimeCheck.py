"""
This script contains a function
which take an int and returns True
if it is a prime otherwise False

Author: Shravan
Date: 12-01-2023
"""

 
def prime(n):
	"""Python function that takes a number as a parameter and check the number is prime or not."""
	if n==1:
		return False
	elif n==2:
		return True
	else:
		for x in range(2,n):
			if(n % x==0):
				return False
		return True
print(prime(5))
