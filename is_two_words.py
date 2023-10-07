"""
This script contains a function to check
Does the input string contain two words?

Author: Shravan
Date: 02-02-2023
"""

def IsTwoWords(string):
	"""
	Returns: True if w is 2 words separated by 1 or more spaces.

	A word is a string with no spaces.So this means that 
	1. The first character is not a space (or empty)
	2. The last character is not a space (or empty)
	3. There is at least one space in the middle
	4. If there is more than one space, the spaces are adjacent
	Precondition: w is a str
	"""
	# splits on ' ' and checks length after splitting
	if len(string.split()) == 2:
		if string[0]==' ' or string[-1]==' ':
			return False
		return True
	return False

result = IsTwoWords("Sitare  University")
print(result)