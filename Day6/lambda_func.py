#------------------------------------------------------------------------
# Lambda Functions
#------------------------------------------------------------------------

# A lambda function is a one-line shorthand for a function

import random

#------------------------------------------------------------------------
# Using the in keyword
#------------------------------------------------------------------------

# We can check if a string contains a sub string by using in

# Write a function to check if the word provided contains an "a"
contains_a = lambda word: "a" in word

print(contains_a("banana"))
print(contains_a("apple"))
print(contains_a("cherry"))

#------------------------------------------------------------------------
# Using string methods
#------------------------------------------------------------------------
# Create a lambda function named long_string that takes an input str and returns True if the string has over 12 characters in it. Otherwise, return False.

# When using an if statement the format is:
# <WHAT TO RETURN IF STATEMENT IS TRUE> if <IF STATEMENT> else <WHAT TO RETURN IF STATEMENT IS FALSE>

long_string = lambda str: True if len(str) > 12 else False
print(long_string("short"))
print(long_string("photosynthesis"))

#--------------------------------------------------------------------------------------------------------------------------

# Create a lambda function named ends_in_a that takes an input str and returns True if the last character in the string is an a. Otherwise, return False.

ends_in_a = lambda str: True if str[-1] == "a" else False

print(ends_in_a("data"))
print(ends_in_a("aardvark"))

#Create a lambda function named double_or_zero that takes an integer named num. If num is greater than 10, return double num. Otherwise, return 0.

double_or_zero = lambda num: num*2 if num>10 else 0
print(double_or_zero(15))
print(double_or_zero(5))

#Create a lambda function named even_or_odd that takes an integer named num. If num is even, return "even". If num is odd, return "odd".

even_or_odd = lambda num: "odd" if num%2 > 0 else "even"

print(even_or_odd(10))
print(even_or_odd(5))


# Create a lambda function named multiple_of_three that takes an integer named num. If num is a multiple of three, return "multiple of three". Otherwise, return "not a multiple".

multiple_of_three = lambda num: "not a multiple" if num%3 > 0 else "multiple of three"

print(multiple_of_three(9))
print(multiple_of_three(10))

# Create a lambda function named rate_movie that takes a number named rating. If rating is greater than 8.5, return "I liked this movie". Otherwise return "This movie was not very good".

rate_movie = lambda rating: "I liked this movie" if rating > 8.5 else "This movie was not very good"

print(rate_movie(9.2))
print(rate_movie(7.2))

#--------------------------------------------------------------------------------------------------------------------------
# Create a lambda function named add_random that takes an input named num. The function should return num plus a random integer number between 1 and 10 (inclusive).

# don't forget to import random
# random.randint(a,b) returns a random int between a and b inclusive
add_random = lambda num: num + random.randint(1, 10)

print(add_random(5))
print(add_random(100))