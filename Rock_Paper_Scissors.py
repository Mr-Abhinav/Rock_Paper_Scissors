#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def get_user_choice():
    while True:
        choice = input("Enter Rock/Paper/Scissor: ").strip().title()
        if choice in ['Rock', 'Paper', 'Scissor']:
            return choice
        print("Please enter a valid choice (Rock/Paper/Scissor)")

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif (player_choice == 'Rock' and computer_choice == 'Scissor') or \
         (player_choice == 'Scissor' and computer_choice == 'Paper') or \
         (player_choice == 'Paper' and computer_choice == 'Rock'):
        return "Player"
    else:
        return "Computer"

def main():
    options = ['Rock', 'Paper', 'Scissor']
    name = input("Enter your name: ").strip().title()
    computer_score = 0
    player_score = 0

    print(f"Welcome {name}")

    for round_number in range(1, 6):
        print(f"\n----- Round {round_number} -----")
        computer_choice = random.choice(options)
        player_choice = get_user_choice()

        print(f"Computer choice: {computer_choice}")
        print(f"{name} choice: {player_choice}")

        winner = determine_winner(player_choice, computer_choice)
        if winner == "Player":
            player_score += 1
            print(f"{name} wins this round!")
        elif winner == "Computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a tie this round!")

        print("\n------ Score Board ------")
        print(f"{name}: {player_score} | Computer: {computer_score}")
        print("-------------------------")

    print("\n===== Game Over =====")
    if player_score == computer_score:
        print("It's a draw!")
    elif player_score > computer_score:
        print(f"Congratulations {name}, you win the game!")
    else:
        print(f"Sorry {name}, the computer wins this time.")

if __name__ == "__main__":
    main()


# In[ ]:




