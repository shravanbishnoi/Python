"""
This script contains a function
which prints a Christmas Tree
of asterisks

Author: Shravan
Date: 25-01-2023
"""


def christmas(first_row, incr, num_rows, line_width):
	"""prints christmas tree using asterisk.

	parameter first_row: number of asterisk must be printed on first row.
	precondition: first_row must be a positive integer.

	parameter incr: increment of asterisk that every next line should follow.
	precondition: incr must be a positive integer and for trunk it should be 0.

	parameter num_rows: Total number of rows program should contain.
	precondition: num_rows must be a positive integer.

	parameter line_width: is the width of line about which program should be center aligned.
	precondition: line_width must be a positive integer.
	"""

	# check for incr input if odd make it even by adding one
	increment = incr
	if increment%2 != 0:
		increment = incr + 1

	# check for valid first_row input
	if first_row <= 0:
		print("invalid input: first line input should be positive integer")
		return

	# check for increment input in each following line
	if increment < 0:
		print("invalid input: increment should be 0 or positive integer")
		return

	# check for total no. of rows input
	if num_rows <= 0:
		print("invalid input: Total number of lines to be printed should be positive integer")
		return

	# check for line_width along which program has to center aligned with the last trapezoid
	if line_width < first_row + (increment * num_rows):
		print("invalid input: please increase the line width")
		return

	# now print rows in a loop
	tree = ''
	for i in range(num_rows):
		num_asterisk = first_row + increment * i # asterisks in this line
		num_spaces = (line_width - num_asterisk) // 2 # spaces before asterisk
		# print(' ' * num_spaces + '*' * num_asterisk)
		tree = tree + (' ' * num_spaces + '*' * num_asterisk) + '\n'
	print(tree.rstrip()) # strips the spaces from the right of the string


christmas(1,3,10,100)
christmas(17,3,10,100)
christmas(27,3,10,100)
christmas(10,0,5,100)
