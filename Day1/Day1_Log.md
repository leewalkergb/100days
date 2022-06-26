# Day 1

Added to Github?: No
Language: Git

# Today’s Focus

- Set up github directory for the 100 days of code
- clone directory locally and create day 1 folder, push and commit
    - Use the command line to do this as per the objectives
- Begin with python lists section on the data science pathway of codeacademy

# Notes

- Launched git Bash and made new directory

```bash
mkdir 100_days_of_code
cd 100_days_of_code
```

- Useful to know that git bash has autocomplete on tab so I jump to that directory just by typing cd 100 [tab]
- I decided to make the directory locally and commit it later, the following command makes the directory into a git repo

```bash
git init
```

I noticed I put the folder in the wrong place so I manually deleted it decided to clone a repo where I wanted it to be.

Repo was created online and called “100 days” with the following url: [https://github.com/leewalkergb/100days.git](https://github.com/leewalkergb/100days.git)

```bash
git clone https://github.com/leewalkergb/100days.git
cd 100days
mkdir Day1
```

Still having odd problems pushing to it, maybe because I haven’t set up remote?

Decided to go through the learn-git pathway on codeacademy quickly so I’m not continually getting stuck.

**Notes on git**

- Version control system that allows us to manage modifications and changes
- A repo is the core of a project and can hold many branches
- When making changes or additions we can branch and not mess with the functionality of the main project

We can turn any directory into a git project. We use this by using the init command, which sets up the tools Git needs to track changes made.

For the purpose of this course I’ve decided to make a repo on my desktop for testing called TestRepo2.

To set up the repo i did the following:

```bash
#navigate to desktop
cd Desktop

#create directory
mkdir TestRepo2

#switch to the new path and init
cd TestRepo2
git init

```

The result was as show below:

![Untitled](Day%201%20224d4837d5544bba81a2fdf32c29e6fa/Untitled.png)

Git projects can be thought of as 3 parts:

1. a working directory - where we create edit, delete and organise files
2. a staging area - where we list the changes we make to the working directory
3. a repository - where git stores those changes as different versions of the project

![Untitled](Day%201%20224d4837d5544bba81a2fdf32c29e6fa/Untitled%201.png)

We can check the status of the changes we make using the status command.

The learning pathway uses a file for performing operations on so I created one locally called screenplay.txt

```bash
#first tried touch command but it doesn't work on windows cmd
touch screenplay.txt

#Made a file by using the echo command
echo [SOME TEXT] > screenplay.txt
```

Got annoyed with some commands I know from bash so switched to powershell locally.

![Untitled](Day%201%20224d4837d5544bba81a2fdf32c29e6fa/Untitled%202.png)

I used the git status command to check the repo status:

![Untitled](Day%201%20224d4837d5544bba81a2fdf32c29e6fa/Untitled%203.png)

As expected there are untracked changes due to the creation of the screenplay.txt file.

```bash
# following the tutorial I add the file and recheck the status
git add screenplay.txt
git status
```

![Untitled](Day%201%20224d4837d5544bba81a2fdf32c29e6fa/Untitled%204.png)

Et voila we now have staged changes to commit.

The tutorial now edits the file and checks what the changes are, so I have to google how to open, edit and save a file via powershell.

It looks like there are a variety of ways to do this based on this link: [https://www.delftstack.com/howto/powershell/edit-a-text-file-on-the-console-using-powershell/](https://www.delftstack.com/howto/powershell/edit-a-text-file-on-the-console-using-powershell/)

First I used notepad:

```bash
notepad screenplay.txt
```

This opened notepad and allowed me to edit and save the file.

I tried nano but as the link says you have to install it so I just stuck with notepad for now.

```bash
git diff screenplay.txt
```

![Untitled](Day%201%20224d4837d5544bba81a2fdf32c29e6fa/Untitled%205.png)

Ta Da added text was tracked.

```bash
#stage the changed file and then check the status
git add screenplay.txt
git status
```

Next I went to commit the changes

```bash
git commit -m "MESSAGE"
```

![Untitled](Day%201%20224d4837d5544bba81a2fdf32c29e6fa/Untitled%206.png)

The tutorial then shows you how to check the log of commits

```bash
git log
```

![Untitled](Day%201%20224d4837d5544bba81a2fdf32c29e6fa/Untitled%207.png)

That completes the first lesson.

I decided to push this to my 100 day repo:

```bash
#This didn't work as I had no remote connection
git push

# So I set it up
git remote add Day1 https://github.com/leewalkergb/100days.git
git branch -M main
git push -u Day1 main
```

This text was there when I created the repo so it seemed like I was missing the remote connection.

This got me thinking, now that the repo is properly set up and I’ve successfully done some work can I clone it?

The answer is yes:

```bash
git clone https://github.com/leewalkergb/100days.git
```

![Untitled](Day%201%20224d4837d5544bba81a2fdf32c29e6fa/Untitled%208.png)

That put a 100 days folder into the one I already had so I delete and restarted

I then moved the screenplay.txt to the day 1 folder to tidy things up

![Untitled](Day%201%20224d4837d5544bba81a2fdf32c29e6fa/Untitled%209.png)

```bash
#I tried to push the changes without staging first
git push

#So I added them checked status
git add .
git status

#I tried to push again but you can do that until you commit
#I forgot to -m "Message" so it forced me to add it via visual studio code 
git commit
git log #To check if the message saved

git push
```

So I need to remember the order of operations is:

```bash
git add .
git commit -m "Message"
git push
```

# TLDR Summary

## Commands Learned

- git init - creates a new git repository
- git status - inspects the contents of the staging area
- git add - adds files from the working directory to the staging area
- git diff - lists the differences between the working directory and the staging area
- git commit - stores file changes from the staging area in the repository
- git log - shows a list of previous commits

## Useful Information

- There’s a decent git cheat sheet here:

[](https://education.github.com/git-cheat-sheet-education.pdf)

- Basic windows command line cheatsheet

[](http://www.cs.columbia.edu/~sedwards/classes/2015/1102-fall/Command%20Prompt%20Cheatsheet.pdf)

- Codeacademy git cheatsheet:

[Learn Git & GitHub: Basic Git Workflow Cheatsheet | Codecademy](https://www.codecademy.com/learn/learn-git/modules/learn-git-git-workflow-u/cheatsheet)

## Reflections

There’s no need to rush things, just take your time and learn how to do things one step at a time. I was trying to do all this fancy git management and write my code and all these other things and spinning my wheels because I didn’t understand what I was doing.

Once I switched to git learning path everything was easy and it’ll set me up well for the future.

**Things I learned today:**

- Windows default command line is rubbish, powershell or git bash is much more enjoyable to use.
- I need to learn more notion shortcuts but for now I have the basics.
- Writing up, doing the lessons on codeacademy and locally is a lot of work so I’ll have to review this in the future. My notes should be less I did this and I did that and just summaries of what I learned, what I struggled with and what I will focus on next.

## Tomorrow’s Focus

- Complete the git learning path on codeacademy
- If time then continue with the data science on codeacademy