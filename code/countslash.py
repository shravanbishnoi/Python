def count_slash(s):
	"""Returns: the number of times'/' appears in s.

	parameter s: is a input string
	precondition: s can be possibly empty string"""
	count = 0
	# using while loop
	i = 0 # loop var
	while i < len(s):
		if s[i]=='/':
			count += 1
		i += 1 # increase loop var

	return count
print(count_slash('sj/s //kd/d/d'))
