string = "malayalam"
def is_palindrome(string):
	try:
		assert type(string)==str
	except:
		return "Input is not string type"
	if len(string)<=1:
		return True
	left = True if string[0]==string[-1] else False
	right = is_palindrome(string[1:-1])

	return right and left
print(is_palindrome(string))
