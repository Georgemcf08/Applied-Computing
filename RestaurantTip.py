#ask for the bill total
bill_total = float(input("Enter the bill amount: $"))
#Ask for the number of people splitting the bill
num_people = float(input("How many people are splitting the bill: "))
#Ask for the desired tip
tip_percent = float(input("What is the desired tip percentage (e.g 10 for 10%): "))
#ask how long the taxi ride is in miles
taxi_distance = float(input("Enter the taxi distance in miles: "))
#Find out the bill total
total_with_tip = bill_total * (1 + tip_percent/100)
#Find out the cost of the taxi per mile
taxi_cost = taxi_distance * 0.45
#Find the grand total
grand_total = total_with_tip + taxi_cost
#Find the cost per person
per_person = total_with_tip/num_people
#Print a heading
print("\n--- Summary ---")
#Print taxi cost
print(f"Taxi cost: ${taxi_cost:.2f}")
#print grand total
print(f"Grand total: ${grand_total:.2f}")
#print the cost for each person
print(f"Each person should pay: ${per_person:.2f}")