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