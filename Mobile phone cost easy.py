#Ask the user how many pictures, texts and data they are going to use in the month
pictures = int(input("How many pictures are you going to take this month? "))
texts = int(input("How many texts are you going to send this month? "))
data = float(input("How much data are you going to use this month? (In MB) "))
#Add the cost for each picture, text and Megabite of data used
cost_picture = pictures * 0.35
cost_texts = texts * 10 
cost_data = data * 0.05
#Add the cost of them all together
total_cost = cost_picture + cost_texts + cost_data
#Print
print(f"${total_cost:.2f}")
#If the total cost is more than $10 print
if total_cost > 10:
    print ("You should be on a data program it would be cheaper")

