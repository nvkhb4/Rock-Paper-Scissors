import random
        
actions = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    user_choice = int(input("Enter a choice: Rock[1], Paper[2], Scissors[3] \n"))
    print("Computer making its choice...")
    
    computer_choice = random.randint(1, 3)
    
    print(f"User's choice: {actions[user_choice-1]} \nComputer's choice: {actions[computer_choice-1]}")
    
    if user_choice == 1 and computer_choice == 3:
        print("Rock beats Scissors. A win for you!")
        user_score += 1
    elif user_choice == 3 and computer_choice == 2:
        print("Scissors beat Paper. A win for you!")
        user_score += 1
    elif user_choice == 2 and computer_choice == 1:
        print("Paper beats Rock. A win for you!")
        user_score += 1
    elif user_choice == computer_choice:
        print("It's a tie! Try again.")
    else:
        print("A win for computer!")
        computer_score += 1

    print(f"User's score: {user_score} \nComputer's score: {computer_score}")
    
    play_again = input("Do you want to play again? (y/n) \n")
    if play_again.lower() != "y":
        break
    
print("And the winner is...")
if user_score > computer_score:
    print("YOU!!")
elif user_score == computer_score:
    print("NO ONE!! It's a tie!")
else:
    print("COMPUTER!!")