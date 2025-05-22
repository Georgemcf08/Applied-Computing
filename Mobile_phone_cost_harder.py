#import the math function
import math
#Ask the user how many pictures, texts and megabites of data they are going to use
pictures = int(input("How many pictures are you going to take this month? "))
texts = int(input("How many texts are you going to send this month? "))
data = int(input("How much data are you going to use this month? (In MB) "))
#Add the cost of each
cost_picture = pictures * 0.35
cost_texts = texts * 10 
data_block = math.ceil(data / 500)
cost_data = data_block * 2.5
total_cost = cost_picture + cost_texts + cost_data
#Print and recommed a data plan if more than 10 dollars
print(f"${total_cost:.2f}")
if total_cost > 10:
    print ("You should be on a data program it would be cheaper")


