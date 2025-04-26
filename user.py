import random
print("guess the number between 1 to 100!")
#generate random number
number = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess number:"))
    if guess < number:
        print("too low Number!")

    elif guess > number:
        print("too high Number!")

    else:
        print("congratulations You Got it Right!")
        break

    
