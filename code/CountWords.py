"""
This script contains a function
which takes two strings and a word
and prints the string name with higher 
occurrence of the given word

Author: Shravan
Date: 20-01-2023

"""

first = input("Enter the first string: ")          # Reads the first input
second = input("Enter the second string: ")        # Reads the second input
word = input("Enter the word to check for: ")      # Reads the input word

def count_word(first,second,word):
	"""prints the string name with higher occurrence of word
	
	parameter first: first string in which we have to count the word
	Precondition: first must a string

	parameter second: second string in which we have to count the word
	Precondition: second must be string

	parameter word: word whose occurences we have to count
	precondition: word must be a string
	"""

	# converts inputs into lowercase
	first_str = first.lower()
	second_str = second.lower()
	word_new = word.lower()

	first_str_new = ''     # initialise string
	for i in first_str:
		if i.isalnum():
			first_str_new = first_str_new + i      # collects alphanumeric characters
		else:
			first_str_new = first_str_new + ' '    # replaces non-alphanumeric characters with space

	second_str_new = ''    # initialise string
	for i in second_str:
		if i.isalnum():
			second_str_new = second_str_new + i      # collects alphanumeric characters
		else:
			second_str_new = second_str_new + ' '    # replaces non-alphanumeric characters with space

	# splits both strings
	first_str_new = first_str_new.split()
	second_str_new = second_str_new.split()

	Total_first = 0   # initialise count for the words
	for i in first_str_new:
		if word_new == i:
			Total_first += 1  # adds one if word exactly matches
			
	Total_second = 0   # initialise count for the words
	for i in second_str_new:
		if word_new == i:
			Total_second += 1  # adds one if word exactly matches

	# prints the string name with greater occurrence of word
	if Total_first > Total_second:
		print("first")

	elif Total_first < Total_second:
		print("second")

	else:
		print("equal") # prints equal if occurrence is equal

count_word(first,second,word)
