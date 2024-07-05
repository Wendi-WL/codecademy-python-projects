"""
This program is a game of rock-paper-scissors between the user and the computer.
"""

from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]
message = {
  "tie" : "Yawn it's a tie!", 
  "won" : "Yay you won!", 
  "lost" : "Aww you lost!" 
}

def decide_winner(user_choice, computer_choice):
  print("Your choice is %s." % (user_choice))
  print("The computer chose %s." % (computer_choice))
  if user_choice == computer_choice:
    print(message["tie"])
  elif user_choice == options[0] and computer_choice == options[2] \
  or user_choice == options[1] and computer_choice == options[0] \
  or user_choice == options[2] and computer_choice == options[1]: # I combined all of the possible win situations into 1 elif statement, using the or operator
    print(message["won"])
  else:
    print(message["lost"])
    
def play_RPS():
  user_choice = input("Enter Rock, Paper, or Scissors: ")
  user_choice = user_choice.upper()
  computer_choice = options[randint(0, 2)]
  decide_winner(user_choice, computer_choice)
  
play_RPS()