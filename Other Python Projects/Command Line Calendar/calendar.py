"""
This calendar program allows the user to view the calendar and add, update, or delete events.

I started it based off of codecademy's instructions, then added my own functionality and made it more robust:
- Update robustness (if invalid date is inputted)
- Delete robustness (if invalid event is inputted)

Future additions:
- Date format robustness
    - if input is not in ##/##/#### format
    - if month or day do not make sense
- Can implement exception handling instead of using if and else statements
- Create more functions to reduce code duplication (checking calendar length, prompting try again, etc.)
"""

#structures
from time import sleep, strftime
calendar = {}

def welcome():
  username = input("Please enter your username: ")
  print("Welcome to your calendar, " + username + "!")
  print("Opening calendar...")
  sleep(1)
  print("Today is: " + strftime("%A %B %d, %Y"))
  print("It is " + strftime("%H : %M : %S") + " right now.")
  sleep(1)
  print("What would you like to do?")

def print_calendar():
  if len(calendar.keys()) == 0:
    print("Your calendar is empty.")
  else:
    print(calendar)
  
def start_calendar():
  welcome()
  start = True
  def exit():
    print("Exiting...")
    print("Goodbye, see you next time.")
    start = False
  while start:
    user_choice = input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      print_calendar()
    elif user_choice == "U":
      if len(calendar.keys()) == 0:
        print("Your calendar is empty!")
      else:
        date = input("What date? ")
        if date not in calendar.keys():
          print("No events exist for this date.")
        else:
          update = input("Enter the update: ")
          calendar[date] = (update)
          print("Update success.")
          print_calendar()
    elif user_choice == "A":
      event = input("Enter event: ")
      date = input("Enter date (MM/DD/YYYY): ")
      if (len(date) != 10) or int(date[6:]) < int(strftime("%Y")):
        print("You've entered an invalid date.")
        if (int(date[6:]) < int(strftime("%Y"))):
          print("Date must be in current or future years.")
        try_again = input("Try again? Y for Yes, anything else for No: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          exit()
      else:
        calendar[date] = event 
        print("Event successfully added to calendar.")
        print_calendar()
    elif user_choice == "D":
      if len(calendar.keys()) == 0:
        print("Your calendar is empty!")
      else:
        event = input("What event? ")
        if event in calendar.values():
          for date in calendar.keys():
            if event == calendar[date]:
                del calendar[date]
                print("Succesfully deleted the event.")
                print_calendar()
                break
        else:
          print("Invalid event specified, no event found with given name.")
    elif user_choice == "X":
      exit()
    else:
      print("Invalid command.")
      try_again = input("Try again? Y for Yes, N for No: ")
      try_again = try_again.upper()
      if try_again == "Y":
        continue
      elif try_again == "N":
        exit()
      else:
        print("Invalid command again.")
        exit()
      
start_calendar()