#------------------------------------------------------------------------
# List Comprehensions
#------------------------------------------------------------------------
temperatures = [-5, 29, 26, -7, 1, 18, 12, 31]

# A long way of correcting the above list is to do it manually
temp_corrected = [15, 49, 46, 13, 21, 38, 32, 51]
print(temp_corrected)

# Python also allows us to do this programmatically via a list comprehension

# It uses the following format [operation for item in list]
# In this case for every item in the list we add 20 to that item
temp_corrected2 = [temp+20 for temp in temperatures] 
print(temp_corrected2)

# The operations can be more complex i.e. convert from celcius to farenheit
temp_far = [(9.0/5.0)* temp + 32 for temp in temperatures] 
print(temp_far)

#------------------------------------------------------------------------
# List Comprehensions - Codeacademy Challange
#------------------------------------------------------------------------

# Doubling
nums = [4, 8, 15, 16, 23, 42]

#create a new list that doubles every number in nums
double_nums = [number * 2 for number in nums]
print(double_nums)


# Squaring
# Generate a list of numbers between 0..10
nums = range(11)

#Note that the following works the same as [index**2 for index in nums]
squares = [index**2 for index in range(11)]
print(squares)

#-----------------------------------------------------------------------------------------------------------------------------

# Add 10
nums = [4, 8, 15, 16, 23, 42]
add_ten = [num+10 for num in nums]
print(add_ten)

#-----------------------------------------------------------------------------------------------------------------------------

# Concatenate Strings
names = ["Elaine", "George", "Jerry", "Cosmo"]
greetings = ["Hello, "+ name for name in names]

print(greetings)

#-----------------------------------------------------------------------------------------------------------------------------

# Get first character of every element
first_character = [name[0] for name in names]
print(first_character)

#-----------------------------------------------------------------------------------------------------------------------------

# Find length of each element
lengths = [len(name) for name in names]
print(lengths)

#-----------------------------------------------------------------------------------------------------------------------------

booleans = [True, False, True]

#Get the opposite of each element
opposite = [not index for index in booleans]
print(opposite)

#-----------------------------------------------------------------------------------------------------------------------------

#Check if the element is jerry or not
is_Jerry = [name=="Jerry" for name in names]
print(is_Jerry)

nums = [5, -10, 40, 20, 0]


#-----------------------------------------------------------------------------------------------------------------------------

#Check is a number is >2
greater_than_two = [num>2 for num in nums]
print(greater_than_two)

nested_lists = [[4, 8], [15, 16], [23, 42]]

#-----------------------------------------------------------------------------------------------------------------------------

#Find the product of each sublist
product = [num1 * num2 for (num1, num2) in nested_lists]
print(product)

nested_lists = [[4, 8], [16, 15], [23, 42]]

#-----------------------------------------------------------------------------------------------------------------------------

#Check if the first number is greater than the other number in each sub list
greater_than = [item1 > item2 for (item1, item2) in nested_lists]
print(greater_than)

# Using zip
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]

sums = [a1+b1 for (a1,b1) in zip(a,b)]
print(sums)

#-----------------------------------------------------------------------------------------------------------------------------

# Combine capitals and countries using a list comprehension and zip so the new list has the format "Captial, Country"
capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]

locations = [cap+", " + cou for (cap, cou) in zip(capitals,countries)]
print(locations)

#-----------------------------------------------------------------------------------------------------------------------------

names = ["Shilah", "Arya", "Kele"]
ages = [14, 9, 35]

# Create a new list named users that contains the string "Name: name, Age: age"
users = ["Name: "+name+", Age: " + str(age) for (name, age) in zip (names, ages)]
print(users)