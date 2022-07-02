# Day 6

Added to Github?: Yes
Completion date: 02/07/2022
Language: Python

# Today’s Focus

- Finish the introduction to python section of the Analyse data with python path on codeacademy
    - [x]  List comprehensions
    - [x]  Lambda functions
    - [x]  Files

# Notes

### List Comprehensions

Sometimes we need to make changes to everything in a list. A list comprehension allows us to perform that operation all at once programmatically

The way comprehensions in python work is by the following format:

```python
# Where list is the list we perform the operation on and operation is what we want to do
[operation for item in list]

# In this case for every item in the list we add 20 to that item
temp_adjusted = [temp+20 for temp in temperatures]
```

You can also use list methods in list comprehensions

```python
# Find length of each element
lengths = [len(name) for name in names]
print(lengths)
```

We can also perform them on lists of lists

```python
original_list = [[1, 2], [3, 4],  [5, 6]]
new_list = [item1 + item2 for (item1, item2) in original_list]

# output in the above case is [3, 7, 11]
```

We can use zip but I find it confusing

```python
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]

sums = [a1+b1 for (a1,b1) in zip(a,b)]
print(sums)

#It can basically take two lists and then 
# perform operations on the corresponding elements of that list
```

Zip is quite nifty once you understand the syntax, but will required lots of practice to keep that syntax in your head.

List comprehensions is now finished.

---

### Using Lambda Functions

A lambda function is a one-line shorthand for a function:

```python
# Normal way to define a function
def myfunction():
	return

#Lambda function syntax
add_two = lambda my_input: my_input + 2
```

Lambda functions can also use conditional statements:

```python
# The format for this is <WHAT TO RETURN IF STATEMENT IS TRUE> if <IF STATEMENT> else <WHAT TO RETURN IF STATEMENT IS FALSE>
check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A...'

```

Lambda functions are really easy to use

<aside>
💡 A nifty trick to see if something is a multiple of a number is to use n%n - If it returns 0 then it is a multiple

</aside>

The random function will return a random int between a and b inclusive:

```python
# random.randint(a,b) returns a random int between a and b inclusive
add_random = lambda num: num + random.randint(1, 10)

print(add_random(5))
print(add_random(100))
```

The lambda function module is now completed!

---

### Working with Files

We have built in functionality to read files

```python
# We can read files using the following syntax

#Tell it what file to open and as what object
# DO NOT FORGET THE PATH IF YOU ARE USING A FOLDER STRUCTURE
with open('Day6\practice.txt') as cool_doc:
# Read the contents and save them to the variable cool_contents
    cool_contents = cool_doc.read() 

# Print out the file contents
print(cool_contents)
```

---

We have built in functionality to write to files

```python

# The 'w' parameter allows us to write to the file 
with open('generated_file.txt', 'w') as gen_file:
  gen_file.write("What an incredible file!")
```

<aside>
💡 .write() WILL OVERWRITE ALL CONTENTS OF THE FILE!!!!

</aside>

---

```python
# We can update a file with additional contents using 'a'
with open('Day6\practice.txt','a') as lines_doc:
    lines_doc.write('I have added this line programmatically 1')
```

<aside>
💡 If you you want to write to a new line you need to use the \n escape character

</aside>

The with keyword invokes what is known as a context manager for the file we are calling open() on. The context manager takes care of opening the file and then closing it again after the block has been executed. With is a more modern way of dealing with files.

So basically if you don’t use the WITH keyword you must manually close the file yourself using the .close() method.

---

### CSV Files

A lot of the same I/O commands that work on text files also work on .csv files

```python
# We can do similar file operations on csv files as we can on text files
with open('Day6\logger.csv') as log_csv_file:
    print(log_csv_file.read())
```

However the formatting of what we read won’t be very pretty.

We can convert the csv contents to something nicer to read using the built in .DictReader() method

```python
# Using the .DictReader() method of the csv library
with open('Day6\logger.csv') as cool_csv_file:
    cool_csv_dict = csv.DictReader(cool_csv_file)
    for row in cool_csv_dict:
        print(row)
```

---

<aside>
💡 REMEMBER NOT ALL .CSV FILES USE A COMMA AS A DELIMITER

</aside>

The good news is we have a built in way of dealing with that by passing it as and argument to the DictReader method:

```python
# Using the .DictReader() method of the csv library
with open('Day6\logger.csv') as cool_csv_file:
    cool_csv_dict = csv.DictReader(cool_csv_file, delimiter=';')
    for row in cool_csv_dict:
        print(row)
```

If we wanted we can make a large list into a .csv file.

To do this we can use similar syntax as to when we write to a new file, but we need to remember that a .csv has two distinct parts: a header and the data

```python
import csv
#define the data dictionary
#define the header dictionary

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
	
```

---

### JSON FILES

json is another cool data file type.

Python has a built in library for interacting with it as well

```python
#import json
```

---

Similar to text files and .csv files we can use the same file methods we have been doing so far

```python
#Open the JSON file
with open('message.json') as message_json:
  # Notice that this is .load
  message = json.load(message_json)
  # We target the specific key
  print(message['text'])
```

---

We can also write to the file

```python
#Write to the JSON file

# We can create the file just as we did with the .csv file
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

with open('Day6\data.json', 'w') as data_json:
  # Add the data to the json file notice that it is .dump
  json.dump(data_payload, data_json)
```

 This is the end of the FILES module

---

This is where I will end today.

## Useful Information

- Zip official documentation

[Built-in Functions - Python 3.10.5 documentation](https://docs.python.org/3/library/functions.html#zip)

- Cheat sheet for files

[Introduction to Python: Files Cheatsheet | Codecademy](https://www.codecademy.com/learn/paths/analyze-data-with-python/tracks/ida-2-introduction-to-python/modules/learn-python3-files/cheatsheet)

- Python docs for I/O operations

[7. Input and Output - Python 3.10.5 documentation](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects)

- Python docs for JSON

[json - JSON encoder and decoder - Python 3.10.5 documentation](https://docs.python.org/3/library/json.html?highlight=json)

- Python docs for CSV

[csv - CSV File Reading and Writing - Python 3.10.5 documentation](https://docs.python.org/3/library/csv.html?highlight=csv#module-csv)

## Reflections

- I was getting an incredibly weird issue in VS code when trying to open a file path if the file begins with a b and doing Day6\books.csv
- Pulling pushing staging and comitting is now becoming second nature.
- I’ve not finished all of the basics of the language which is really good!

## Tomorrow’s Focus

- Complete the files project on the codeacademy website
- Start working on one of the projects so far