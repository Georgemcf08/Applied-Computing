#Ask the user how much money they have
Lunch = float(input("How much money do you have? "))
#Ask the user how much money they haven spent on school lunch
Spent = float(input("How much money have you spent on school lunch? "))
#Subtract them from each other then print
Total_Spent = Lunch - Spent
print("You have", Total_Spent , "left")