#Import turtle drawing tool
import turtle
wn = turtle.Screen()
tom = turtle.Turtle()
#Draw a squre using 4 sides and 90 degrees
def square(length):
    for a in range (4):
        tom.forward(length)
        tom.right(90)
    wn.exitonclick()
#Ask the user for a length to use for the square
size = int(input("Enter the length of the square: "))
square(size)
