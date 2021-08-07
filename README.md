# Nik's Funhouse

Using this github as a way to watch Nik's coding progress, help with actual code reviews, and teach him git cause it's important. All contributions welcome

# 1. Git Rundown

### 1.1 What is Git?
Git is a source control command line tool. Imagine it as sort of like OneDrive for code except it doesn't live update. So this repository here (andrewdaly124/nik) contains a codebase. When you want to make a change, you basically download everything from this database, make changes on your local PC, then "push" the changes you made manually back to the database. Then, when me or anyone else wants to test your changes, we "pull" the changes that you pushed from this database into our own local PCs. That's pretty much it from a very high level. I'll explain all the important functions of git in more detail in other sections.

***Making Changes***
1. Change the code on your local PC until you wanna push it
2. Push the code to the repo

***Getting Changes***
1. Pull from the repo

### Do this to run this code. I'm not done this wiki yet, I promise I'll explain these later. It's like 1 am I'm tired

1. `git clone https://github.com/andrewdaly124/nik.git` this will clone the repo to your local PC
2. You're done! wanna run the code?
    a. Go into the folder containing this README
    b. `shift` + right click and select "Open PowerShell window here"
    c. a PowerShell window should open reading `PS C:\Users\yourPCName\pathToFolder\nik>`
    d. then run the code by typing `python .\Andrew\scramble.py` or `python .\Andrew\scrambleWithNotes.py` or `python .\Nik\test.py`

