#Ask the user how happy they are?
happy = float(input("How happy are you on a scale of 1-10? "))
#Print different messages based on how happy they are from a scale of 1 to 10
if happy <= 3:
    print("That's not good. Try going for a walk to cheer yourself up")
elif 4 <= happy <= 7:
    print("That's not too bad. Keep doing what you love!")
elif 8 <= happy <= 10:
    print("That's awesome! Try to make someone else's day better too")
else:
    print("Hmm, that number is out of range. Please enter a number between 1 and 10.")
