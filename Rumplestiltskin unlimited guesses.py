#Correct name
correct_first_name = "George"
#Asks the user for its name if it is correct they are allowed in if correct they try agian
while True:
    user_name = input("What is your first name? ")
    if user_name == correct_first_name:
        print("Welcome to the program")
        break
    else:
        print("Try again")
