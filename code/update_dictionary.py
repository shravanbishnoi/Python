# test_dict = {"Gfg":5, "is":8, "Best":10, "for":8, "Geeks":9}
# updict = {"Geeks":10, "Best":17}
# def update_dict(test_dict, updict):
# 	"""Returns: the updated dict to be updated from the updict"""
# 	for key in updict:
# 		if key in test_dict:  
# 			test_dict[key] = updict[key]
	
# update_dict(test_dict, updict)
# print(test_dict) 

dict_1 = {'emp1': {'name': 'Hameed', 'age': 29,'Designation':'Programmer','Salary':100},'emp2': {'name': 'Gurjeet','age': '45', 'Designation':'Programmer','Salary':30000}}
s = 9999
d = 'Programmer'
def up_dict(dict_1, d, s):
	# itorating over dictionary if d matches Designation in the dict_1
	for key in dict_1:
		if dict_1[key]['Designation']==d:
			dict_1[key]['Salary']=s  # updates salary to given salary s corresponding to that key
	
up_dict(dict_1, d, s)
print(dict_1)