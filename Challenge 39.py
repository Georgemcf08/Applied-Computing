# Add the data to file 
data = [
    "James", 1.82, 73,
    "Peter", 1.80, 78,
    "Jay", 1.76, 70,
    "Beth", 1.53, 65,
    "Mags", 1.50, 66,
    "Joy", 1.34, 62
]

# Write data to file
with open("people.txt", "w") as f:
    for i in range(0, len(data), 3):
        f.write(f"{data[i]},{data[i+1]},{data[i+2]}\n")  # name,height,weight

# Read data from file
people = []
with open("people.txt", "r") as f:
    for line in f:
        name, height, weight = line.strip().split(",")
        people.append((name, float(height), int(weight)))

# Print each person's data
print("\nPeople's data:")
for name, h, w in people:
    print(f"{name}: {h} m, {w} kg")

# Calculate and display averages
total_h = sum(p[1] for p in people)
total_w = sum(p[2] for p in people)
#Then print average height and weight for male and female
print("\nAverage height (all):", round(total_h / len(people), 2), "m")
print("Average weight (all):", round(total_w / len(people), 2), "kg")
