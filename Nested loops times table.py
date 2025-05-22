#Ask the user for a number
multiplied_number = int(input("Insert a number to be multiplied: "))
#Print the multiplication table for the number than print
print(f"{multiplied_number} Times Table")
for b in range (1, 13):
    print(f"{multiplied_number} times {b} = {multiplied_number*b}")