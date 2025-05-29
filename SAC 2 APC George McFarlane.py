# ask for number of students in class
num_students = int(input("Enter the total number of students in this class: "))

# ask for number of periods (only between 1 and 5)
while True:
    num_periods = int(input("Enter total number of periods of this class held in the week (between 1 and 5): "))
    if 1 <= num_periods <= 5:
        break
    print("Please enter a number between 1 and 5")

# database to hold student attendance
students = {}

#getting attendance
for i in range(num_students):
    name = input(f"Enter name for student {i + 1}: ")
    attendance = []
    for p in range(num_periods):
        while True:
            status = input(f"Enter attendance for {name} (P/A) for period {p + 1}: ").upper()
            if status in ["P", "A"]:
                attendance.append(status)
                break
            else:
                print("Enter 'A' for absent or 'P' for present. ")
        students[name] = attendance
#Print the final report of attendance and give a warning if attendance lower than 75%

print("\n-----Attendance Report-----")
with open("attendance_records.txt", 'w') as file:
    for name, records in students.items():
        present_count = records.count("P")
        percentage = (present_count / num_periods) * 100
        report = f"{name}: {present_count} periods present ({percentage:.0f}%)"
        if percentage < 75:
            report += "-Warning: Low Attendance-"
        print(report)
        file.write(f"{name}: {' '.join(records)}\n")
        print("\n Data written to file")
            
            