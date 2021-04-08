# Rock, Paper, and Scissors variables
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
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
---.__(___)
'''

# importing the random library and putting the above variables into a list
import random
game = [rock, paper, scissors]

# Prompting the user to enter 0, 1, or 2 for the game
player = input("Play a game of Rock, Paper, Scissors. For Rock type 0, Paper 1, or 2 for Scissors: ")

# Makes the computer player randomly select rock, paper, or scissors
computer = random.choice(game)

# If else statement to determine what happens when the computer and the player decides to play rock, paper, or scissors
# Also, displays the results of the game
if player == "0" and computer == rock:
  print(f"You chose {rock}\n The computer chooses {rock}\n")
  print("It's a tie")
elif player == "0" and computer == paper:
  print(f"You chose{rock}\n The computer chooses {paper}\n")
  print("You lose")
elif player == "0" and computer == scissors:
  print(f"You chose{rock}\n The computer chooses {scissors}\n")
  print("You win")

if player == "1" and computer == paper:
  print(f"You chose{paper}\n The computer chooses {paper}\n")
  print("It's a tie")
elif player == "1" and computer == scissors:
  print(f"You chose{paper}\n The computer chooses {scissors}\n")
  print("You lose")
elif player == "1" and computer == rock:
  print(f"You chose{paper}\n The computer chooses {rock}\n")
  print("You win")

if player == "2" and computer == scissors:
  print(f"You chose{scissors}\n The computer chooses {scissors}\n")
  print("It's a tie")
elif player == "2" and computer == rock:
  print(f"You chose{scissors}\n The computer chooses {rock}\n")
  print("You lose")
elif player == "2" and computer == paper:
  print(f"You chose{scissors}\n The computer chooses {paper}\n")
  print("You win")
