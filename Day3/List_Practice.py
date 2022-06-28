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
