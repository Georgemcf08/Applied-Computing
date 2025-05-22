#Ask the user for 6 numbers and add it to a list
numbers = []
print("Enter 6 numbers: ")
for i in range(6):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
with open("example.txt", "w") as MyFile:
    for num in numbers:
        MyFile.write(str(num) + "\n")
#Read the numbers from the list and display total, average then sort by ascending
with open("example.txt","r") as MyFile:
    numbers = [int(line.strip()) for line in MyFile]

print('\nNumbers in file:',numbers)
print('Total', sum(numbers))
print("Average:", sum(numbers) / len(numbers))
print("Sorted (ascending):", sorted(numbers))
#Ask user to add 4 new numbers to file
print("\nAdd 4 more numbers:")
with open("example.txt","a") as MyFile:
    for i in range(4):
        new_num = int(input(f"Enter new number {i + 1}: "))
        MyFile.write(str(new_num) + "\n")
        
print("New numbers were added to the file.")

