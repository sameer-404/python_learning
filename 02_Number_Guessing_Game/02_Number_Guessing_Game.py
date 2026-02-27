import random
number = random.randint(1, 20)  # picks a random number between 1 and 20

guess = int(input("Pick a number between 1 and 20: "))
count = 1
while guess != number:
    if guess < number:
        print("Too low! Try again!")
    else:
        print("Too high! Try again!")
    guess = int(input("Pick a number between 1 and 20: "))
    count += 1
print("Congratulations! You guessed the number!")
print(f"Total count: {count}")