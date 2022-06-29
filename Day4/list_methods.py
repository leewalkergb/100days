# This file practices the use of list methods

# using .insert(<index><element>)
# This takes two inputs the index and the element
front_display_list = ["Mango", "Filet mignon", "Chocolate milk"]
print(front_display_list)

# Add pineapple to sthe front of this list
front_display_list.insert(0,"Pineapple")
print(front_display_list)

#using .pop(<index>) pop can remove an element at an index
#if you like it as .pop() with no index the last one gets removed
data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

#remove python 3
data_science_topics.pop()
print(data_science_topics)

# remove algorithms
data_science_topics.pop(-2)
print(data_science_topics)

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