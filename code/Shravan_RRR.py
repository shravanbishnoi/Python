# first read overs bowled,target,runs scored by which we have to find RRR
overs_bowled = float(input("Enter the number of overs bowled: "))
target = int(input("Enter the target: "))
current_runs = int(input("Enter the runs scored: "))

def calculating_rrr(overs_bowled,target,current_runs):
	"""Returns: required run rate team needs to win the match.

	This function takes the required inputs from the user,
	calculate and returns the required run rate a team 
	needs to win the cricket match. 

	parameter overs_bowled:no.of overs bowled
	precondition:must be a float upto one digit after decimal.

	parameter target:target to chase
	precondition:must be an integer.

	parameter current_runs:runs scored
	precondition:must be an integer.

	Examples:
	>>> calculating_rrr(10,200,100)
	10.0
	>>> calculating_rrr(10.3,200,100)
	10.526315789473685
	>>> calculating_rrr(10.6,200,100)
	'Invalid overs bowled entered'
	>>> calculating_rrr(20.0,200,100)
	'Invalid overs bowled entered'
	>>> calculating_rrr(21.0,200,100)
	'Invalid overs bowled entered'
	>>> calculating_rrr(10.3,150,151)
	'Hey! you have won the match'
	"""

	# check for no. of overs bowled entered is valid
	if (overs_bowled*10) % 10 > 5 or overs_bowled >= 20.0:
		return "Invalid overs bowled entered"

	# check for current runs
	elif current_runs > target:
		return "Hey! you have won the match"

	else:
		# finds no. of balls remaining
		no_of_remainingballs = 120 - ((int(overs_bowled)*6)+(overs_bowled*10)%10)
		# converting balls remaining into overs
		overs_remaining = no_of_remainingballs/6
		# finds required runs
		runs_required = target - current_runs
		# Hence finds run rate required
		required_run_rate = runs_required/overs_remaining
		return (f"Required run rate is: {required_run_rate}")

print(calculating_rrr(overs_bowled,target,current_runs))
