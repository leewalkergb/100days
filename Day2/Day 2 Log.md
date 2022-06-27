# Day 2

Added to Github?: No

# Today’s Focus

- Continue with the Learn Git and GitHub course on codeacademy
    - Aim - Complete Basic Git Workflow Section

# Notes

The second project looks at the following:

![Untitled](Day%202%20a0ef418761ed47e189c81825e3a1420f/Untitled.png)

I will be:

- initialising a repo,
- checking status,
- adding files to the staging area,
- confirm they have been staged,
- commit
- check the logs

```bash
git init
git status
git add .
git status
git commit -m "Added files to be commited"
git log
```

![Untitled](Day%202%20a0ef418761ed47e189c81825e3a1420f/Untitled%201.png)

The project then requires the file to be updated:

![Untitled](Day%202%20a0ef418761ed47e189c81825e3a1420f/Untitled%202.png)

Important to note that git add can be everything or a specific file:

```bash
#This adds everything to the staging area
git add .

#This adds a specific file
git add <FILENAME>
```

Finally completed the quiz for this section of the Git and GitHub course:

![Untitled](Day%202%20a0ef418761ed47e189c81825e3a1420f/Untitled%203.png)

---

Looking at the Git & GitHub syllabus I think the priority should be on:

- Basic Git Workflow
- Important git Operations
- Git branching

Then as needed:

- Deploying websites using Git and Github (this supports an objective)
- Best practices for Git and Github repos

---

Started the important git operations lesson.

The lessons introduce the HEAD command:

```bash
git show HEAD
```

![Untitled](Day%202%20a0ef418761ed47e189c81825e3a1420f/Untitled%204.png)

Git checkout allows us to change things in the working directory to discard changes made.

In my local version because I never pushed to the repo it reverted to the original text from the beginning:

![Untitled](Day%202%20a0ef418761ed47e189c81825e3a1420f/Untitled%205.png)

Note the - before the new ghost text.

We can unstage things by using the git reset command:

```bash
git reset HEAD filename
```

I added a change to my scene-5.txt file and staged the change

![Untitled](Day%202%20a0ef418761ed47e189c81825e3a1420f/Untitled%206.png)

```bash
git reset HEAD scene-5.txt
```

![Untitled](Day%202%20a0ef418761ed47e189c81825e3a1420f/Untitled%207.png)

interesting that when checking status git bash gives the following option to unstage changes:

```bash
git restore --staged <file>
```

It seems to work the same:

![Untitled](Day%202%20a0ef418761ed47e189c81825e3a1420f/Untitled%208.png)

Its interesting that you can also roll back to a specifc SHA (by taking the first 7 characters of the SHA of a previous commit: 

![Untitled](Day%202%20a0ef418761ed47e189c81825e3a1420f/Untitled%209.png)

```bash
git reset commit_SHA
```

I didn’t do this on my local repo for simplicity reasons.

![Untitled](Day%202%20a0ef418761ed47e189c81825e3a1420f/Untitled%2010.png)

# Summary

- git checkout HEAD filename - Discards changes in the working directory
- git reset HEAD filename - Discards changes in the staging area
- git reset commit_SHA - Resets to a previous commit in the commit history.

## Useful Information

- Cheatsheet for these operations

[Learn Git & GitHub: Important Git Operations Cheatsheet | Codecademy](https://www.codecademy.com/learn/learn-git/modules/learn-git-git-backtracking-u/cheatsheet)

## Reflections

- Important to be quite specific with your commands especially with checkout, reset and add.
- I’m feeling very confident creating a repo adding committing and pushing now, will need more practice with rolling back in the future however.
- I may eventually split my coding days
    - One part in the morning or at lunch covering softer skills like specification, design and config management
    - One part in the afternoon where I focus on coding project.

## Tomorrow’s Focus

- Complete the Important git operations projects then.