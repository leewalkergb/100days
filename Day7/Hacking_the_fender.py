#----------------------------------------------------------------------------------
# This is the code for the Hacking the Fender project on the Analyze data with Python
# pathway on Codeacademy
#
# Date: 03/07/22
#----------------------------------------------------------------------------------

'''TODO: 
    - Update the Passwords.txt file to scramble the secret data
    - Add the signature of Slash Null
'''

#-----------------------------------------------------------------------------------------------------------------------------
import csv
import json

compromised_users = []

#-----------------------------------------------------------------------------------------------------------------------------

# Open the csv file and extract the user data to the compromised users list
with open('Day7/passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)

#Iterate through the csv and perform an operation
    for rows in password_csv:
        # Temp store the row
        password_row = rows

        # Put all the users in the compromised users list
        compromised_users.append(rows['Username'])

#-----------------------------------------------------------------------------------------------------------------------------

# Open the open a compromised users file and add the data acquired 
# Assume maybe 'a' could've been used here as well but seeing as we use a for loop they all get added anyway
with open('Day7/compromised_users.txt', 'w') as compromised_user_file:
    for users in compromised_users:
        # Escape character so they are nicely formatted
        compromised_user_file.write(users + "\n")

#-----------------------------------------------------------------------------------------------------------------------------

# We now need to create a json file
with open('Day7/boss_message_json','w') as boss_message:

    boss_message_dict = {
        'recipent': 'The Boss',
        'message': 'Mission Success'
    }

    #Write to the JSON file
    json.dump(boss_message_dict, boss_message)

#-----------------------------------------------------------------------------------------------------------------------------

# 'Hack' the passwords file
with open('Day7/new_passwords.csv','w') as new_passwords_obj:
    slash_null_string = ''' 
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)     

 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 

        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/ 

 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/

'''
    new_passwords_obj.write(slash_null_string)