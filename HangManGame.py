# import packages 
import random 

# Given sentence
sentence = 'King eats mangos apple watermelon'

#split the sentence
words = sentence.split()
words = [word.lower() for word in words]

#Get the random word - Generated from the system
word = random.choice(words)

# Variable to keep track of the guessed letters 
guess_letter = ['_' for i in word]
guess_letter_count = guess_letter.count('_')

# Count of the word
count = len(word) + 2

#for index, letter in enumerate(word):
while count > 0:
    # printing the guess letter in the blank 
    print(' '.join(guess_letter))
    
    # Getting the guess from the user
    guess = input("\nGuess letter: ").strip().lower()
    
    #If the user guesses the word
    if '_' not in guess_letter:
        print(f"You guessed the word correctly: '{word}'")
        break
    
    if guess in word:
        for index, letter in enumerate(word):
            if guess == letter: 
                guess_letter[index]=guess
        print(f"Guess is correct! '{guess}' is in the word.")
    else:
        print(f"Guess is wrong! '{guess}' is not in the word.")

    count -= 1

#If user still hasn't guessed word 
if '_' in guess_letter:
    print(f"You've run out of guesses! The word was: '{word}'")
        





