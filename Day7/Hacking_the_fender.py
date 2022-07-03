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

# import the required modules
import csv

compromised_users = []

with open('\Day7\passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)

    for rows in password_csv:
        password_row = rows