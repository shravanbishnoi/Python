import random
roll = random.randint(1, 6)
goal = 50
def roll_past(goal):
	"""Returns: The score from rolling a die until passing goal"""
	score = 0
	loop_var = True
	while loop_var:
		roll = random.randint(1, 6)
		if roll == 1:
			return 0
		else:
			score += roll
			loop_var = score < goal
	return score
print(roll_past(goal))