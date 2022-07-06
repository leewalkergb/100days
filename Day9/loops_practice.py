#------------------------------------------------------------------------
# Loops
#------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------
# For Loops
#--------------------------------------------------------------------------------------------------------------------------

# The general format of a for loop is as follows:
# for <temporary variable> in <collection>:
#   <action>

for step in range(0,10):
    print("This is step ", step)

# The above loop could even be condensed to one line but the more line version is easier to read
for step in range(0,10): print("This is step ", step)

#--------------------------------------------------------------------------------------------------------------------------

# Basic looping through list items examples
board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]
sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
  print(game)

for sport in sport_games:
  print(sport)

#--------------------------------------------------------------------------------------------------------------------------
# note that when using range in a for loop you don't need the range(a,b) format
promise = "I will finish the python loops module!"

for message in range(5):
    print(promise)

#--------------------------------------------------------------------------------------------------------------------------
# While Loops
#--------------------------------------------------------------------------------------------------------------------------

# The general format of a while loop is as follows:
# while <conditional statement>:
#   <action>

count = 0
while count <= 3:
  # Loop Body
  print(count)
  count += 1

# We can also single line while loops:
# count = 0
# while count <= 3: print(count); count += 1

# Basic example
countdown = 10
while countdown >= 0:
  print(countdown)
  countdown -= 1
print("We have liftoff!")

#--------------------------------------------------------------------------------------------------------------------------
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics)
index = 0

while index < length:
  print("I am learning about", str(python_topics[index]))
  index += 1

#--------------------------------------------------------------------------------------------------------------------------
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

# Example using a break condition
for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break
#--------------------------------------------------------------------------------------------------------------------------
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
  if i < 21:
    continue
  print(i)

#--------------------------------------------------------------------------------------------------------------------------
# Nested Loop
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for location in sales_data:
  for sales in location:
    # looping through the sublists and finding the sum
    scoops_sold += sales
print(scoops_sold)

#--------------------------------------------------------------------------------------------------------------------------
# List comprehension examples
#!Remember list comprehensions take the form new_list = [<expression> for <element> in <collection>]
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [score+10 for score in grades]

print(scaled_grades)

#Note conditional loops can be tricky structure in list comprehensions
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [tall for tall in heights if tall > 161]

print(can_ride_coaster)