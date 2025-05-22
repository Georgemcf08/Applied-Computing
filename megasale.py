#Ask Cashier how much the customer spent
amount = float(input("Enter the total amount spent: "))
#Based on the ammount of money the customer spent print a voucher 
if amount > 20:
    print("Give the customer a $3 voucher.")
elif amount > 10:
    print("Give the customer a $1 voucher.")
else:
    print("No voucher.")
