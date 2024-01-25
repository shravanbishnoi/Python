"""It is a script to receive user input and provide an answer according to the input.
   In this a module is imported which contains many helper functions to 
   process the correct output of this function.
   """

import shravan_a1

old=input("Enter original currency: ").upper()
new=input("Enter desired currency: ").upper()
amt=input("Enter original amount: ")


if (not(shravan_a1.is_currency(old))):
	print(old,"is not a valid currency")
	quit()

if (not(shravan_a1.is_currency(new))):
	print(new,"is not a valid currency")
	quit()

new_amt=shravan_a1.exchange(old,new,amt)
print(f"You can exchange {amt} {old} for {new_amt} {new}.")
