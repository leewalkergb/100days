# Day 4

Added to Github?: Yes
Completion date: 29/06/2022
Language: Python

# Today’s Focus

- Finish the lists module on codeacademy

# Notes

---

**Start 20:30** 

Completed the gradebook project.

My continuous mistake with lists is added and removing things with the methods when using a 2D list.

```python
list[1,2,3,4]
list.append()
list.remove()

#When using a 2D list we reference the index and then the element we want to remove
list[2].append("Dog")

#What ever is in the remove bracket is what it looks to remove
list[2].remove(3)
```

There are a lot of methods for lists:

![Untitled](Day%204%20ef0be7d02c924578bf63663d4b2420c1/Untitled.png)

Based on the work done the most important take aways are:

```python
.insert(<index><element>)

#pop with no index removes the last element
.pop(<index>)

#range is its own object but we can cast it to a list
list(range())

#range syntax
range(<start>,<endpoint-1>,<increment_size>)
```

Managed to complete up to the len() function and stopped there for tonight

## Useful Information

---

- Watched an interesting video on the streamlit library for python today. It may be interesting to use it for a mini project
    - Maybe a todo app now that I’m doing lists?
- When you have a local workspace with folders and you don’t use git add . to stage you need to specify the path and filename if you want to be specific.
- Insteresting streamlit video

[How to Build Your First Data Science Web App in Python - Streamlit Tutorial #1](https://www.youtube.com/watch?v=ZZ4B0QUHuNc)

## Reflections

---

- As expected lists have a lot of things you can do with them and nice built in functions, basically arrays/lists are the most important basic data type
- I got in from work really late today and it made me almost not want to do any coding so I need to keep that in mid for the future
- I want to make at least one portfolio project that has a webapp component to it

---

# Tomorrow’s Focus

---

- Finish the working with lists section and begin the section on list comprehensions