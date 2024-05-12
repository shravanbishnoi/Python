
lst = [input("Enter your name: "),float(input("Enter your height: ")),float(input("Enter your weight: "))]

def bmi(lst):
    lst_new = []
    bmi = lst[2]/((lst[1]/100)**2)
    if bmi < 20:
        data = lst[0] + ": Under weight"
        lst_new.append(data)

    elif bmi >= 20:
        data = lst[0] + ": Normal"
        lst_new.append(data)
            
    elif bmi >= 30:
        data = lst[0] + ": Over weight"
        lst_new.append(data)

    return lst_new
print(bmi(lst))