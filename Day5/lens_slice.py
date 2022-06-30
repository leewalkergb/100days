#----------------------------------------------------------------------------------
# This is the code for the Len's Slice project on the Analyze data with Python
# pathway on Codeacademy
#
# Date: 30/06/22
#----------------------------------------------------------------------------------

#Create the toppings and price list
from numpy import append

#----------------------------------------------------------------------------------
# Global Variables
#----------------------------------------------------------------------------------

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
# Create a 2D list from our lists
pizza_and_prices=[]

#Count the number of occurences of 2 in the price list
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Find how many toppings are in the toppings list and print how many pizzas we sell
num_pizzas = len(toppings)
print("We sell", num_pizzas, "different kinds of pizzas")

# Create a 2D list from our lists
pizza_and_prices=[]

# It said to create this manually but I thought I'd give it a go in a loop as this will be a common thing to do
for i in range(len(toppings)):
    pizza_and_prices.append([prices[i],toppings[i]])


print(pizza_and_prices)

# Put the new list in price order, note
pizza_and_prices.sort()
print(pizza_and_prices)

#Cheapest pizza is
cheapest_pizza = pizza_and_prices[0]

# Priciest pizza is
priciest_pizza = pizza_and_prices[-1]

# That was the last slice of that pizza so remove from the list
pizza_and_prices.pop()

# Add pepper pizza to the list in the right place - Price = 2.5
pizza_and_prices.insert(4,[2.5, "peppers"])
print(pizza_and_prices)

#List the three cheapest pizzas
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)