#function to calculate area
def area(length, width):
    return length * width
#function to calculate perimeter
def perimeter(length, width):
   return 2 * (length + width)
# Function to calculate volume
def volume(length, width, height):
    return length * width * height
#Ask the user what they want to calculate
response = None
while response not in ("a","p", "v"):
    response = input("Do you want to calculate area, perimeter or volume? Enter a or p or v: ")
    response = response.lower()
#Work out either Area, Width or Volume based off of user input
if response == "a":
    length = float(input ("Enter the length of the rectangle: "))
    width = float(input ("Enter the width of the rectangle: "))
    print("Area =", area(length, width))

elif response == "p":
    length = float(input ("Enter the length of the rectangle: "))
    width = float(input ("Enter the width of the rectangle: "))
    print("Perimeter =", perimeter(length, width))
    
elif response =="v":
    length = float(input ("Enter the length of the rectangle: "))
    width = float(input ("Enter the width of the rectangle: "))
    height = float(input ("Enter the height of the rectangle: "))
    print("Volume =", volume(length, width, height))