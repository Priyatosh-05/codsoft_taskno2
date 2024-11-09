import random
import time
import os

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def print_score(user_score, computer_score):
    print("\n=========================")
    print("   Current Score   ")
    print("=========================")
    print(f"   You: {user_score} | Computer: {computer_score}")
    print("=========================\n")

def play_game():
    os.system('cls')
    user_score = 0
    computer_score = 0

    print("\n**************** Welcome to Rock-Paper-Scissors! ****************\n")
    print("Instructions: Choose an option by entering the number.")
    print("Type '4' to end the game.\n")

    choices = {1: 'rock', 2: 'paper', 3: 'scissors'}

    while True:
        # Display choices
        print("Choose your option:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")

        # Get user choice
        try:
            user_choice_num = int(input("Enter your choice (1-4): "))
            if user_choice_num == 4:
                print("\nThanks for playing!")
                break
            elif user_choice_num not in choices:
                print("Invalid choice. Please choose a number between 1 and 4.\n")
                continue

            user_choice = choices[user_choice_num]

            # Get computer choice
            computer_choice = get_computer_choice()

            # Display choices
            print("\nRock...")
            time.sleep(0.5)
            print("Paper...")
            time.sleep(0.5)
            print("Scissors!")
            time.sleep(0.5)
            print(f"\nYou chose: {user_choice.capitalize()}")
            print(f"Computer chose: {computer_choice.capitalize()}")

            # Determine the winner
            result = determine_winner(user_choice, computer_choice)
            
            # Update and display result
            if result == "tie":
                print("\nIt's a tie! 🤝")
            elif result == "user":
                print("\nYou win this round! 🎉")
                user_score += 1
            else:
                print("\nComputer wins this round! 💻")
                computer_score += 1

            # Display current score
            print_score(user_score, computer_score)

            # Ask to play again
            play_again = input("Do you want to play another round? [Yes(y)/No(n)] : ").strip().lower()
            if play_again != 'y':
                print("\nFinal Score:")
                print_score(user_score, computer_score)
                print("Goodbye! Thanks for playing! 🎮")
                break

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.\n")

# Run the game
play_game()
