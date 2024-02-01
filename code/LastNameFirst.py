"""
This script contains a function
which take first and last name 
and returns last and first name
respectively in order 

Author: Shravan
Date: 14-01-2023
"""

def LastNameFirst(name):
	'''
	Returns: <name> but in the form <last name>,<first name>

	Precondition:<name>is in the form <first name><last name>
	with one blanks between the two names
	>>> last_name_first('Sitare Foundation')
	'Foundation, Sitare'
	'''
	assert type(name)==str,f'{name} must be a valid string'
	assert name.count(' ')>=1,'First name and Last name must be separated with atleast one space'
	names = name.split()
	return names[1].strip() + ', '+ names[0].strip()

print(LastNameFirst('Sitare  University'))


# For testcases
if __name__=='main_':
 	import doctest
 	doctest.testmod()
