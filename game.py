# Project Hangman Game

import random

#List of words
words = ["Adventure", "Spaceship", "Lantern", "Monster", "Knowledge", "Microwave", "Watermelon", "Journey", "Tornado", "Blanket", "Octopus"]

#Choose a random word
secret_word = random.choice(words).lower()
guessed_word = ["_"] * len(secret_word)
attempts = 6
guessed_letters = []

#Introduction
print("Welcome to the Hangman Game!")
print("Guess the secret word letter by letter")
print(f"The word has {len(secret_word)} letters.")
print("You have 6 chances, Good Luck! \n")

while attempts > 0:
    #Display current progress
    print("Word: "," ".join(guessed_word))
    print(f"Guessed Letters: {','.join(guessed_letters)}")
    print(f"Remaining attempts: {attempts}")

#User Input
    guess = input("Guess a letter: ").lower()

#Input Validation
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Please enter a single letter.\n")
        continue

#Check if the letter is already check
    if guess in guessed_letters:
        print("You already guessed that letter! Try Again.\n")
        continue

#Add the guessed letters to the list
    guessed_letters.append(guess)

#Check if the guessed letters is in the secret letter
    if guess in secret_word:
        print(f"Good Job! '{guess}' is in the words.\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess

    else:
        print("Oops! You guessed the wrong word.")
        attempts -= 1

#Check if the user has guessed the word
    if "_" not in guessed_word:
        print("Congratulations! You guessed the correct word.")
        print("".join(guessed_word))
        break

#If the user runs out of attempts
if attempts == 0:
    print("Game Over! You runs out of the attempts.")
    print(f"The correct word was: {secret_word}")


      