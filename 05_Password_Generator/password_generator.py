import string
import random

characters = string.ascii_letters + string.digits + string.punctuation

random.choice(characters)
long = int(input("Enter the length of the password: ")) 
password = []
for item in range(long):
    password.append(random.choice(characters))

for item in password:
    print(item, end="")