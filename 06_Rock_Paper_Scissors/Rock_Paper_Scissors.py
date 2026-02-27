from random import choice

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter your choice (rock, paper, or scissors) or 'quit' to exit: ").lower()
    
    if user_choice == "quit":
        print("Goodbye!")
        break
    
    if user_choice not in choices:
        print("Invalid input. Please enter rock, paper, or scissors.")
        continue
    
    computer_choice = choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")