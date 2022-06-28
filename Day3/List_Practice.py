#-----------------------------------------------------------------
# Python Lists
# Date: 28/06/22
#-----------------------------------------------------------------

heights = [61, 70, 67, 64]

# Note lists can mix datatypes
ints_and_strings = [1, 2, 3, "four", "five"]

mixed_list_common = ["Mia", 27, False, 0.5]
sam_height_and_testscore = ["Sam", 67, 85.5, True]

# Lists can also be empty
my_empty_list = []

#Lists also have methods
append_example = ["This", "is", "an", "Example"]
append_example.append("list")

print(append_example)

#-----------------------------------------------------------------
#This is practice with the .append method
#-----------------------------------------------------------------

orders = ["daisies", "periwinkle"]
print(orders)

orders.append("tulips")
orders.append("roses")

print(orders)

orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]
new_orders = ["lilac","iris"]

orders_combined = orders+new_orders

print(orders_combined)

#-----------------------------------------------------------------
#This is practice accessing list elements
#-----------------------------------------------------------------

employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

#To access the fourth employee
employee_4 = employees[3]
print(employee_4)

#we can select the last element of a list using -1
shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

#shopping_list[-1] is cereal and is equal to shopping_list[5]
print(shopping_list[-1])
print(shopping_list[5])

#This works for the whole list e.g. shopping_list[-5] will be butter
print(shopping_list[-5])

last_element = shopping_list[-1]
index5_element = shopping_list[5]

print(index5_element)
print(last_element)

#-----------------------------------------------------------------
#This is practice modifying list elements
garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]

garden_waitlist[1] = "Calla"
print(garden_waitlist)

garden_waitlist[-1] = "Alex"
print(garden_waitlist)

#-----------------------------------------------------------------
#This is practice using the .remove() method on list elements
order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
print(order_list)

#remove flatbread
order_list.remove("Flatbread")
print(order_list)

new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)

#remove the duplicate
new_store_order_list.remove("Mango")
print(new_store_order_list)

#-----------------------------------------------------------------
# Decided to complete the lists section
#-----------------------------------------------------------------

#We can increase the dimension of a list by putting a list within a list
heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64], ["Vik",68]]

ages = [["Aaron",15], ["Dhruti",16]]

#We can also acess specific indices in a 2d list usint list_name[][]
class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]

print(class_name_test)

# We want to select sam's score
sams_score = class_name_test[2][1] 
#If we were to put [2][0] it would return just the name
print(sams_score)

#We want to select ellie's score using negative indices
ellies_score = class_name_test[-1][-1]
print(ellies_score)

#-----------------------------------------------------------------
#Modifying 2D lists
#-----------------------------------------------------------------
incoming_class = [["Kenny","American",9], ["Tanya","Russian",9], ["Madison","Indian",7]]

print(incoming_class)

#We need to update Madisons grade
incoming_class[2][2] = 8
print(incoming_class)

#changing kenny's namme using negative indices
incoming_class[-3][-3] = "Ken"
print(incoming_class)

#-----------------------------------------------------------------
#Review
#-----------------------------------------------------------------
#Create the 1d list
first_names = ["Ainsley","Ben","Chani","Depak"]

# Create preferred_size list
preferred_size = ["Small", "Large", "Medium"]

#Append the preferred_size list
preferred_size.append("Medium")
print(preferred_size)

#Make a 2D list
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)

# Alter chani's entry
customer_data[2][2] = False

#This was tricky, we use the 'row' index and then remove the element of interest
customer_data[1].remove(False)

#Create final customer list using concatenation
customer_data_final = customer_data +[["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)

#-----------------------------------------------------------------
# List Cheatsheet: https://www.codecademy.com/learn/paths/analyze-data-with-python/tracks/ida-2-introduction-to-python/modules/ida-2-3-python-lists/cheatsheet
#-----------------------------------------------------------------