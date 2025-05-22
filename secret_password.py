#Correct password
secret_password = "frogbridge"
attempts = 3
#ask the user for the password if correct they are allowed in if not they get 2 more trys
while attempts > 0:
    user_input = input("Enter the secret password: ") 
    if user_input == secret_password:
        print("Access granted! Welcome to the program.")
        break
    else:
        attempts -= 1
        print("Incorrect password.", attempts, "attempt(s) left.")

if attempts == 0:
    print("Access denied, too many failed attempts.")
