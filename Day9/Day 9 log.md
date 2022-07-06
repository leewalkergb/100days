# Day 9

Added to Github?: Yes
Completion date: 06/07/2022
Language: Python

# Today’s Focus

- Finish Python Fundamentals part 1 and the portfolio project

# Notes

<aside>
💡 To exit an infinite loop we can use control + c

</aside>

We can stop an iteration by using the break statement

```python
for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break
```

Similarly continue allows us to skip an iteration of a loop

```python
for i in ages:
  if i < 21:
    continue
  print(i)
```

Nested loop

```python
# Nested Loop
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for location in sales_data:
  for sales in location:
    # looping through the sublists and finding the sum
    scoops_sold += sales
print(scoops_sold)
```

Completed the loop version of the medical insurance project

---

## Useful Information

- List of code review tools

[12 Best Code Review Tools for Developers (2022 Edition)](https://kinsta.com/blog/code-review-tools/)

## Reflections

- Frida Kahlo project done

## Tomorrow’s Focus

- Will go and complete module 1 and 2 of the path tomorrow