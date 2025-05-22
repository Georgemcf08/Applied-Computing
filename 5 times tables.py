#Ask the user for a sentence
sentence = input("Write a sentence: ")
vowel_count = 0
#count the number of vowels in the given sentence
for letter in sentence:
    if letter.lower() in ("a", "e", "i", "o", "u"):
        vowel_count += 1
#print the number of vowels
print("The number of vowels in the sentence is:", vowel_count)
