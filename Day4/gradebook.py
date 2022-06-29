
# You are a student and you are trying to organize your subjects and grades using Python. Let’s explore what we’ve learned about lists to organize your subjects and scores.

# Create our lists
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

gradebook = [["physics",98],["calculus",97],["poetry", 85],["history",88]]
#print(gradebook)

# Add additional items to the list
gradebook.append(["computer science",100])
gradebook.append(["visual arts", 93])

# Update the visual arts score to 98
gradebook[-1][-1] = 98

#Replace the score for poetry with "Pass"
gradebook[2].remove(85)
gradebook[2].append("Pass")
#print(gradebook)

#combine two lists
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)