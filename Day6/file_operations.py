#------------------------------------------------------------------------
# Working with files
#------------------------------------------------------------------------
import csv

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
with open('Day6\books.csv') as books_csv:
# This file has an @ delimiter so we need to pass that to the DictReader() method
  books_reader = csv.DictReader(books_csv, delimiter='@')
  
  # Make a books list
  isbn_list = []
  for rows in books_reader:
    # We need to extract the ISBN value from the rows and add it to our ISBN list
    isbn_list.append(rows['ISBN'])

print(isbn_list)
