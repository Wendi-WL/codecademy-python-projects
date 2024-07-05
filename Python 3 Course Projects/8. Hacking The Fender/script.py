import os
import csv
import json

# Reading In The Passwords

compromised_users = []

# I used os to locate this script's directory and access the passwords csv file in it, after moving it off of codecademy.
def full_path(relative_path):
  script_dir = os.path.dirname(__file__)
  return os.path.join(script_dir, relative_path)

with open(full_path("passwords.csv"), "r") as password_file:
  password_csv = csv.DictReader(password_file)
  for row in password_csv:
    compromised_users.append(row['Username'])

# test
with open(full_path("passwords.csv")) as pw:
  passwords = pw.read()
print(passwords)

with open(full_path("compromised_users.txt"), "w") as compromised_users_file: 
  for user in compromised_users:
    compromised_users_file.write(user + "\n")

# test
with open(full_path("compromised_users.txt")) as cu:
  users = cu.read()
print(users)

# Notifying the Boss

with open(full_path("boss_message.json"), "w") as boss_message:
  boss_message_dict = {
    "recipient": "The Boss", 
    "message": "Mission Success"
  }
  json.dump(boss_message_dict, boss_message)

# test
with open(full_path("boss_message.json")) as bm:
  message = bm.read()
print(message)

# Scrambling the Password
with open(full_path("new_passwords.csv"), "w") as new_passwords_obj:
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
with open(full_path("new_passwords.csv")) as np:
  new_passwords = np.read()
print(new_passwords)