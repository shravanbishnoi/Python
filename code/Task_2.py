# stores the input given by user
string = input("Enter the string: ")
letter = input("Enter the letter: ")

def task_2(string,letter):
	"""prints the words starting with the given letter from the given string and prints such number of words

	The program prints such words which starts with the given letter 
	and total number of such words in the given string.The program is for case-insensitive english alphabets.
	program reflects a word with only enlish alphabets by dropping the numbers and special characters

	parameter string: The string from the words to be taken out
	precondition: string must be a string

	parameter letter: words starting with this letter has to be taken out
	precondition: letter must contain only one english alphabet

	Testplan:
	>>> task_2(' Hello worldwide ','w')  # test for one word
	 worldwide
	1
	>>> task_2(' Are you  A   GOOD PROGRAMMER and   artificial man as well as.? ','a') # test for multiple words
	 are a and artificial as as
	6
	>>> task_2(' ...Are you  A   GOOD PROGRAMMER? and   artificial man as!! well as.? ','a')  # test for multiple words with special charaters at beginning and end
	 are a and artificial as as
	6
	>>> task_2(' Hello worldwide ','1')  # test for non-alphabetical letter
	Invalid input: letter must be an english alphabet
	>>> task_2(' Hello worldwide ','a')  # test for no word present starting with given letter
	There is no such word starting with: a
	"""

	# modifies string argument by adding only one space at the beginning and also at the end
	# converts string, letter into lower case and strips them
	string = (' ' + string.strip() + ' ').lower()
	letter = letter.strip().lower()

	# check if the letter contains english alphabet OR not
	if letter.isalpha() == False:
		print("Invalid input: letter must be an english alphabet")
		return

	# initialize the word count and final string with such words starting with the given letter
	total_words = 0
	string_1 = ''

	for i in range(len(string)-1):
		# checks for non-alphabetical character
		if string[i].isalpha() == False:

			# checks if the starting letter of word is same as letter
			if string[i+1] == letter:
				# Adds 1 to total_words
				total_words = total_words + 1
				word = string[i+1 : string.find(' ', i+1)]

				# running for loop to collect only alphabets and remove other numbers OR special character
				word_string = ''
				for x in word:
					if x.isalpha() == True:
						word_string = word_string + x
				string_1 = string_1 + ' ' + word_string  # final variable to reflect the words to the accumulator

	# prints message to the user that there is no such word starting with the given letter
	if total_words == 0:
		print(f"There is no such word starting with: {letter}")
		return

	print(string_1)
	print(total_words)

task_2(string,letter)

# code to run the testplan please comment the function call before using it to avoid duplicate running
# if __name__ == '__main__':
# 	import doctest
# 	doctest.testmod()