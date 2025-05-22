#base number
number = 100
#ask the user for a number between 1 and 10 then divide 100 by that number
while number > 10 or number < 1:
    number = int(input("Please enter a number between 1 and 10: "))
print("Your number multiplied by 10 is:", number * 10)
