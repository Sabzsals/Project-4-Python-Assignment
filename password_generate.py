import random
import string

def generated_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#Users input
length = int(input("Enter the length of your desired password: "))

password = generated_password(length)
print("your desired generated password:", password)
