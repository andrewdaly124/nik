# 1. Git Rundown

### 1.1 What is Git?
Git is a source control command line tool. Imagine it as sort of like OneDrive for code except it doesn't live update. So this repository here (andrewdaly124/nik) contains a codebase. When you want to make a change, you basically download everything from this database, make changes on your local PC, then "push" the changes you made manually back to the database. Then, when me or anyone else wants to test your changes, we "pull" the changes that you pushed from this database into our own local PCs. That's pretty much it from a very high level. I'll explain all the important functions of git in more detail in other sections.

***Making Changes***
1. Change the code on your local PC until you wanna push it
2. Push the code to the repo

***Getting Changes***
1. Pull from the repo

### 1.2 From the command line

All git commands have to be called within the directory of the repo on your pc, from the command line (there are GUI (Graphical User Interface) versions of git, but you should learn how to do these from the command line). Easiest way to do this would be one of two options:

***1. In VSCode (reccomended)***

This is the easiest way for sure. In VSCode, if you go to `file -> Open Folder` and select the folder called `nik` (or whatever this repo is called on your local filesystem), then go to `terminal -> New Terminal`, it will open a console in this directory, and you can run git commands. Do this and test, you should be able to run `git status` and the following should output:

```
PS C:\Users\pathToFolder\nik> git status
On branch main
Your branch is up to date with 'origin/main'.
```

***2. Using PowerShell (not reccomended)***

This is another way to easy open a commmand window in this directory:

1. Go into the folder containing this README
2. `shift` + right click and select "Open PowerShell window here"
3. a PowerShell window should open reading `PS C:\Users\pathToFolder\nik>`

Again, running `git status` should output this:

```
PS C:\Users\pathToFolder\nik> git status
On branch main
Your branch is up to date with 'origin/main'.
```


### Do this to run this code. I'm not done this wiki yet, I promise I'll explain these later. It's like 1 am I'm tired

1. `git clone https://github.com/andrewdaly124/nik.git` this will clone the repo to your local PC
2. You're done! wanna run the code?
    1. Go into the folder containing this README
    2. `shift` + right click and select "Open PowerShell window here"
    3. a PowerShell window should open reading `PS C:\Users\yourPCName\pathToFolder\nik>`
    4. then run the code by typing `python .\Andrew\scramble.py` or `python .\Andrew\scrambleWithNotes.py` or `python .\Nik\test.py`


### Pulling the code


