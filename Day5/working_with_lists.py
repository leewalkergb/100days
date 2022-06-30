#------------------------------------------------------------------------
# List operations
#------------------------------------------------------------------------

#Using range to make a consecutive list
#range() makes its own object so we have to cast it to a list list(range())

#create a range 0..8, remember zero index!
number_list = range(9)
print(list(number_list))

#create range 0..7
zero_to_seven = range(8)
print(list(zero_to_seven))

#if we call range with two numbers it doesn't start from zero range(x,y)
#if we add a third value it will increment in steps of that third parameter range(x,y,z)

#between 5 and 15 non incluive in steps of 3
range_five_three = range(5, 15, 3)
#between 0 and 40 non incluive in steps of 5
range_diff_five = range(0,40,5)

# We can find the number of items in a list by using the len() method
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 10)

# Find the length of long_list and save it to a new variable
long_list_len = len(long_list)

#Print the long list len variable
print(long_list_len)

# Find the length of big range and save it to a new variable
big_range_length = len(big_range)
print(big_range_length)

#------------------------------------------------------------------------
#Slicing Lists
#------------------------------------------------------------------------

#If we want to extract a portion of a list we can do so by slicing it
#To do this we can use the following syntax listname[start:end] where start and end are indexes ! REMEMBER END IS NOT INCLUSIVE

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# This should remove books
beginning = suitcase[0:4]
print(beginning)

# Modify beginning so it selects the first two elements of suitcase
beginning = suitcase[0:2]

# Create a new list and select the middle elements
middle = suitcase[2:4]
print(middle)

#------------------------------------------------------------------------
# slicing is really flexible If we wanted to take the first n elements we can do the following listname[:n]

#Capture the last two elements of suitcase
#This means everything from -2
last_two_elements = suitcase[-2:]
print(last_two_elements)

#This means everything up to -3
slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

#------------------------------------------------------------------------
#.count() and Lists
#------------------------------------------------------------------------

#The .count() methods lets us count the number of occurances of something within a list
# It even works with 2D lists

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# using count find how many votes Jake got
jake_votes = votes.count("Jake")
print("Jake got", jake_votes, "votes")

#------------------------------------------------------------------------
#.sort() and Lists
#------------------------------------------------------------------------

#.sort() allows us to sort a list into alphabetical or numerical order
# it even works in reverse .sort(reverse=True)

addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
print(addresses)


names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()

# This will cause problems
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort()

# When using sort it does not return a value so it doesn't need to be assigned to a variable
# lists get effected directly so if you try to assign it to a new variable then it will return None
print(sorted_cities)

#This sorts the list in reverse
cities.sort(reverse=True)
print(cities)

#If we want to sort a list without permanently altering it we can use sorted() as it makes a new list
games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

#make a new sorted list from games
games_sorted = sorted(games)

# Show that they are indeed different and games remains unaffected
print(games)
print(games_sorted)

#------------------------------------------------------------------------
#PUTTING IT ALL TOGETHER
#------------------------------------------------------------------------
inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# How many items are there?
inventory_len = len(inventory)

# Select the first and last element from inventory
first = inventory[0]
last = inventory[-1]

#Select items from inventory from index 2 up to but not including index 6
inventory_2_6 = inventory[2:6]

#select the first 3 items of inventory
first_3 = inventory[:3]

# Find how many "twin bed" entries there are
twin_beds = inventory.count("twin bed")

# remove the 5th element and save it to a variable
removed_item = inventory.pop(4)

# add new item in element 11
inventory.insert(10,"19th Century Bed Frame")

#Sort the inventory
inventory.sort()
print(inventory)

