#Step 1
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

random_numberr = random.randrange(0,3)
print(random_numberr)
chosen_name = word_list[random_numberr]
print(chosen_name)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("guess a letter")

lower = guess.lower()
print(lower)


#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


if lower in chosen_name:
    print ("Yes!")
else:
    print("No")