#Guess the number - Computer guesses -2


import random

#Introduction
print("Welcome to the Number Guessing Game!")
print("Think of a number between 1 to 100, and I will try to guess!")
print("You can tell me if my guess is too high(H), too low(L) or correct(C).")

#Initial range of guessing
low = 1
high = 100
guesses = 0

while True:
    #Computer guesses the number
    guess = random.randint(low, high)
    guesses +- 1

    #Show the computer's guess
    print(f"My guess is: {guess}")
    user_input = input("Is my guess is too high(H), too low(L) or correct(C)").upper()

    #Check user response
    if user_input == 'H':
        high = guess -1
    elif user_input == 'L':
        low = guess + 1
    elif user_input == 'C':
        print(f"Yay! I guess your number in {guesses} tries")
        break
    print("Invalid input, Please enter H, L or C.")