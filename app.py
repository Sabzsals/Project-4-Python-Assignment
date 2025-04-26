#Rock paper scissors Game
import random

#Introduction
print("Welcome to the Rock, Papers, Scissors Game!")
print("You will play against the computer, Lets begin!")

#Choices List
choices = ["Rock", "Paper", "Scissor"]

while True:
    user_choice = input("Enter your choices(rock, paper, scissors or 'quit' to stop: ) ").lower()

    if user_choice == 'quit':
        print("Thanks for playing, Good bye!")
        break
    elif user_choice not in choices:
        print("Invalid choice! please choose Rock, Paper or scissor")
        continue

    #Computer generate choices
    computer_choice = random.choice(choices)
    print(f"Computer choose: {computer_choice}")

    #Result
    if user_choice == computer_choice:
        print("It's a tie!")
    elif(user_choice == 'rock' and computer_choice == 'scissor') or \
    (user_choice == 'scissor' and computer_choice == 'paper') or \
    (user_choice == 'paper' and computer_choice == 'rock'):
        print("You Win!")
    else:
        print("Computer Win!")


