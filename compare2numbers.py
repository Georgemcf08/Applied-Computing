#Ask the user for 2 numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
#Calculate which number is higher than print 
if num1 > num2:
    print (num1, " is greater than ", num2)
elif num1 < num2:
    print (num2, " is greater than", num1)
else:
    print (num1, "is equal to", num2)
