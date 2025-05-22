#Ask the user how many people to share the money with
shares =int(input("How many people do you want to share this money with? "))
#Divide 1000 by the number of people the user wants
money = 1000/shares
#print
print('Each person will get' , money)