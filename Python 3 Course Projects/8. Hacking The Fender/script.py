import csv
import json

# Reading In The Passwords

compromised_users = []

with open("passwords.csv", "r") as password_file:
  password_csv = csv.DictReader(password_file)
  for row in password_csv:
    compromised_users.append(row['Username'])

with open("compromised_users.txt", "w") as compromised_users_file: 
  for user in compromised_users:
    compromised_users_file.write(user + "\n")

# Notifying the Boss

with open("boss_message.json", "w") as boss_message:
  boss_message_dict = {
    "recipient": "The Boss", 
    "message": "Mission Success"
  }
  json.dump(boss_message_dict, boss_message)

# test
with open("boss_message.json") as m:
  message = m.read()
print(message)

# Scrambling the Password
with open("new_passwords.csv", "w") as new_passwords_obj:
  slash_null_sig = """ 
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \\
(___)  \___ \/ (_/\/    \\\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/ """
  new_passwords_obj.write(slash_null_sig)

# test
with open("new_passwords.csv") as new_passwords_obj:
  new = new_passwords_obj.read()
print(new)