#------------------------------------------------------------------------
# Working with files
#------------------------------------------------------------------------
import csv
import json

#-----------------------------------------------------------------------------------------------------------------------------
# Reading Files
#-----------------------------------------------------------------------------------------------------------------------------

# We can read files using the following syntax

#Tell it what file to open and as what object
# DO NOT FORGET THE PATH IF YOU ARE USING A FOLDER STRUCTURE
with open('Day6\practice.txt') as cool_doc:
# Read the contents and save them to the variable cool_contents
    cool_contents = cool_doc.read() 

# Print out the file contents
print(cool_contents)

#-----------------------------------------------------------------------------------------------------------------------------
# We can also iterate through the lines of a file using a for statement and .read()
with open('Day6\practice.txt') as lines_doc:
  # Look at each line
  for line in lines_doc.readlines():
    # Print lines one by one
    print(line)

# If we want to read only one line at a time we can use .readline()
with open('Day6\practice.txt') as lines_doc:
    first_line = lines_doc.readline()
    print(first_line)

#-----------------------------------------------------------------------------------------------------------------------------
# Writing to Files
#-----------------------------------------------------------------------------------------------------------------------------

# .write() WILL OVERWRITE ALL CONTENTS OF THE FILE!!!!
# with open('Day6\practice.txt','w') as lines_doc:
#     lines_doc.write('I have added this line programmatically 1')

# r opens the file in read mode. I assume we must close first? !No we don't with does that
# with open('Day6\practice.txt','r') as lines_doc:
#     updates = lines_doc.read()
# print(updates)

# We can update a file with additional contents using 'a'
with open('Day6\practice.txt','a') as lines_doc:
    lines_doc.write('I have added this line programmatically 1\n')


#-----------------------------------------------------------------------------------------------------------------------------
# CSV FILES
#-----------------------------------------------------------------------------------------------------------------------------

# We can do similar file operations on csv files as we can on text files
# with open('Day6\logger.csv') as log_csv_file:
#     print(log_csv_file.read())

# Printing in the above manner is a bit of a pain to read so we can convert it to a dict
# Using the .DictReader() method of the csv library
with open('Day6\logger.csv') as cool_csv_file:
    cool_csv_dict = csv.DictReader(cool_csv_file)
    for row in cool_csv_dict:
        print(row)

#-----------------------------------------------------------------------------------------------------------------------------
#A Way More Complicated example
#-----------------------------------------------------------------------------------------------------------------------------
# Something weird happens if the file begins with a b and doing Day6\books.csv
with open('Day6\list_of_books.csv') as books_csv:
# This file has an @ delimiter so we need to pass that to the DictReader() method
  books_reader = csv.DictReader(books_csv, delimiter='@')
  
  # Make a books list
  isbn_list = []
  for rows in books_reader:
    # We need to extract the ISBN value from the rows and add it to our ISBN list
    isbn_list.append(rows['ISBN'])

print(isbn_list)

#-----------------------------------------------------------------------------------------------------------------------------
#Writing to a .csv
#-----------------------------------------------------------------------------------------------------------------------------

# Define the data dictionary and the header dictionary
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

# Open the file we are making
#! REMEMBER TO SPECIFY THE PATH
with open('Day6\logger1.csv', 'w') as logger_csv:
    # Set the field names remember we are now WRITING hence .DictWriter()
    log_writer = csv.DictWriter(logger_csv, fieldnames=fields)

    #write the header
    log_writer.writeheader()

    #Add the data to the csv file
    for items in access_log:
        log_writer.writerow(items)

# Just checking if it saved
#! REMEMBER TO SPECIFY THE PATH
with open('Day6\logger1.csv') as logger_csv:
    log_reader = csv.DictReader(logger_csv,delimiter=',')
    for row in log_reader:
        print(row)

#-----------------------------------------------------------------------------------------------------------------------------
# JSON FILES
#-----------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------
#Reading a JSON file
#-----------------------------------------------------------------------------------------------------------------------------

#Open the JSON file
with open('Day6\message.json') as message_json:
  # Notice that this is .load
  message = json.load(message_json)
  # We target the specific key
  print(message['text'])


#-----------------------------------------------------------------------------------------------------------------------------
#Writinga JSON file
#-----------------------------------------------------------------------------------------------------------------------------
#Write to the JSON file

# We can create the file just as we did with the .csv file
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

with open('Day6\data.json', 'w') as data_json:
  # Add the data to the json file notice that it is .dump
  json.dump(data_payload, data_json)