#Correct name
correct_first_name = "George"
attempts = 3
#While the user has more than 0 attempts run this code,if correct name print Welcome to the program, if incorrect, try agian
while attempts > 0:
    user_name = input("What is your name? ") 
    if user_name == correct_first_name:
        print("Welcome to the program.")
        break
    else:
        attempts -= 1
        print("Incorrect .", attempts, "attempt(s) left.")
#If the user runs out of guesses, they are locked out
if attempts == 0:
    print("Your locked out, too many failed attempts.")

