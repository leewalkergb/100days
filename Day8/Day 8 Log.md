# Day 8

Added to Github?: Yes
Completion date: 05/07/2022
Language: Python

# Today’s Focus

- Close out the outstanding exercises in the Data Scientist Analytics career path so everything is aligned.

# Notes

Started with the medical insurance list estimation project.

It was relatively simple with practice mainly in creating lists and combining them using zip()

---

Moved onto the medical insurance list costs project.

Completed the project it was relatively simple involving some slicing and list operations

```python
# REMINDER
# When concatenating variables into print strings we need to use str()
print("Here is my int " + str(some_int))

# If we use , notation to insert a variable it gets auto converted to str
print("Here is my int ", some_int)
```

---

Started on the loops lesson

The general structure for a for loop is as follows

```python
for <temporary variable> in <collection>:
  <action>

# Example
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
 
for ingredient in ingredients:
  print(ingredient)
```

Another example using range()

```python
# note that when using range in a for loop you don't need the range(a,b) format
promise = "I will finish the python loops module!"

for message in range(5):
    print(promise)
```

---

The general format for a while loop is as follows

```python
while <conditional statement>:
	<action>

#Example 
count = 0
while count <= 3:
  # Loop Body
  print(count)
  count += 1
```

Decided to stop about halfway through the loop exercise module for today.

---

## Useful Information

[10 Python Code Challenges for Beginners](https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/)

## Reflections

- About 11% through the career path Data Scientist: Analytics Specialist now should finish the Python Fundamentals for Data Science (Part 1) on this career path tomorrow.
- When Part 2 is finished I should have all the non-specific python knowledge to be easily beginner+ knowledge wise
- Now i’m focusing on the career path its been useful to read what its intent is:

![Untitled](Day%208%200ef93217a829450b9d2644a7cf1374dd/Untitled.png)

- I think the most important thing about their career paths is that the foundation is common. Once that is completed it can transfer to one of the other specialisations without issue.

## Tomorrow’s Focus

- Finish Python Fundamentals part 1 and the portfolio project