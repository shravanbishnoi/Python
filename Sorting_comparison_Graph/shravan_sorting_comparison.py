###################### INSERTION SORT #########################

def insertion_sort(b):
	i = 0
	while i<len(b):
		pushdown(b,i)
		i += 1
def pushdown(b,i):
	global comp_insertion
	j = 0
	while j<i:
		comp_insertion += 1
		if b[i-j]<b[i-j-1]:
			swap_Insertion(b,i-j,i-j-1)
			j+=1
		else:
			break
def swap_Insertion(b,v1,v2):
	global swap_insertion
	swap_insertion += 1
	temp = b[v1]
	b[v1] = b[v2]
	b[v2] = temp


###################### SELECTION SORT #########################

def selection_sort(lst):
	i = 0
	while i<len(lst)-1:
		mini = find_minimum(lst, i)
		swap_Selection(lst,i,mini)
		i += 1
def find_minimum(lst,i):
	"""Returns the index of the minimum of the list"""
	global comp_selection
	j = i
	mini = i
	while j<len(lst):
		comp_selection += 1
		if lst[mini]>lst[j]:
			mini = j
		j += 1
	return mini
def swap_Selection(b,idx1,idx2):
	global swap_selection
	swap_selection += 1
	temp = b[idx1]
	b[idx1] = b[idx2]
	b[idx2] = temp


############################# QUICK SORT ######################

def partition(b,h,k):
	""" Returns the new position of 
	pivot in partitioned list b[h..k]. 
	Partition list b[h..k] around a 
	pivot x = b[h]"""
	global comp_quick
	pivot = b[h]
	j = k+1
	i = h
	while i<j-1:
		comp_quick += 1
		if b[i+1]>=pivot:
			swap_Quick(b,i+1,j-1)
			j -= 1
		else:
			swap_Quick(b,i,i+1)
			i += 1
	return i
def swap_Quick(b,idx1,idx2):
	global swap_quick
	swap_quick += 1
	temp = b[idx1]
	b[idx1] = b[idx2]
	b[idx2] = temp
def quick_sort(b,h,k):
	if (k-h)<1:
		return None
	j = partition(b, h, k)
	quick_sort(b, h, j-1)
	quick_sort(b, j+1,k)


import random
import plotly.express as px
import plotly.graph_objects as go

swap_insertion = 0
swap_selection = 0
swap_quick = 0
comp_insertion = 0
comp_selection = 0
comp_quick = 0


lst_length = [] # for x-axis
swap_lst_insertion = []
swap_lst_selection = []
swap_lst_quick = []

comp_lst_insertion = []
comp_lst_selection = []
comp_lst_quick = []

for x in range(30, 1500, 100):
	lst_length.append(x)
	for y in range(3):
		b = [random.randint(1,x) for i in range(x)]
		c = b
		d = b
		insertion_sort(b)
		selection_sort(c)
		quick_sort(d,0,len(d)-1)


###############################################################

	# finding average
	swap_lst_insertion.append(swap_insertion/3)
	swap_lst_selection.append(swap_selection/3)
	swap_lst_quick.append(swap_quick/3)

	comp_lst_insertion.append(comp_insertion/3)
	comp_lst_selection.append(comp_selection/3)
	comp_lst_quick.append(comp_quick/3)

	# reseting to zero for next iteration count
	swap_insertion = 0
	swap_selection = 0
	swap_quick = 0
	comp_insertion = 0
	comp_selection = 0
	comp_quick = 0


# plotting for number of swaps in the three methods
fig = go.Figure()
fig.add_trace(go.Scatter(name = 'swap_insertion', x = lst_length, y = swap_lst_insertion))
fig.add_trace(go.Scatter(name = 'swap_selection', x = lst_length, y = swap_lst_selection))
fig.add_trace(go.Scatter(name = 'swap_quick', x = lst_length, y = swap_lst_quick))
fig.show()

# plotting for number of comparison in the three methods
fig = go.Figure()
fig.add_trace(go.Scatter(name = 'insertion_comparison', x = lst_length, y = comp_lst_insertion))
fig.add_trace(go.Scatter(name = 'selection_comparison', x = lst_length, y = comp_lst_selection))
fig.add_trace(go.Scatter(name = 'quick_comparison', x = lst_length, y = comp_lst_quick))
fig.show()