import random

# ASCII Art for each choice
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.(___)
'''

# Store options and their corresponding ASCII art
options = ['rock', 'paper', 'scissors']
art = [rock, paper, scissors]

# Get user's choice
user_choice = int(input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors:\n"))

# Validate input
if user_choice < 1 or user_choice > 3:
    print("Invalid choice! You lose.")
else:
    # Adjust index (since list indices start at 0)
    user_choice_name = options[user_choice - 1]
    computer_choice = random.choice(options)

    # Display choices
    print(f"\nYou chose {user_choice_name}:\n{art[user_choice - 1]}")
    print(f"Computer chose {computer_choice}:\n{art[options.index(computer_choice)]}")

    # Determine the result
    if user_choice_name == computer_choice:
        print("It's a draw! 🤝")
    elif (user_choice_name == 'rock' and computer_choice == 'scissors') \
        or (user_choice_name == 'paper' and computer_choice == 'rock') \
        or (user_choice_name == 'scissors' and computer_choice == 'paper'):
        print("You win! 🎉")
    else:
        print("You lose! 💻 wins.")
