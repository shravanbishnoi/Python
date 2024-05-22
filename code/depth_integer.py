ele_depth = 1   # tracking count for element depth OR list dimension
total_sum = 0  # sum accumulator

def find_integer_depth_sum(lst):
	"""Returns the sum of integers multiplied by their depth

	parameter lst: is the input list
	precondition: lst must contain integers only

	Testcases:
	>>> find_integer_depth_sum([1,[4,[6]]])
	27
	>>> find_integer_depth_sum([1,[2,2],[[3],2],1])
	23
	>>> find_integer_depth_sum([[[[[[[[[1]]]]]]]]])
	9
	>>> find_integer_depth_sum([1,[[[[[[[10]]]]]]]])
	81
	"""
	global ele_depth, total_sum
	for i in range(len(lst)):
		# Adding element multiplied by its depth if its type not equal to list
		if type(lst[i])!=list:
			total_sum += lst[i]*ele_depth
		
		# recursive calling if element type is list
		elif type(lst[i])==list:
			ele_depth += 1  # increasing depth by 1
			find_integer_depth_sum(lst[i])
		
		# At every last iteration reducing depth by -1
		if i==(len(lst)-1):
			ele_depth -= 1

	return total_sum
lst = [1,[2,2],5]  # input list

print(find_integer_depth_sum(lst))