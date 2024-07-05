'''
This program is a game where the user tries to guess the sum of a pair of dice. The user wins if they guess correctly. Otherwise, the computer wins.
'''

from random import randint
from time import sleep

def get_user_guess():
  guess = int(input("Guess a number: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print("The maximum possible value is %d" % max_val)
  guess = get_user_guess()
  if guess > max_val:
    print("Your guess is invalid. The max possible value is %d" % max_val)
  else:
    print("Rolling...")
    sleep(2)
    print("%d" % (first_roll))
    sleep(1)
    print("%d" % (second_roll))
    sleep(1)
    total_roll = first_roll + second_roll
    print("The total roll is: %d" % (total_roll))
    print("Result...")
    sleep(1)
    if guess == total_roll:
      print("Congrats! You won and beat the computer!")
    else:
      print("Sorry, you lost this time. Try again if you wish.")
    
roll_dice(6)