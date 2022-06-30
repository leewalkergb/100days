# Day 5

Added to Github?: Yes
Completion date: 30/06/2022
Language: Python

# Today’s Focus

- Complete the list module

---

# Notes

- Today we are looking at the remaining list methods.
- The len() method is pretty straight forward.

When slicing a list we need to remember the syntax is:

```python
listname[start:end]
```

<aside>
💡 Remember that the end index in the above example is NOT INCLUSIVE

</aside>

```python
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
beginning = suitcase[0:4]

# beginning = ["shirt", "shirt", "pants", "pants"]
```

The syntax for slicing is very flexible.

If we wanted to take the first n elements we can do the following

```python
listname[:3]

#! Remember the last index is non inclusive so this would give us indecies 0,1,2
```

---

The .count() methods lets us count the number of occurances of something within a list

```python
# This returns how many "i" are in a list
listname.count("i")

# It even works with 2D lists
listname.count([100,200])
```

.sort() allows us to sort a list into alphabetical or numerical order

```python
# This sorts the list
listname.sort()

# It even works with in reverse
listname.sort(reverse=True)
```

When using sort it does not return a value so it doesn't need to be assigned to a variable lists get effected directly so if you try to assign it to a new variable then it will return None

If we want to sort a list without permanently altering it we can use sorted() as it will generate a new list

---

<aside>
💡 Remember when using pop the syntax is as follows:

</aside>

```python
removed_item = inventory.pop(4)

#where 4 is the element index!
```

---

<aside>
💡 Inserting in a specific index of a list can be tricky

</aside>

```python
# add new item in element 11
inventory.insert(10,"19th Century Bed Frame")
```

---

Completed the lessons and quiz.

---

**Len’s Slice**

Made a new file for the project.

Interesting note when sorting a 2D list it sorts by the first element in each sublist.

```python
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
```

Finished here for today!

---

## Useful Information

- Recognised the usefulness of the callout markdown command
- In my code I used a for loop to combine the lists but zip seems to do the same. I couldn’t get it to work so I need to look this up in the future

## Reflections

- Some of the list methods have their syntax a little different than I expected so it’ll be useful to keep using and refreshing my memory with them regularly
- Python and pandas uses a lot of list manipulation so I better get used to using them
- Not quite sure the differences of list vs dictionary but I’m sure it is on the track

## Tomorrow’s Focus

- Finish the introduction to python section of the Analyze data with python path on codeacademy
    - List comprhensions
    - Lambda functions
    - Files