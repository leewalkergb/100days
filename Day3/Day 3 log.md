# Day 3

Added to Github?: Yes
Completion date: 28/06/2022
Language: Git, Python

# Today’s Focus

- Have a go at some of the hackerrank prep tests
- Continue with the git hub path on codeacademy
- Refresh python knowledge on codeacademy before continuing on the data analysis path

# Notes

Hacker rank is quite interesting, the problems are a bit arbitrary but it gives you a good gauge as to where you are at. I used to do project Euler problems so maybe as I go throughout the the 100 days I’ll also see how far I can get on hacker rank.

What I have noticed is that I need to practice and develop my programmatic thinking skills. Maybe even do some work on algorithms and data structures but I will see.

Continued todays log with the Poem Fiasco task.

```bash
#You can checkout directly by filename
git checkout -- filename
```

I finished the poem fiasco and decided to turn my attention to the data analysis pathway for python.

---

### Python Lists

I’m developing in visual studio code with the better commenting addon:

![Untitled](Day%203%20a3ec206b728f4c45b95b6763e6e1c819/Untitled.png)

General note:

```python
# For got that a multiline comment uses 

'''
See
This
Is 
Multiline
'''
```

- A list is a data structure in python that allows us to work with a set of data in sequential order

```python
# The syntax for a list is [,,,]
heights = [61, 70, 67, 64]
```

- A list can contain more than just numbers

```python
sam_height_and_testscore = ["Sam", 67, 85.5, True]

#Lists can also be empty
empty_list = []
```

- Lists have a number of associated methods

```python
append_example = ['This', 'Is', 'an', 'example']
append_example.append('list)
```

- Note that .append always adds to the end of the list
- When we want to add multiple items we can use the + operator but they must be another list

```python
items_sold = ["Cake", "hotdog"]
items_sold_new = items_sold + ["biscuit", "Fruit"]
```

We can also access list elements directly. In python things are indexed from 0

```python
append_example = ['This', 'Is', 'an', 'example']
append_example[3] = 'example'
```

We can access list elements directly  to modify them

```python
garden = ["Tomatoes", "Green Beans", "Cauliflower", "Grapes"]
garden[2] = "Strawberries"
 
print(garden)

# Output ["Tomatoes", "Green Beans", "Strawberries", "Grapes"]
```

Lists also have a method called remove

```python
shopping_list.remove()
```

We can remove any item from a list here if we know what the items in the list are.

If there are duplicates it will remove the first one. If there are 3 of the same it will be reduced to two of the same for example.

---

I was getting tired so I decided to finish there for tonight

## Useful Information

- Stackoverflow of answer on how to make a multiline comment

[How do I create multiline comments in Python?](https://stackoverflow.com/questions/7696924/how-do-i-create-multiline-comments-in-python)

## Reflections

- I spent too much time today messing around with notion templates and things which detracted from my coding challenge.
- I should mark the time I started working so I can see how many hours I am actually doing.
- It might be easier to make all my notes in VS Code when I am writing in python, that way I can just copy paste it into a notion code block after the fact to be more efficient.

## Tomorrow’s Focus

- Complete the list section on the skill path and move on to list comprehensions.
    - My feeling is that mastering lists will be important