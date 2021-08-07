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

### 1.2 What is a branch?
A branch is a "version" of the codebase. Usually, there is one "main" branch (often called `main` or `develop` or something really general) which has the main code that everybody using the repo works off of. So for example if we're making a website, then the `main` branch would typically have a fully working and mostly bug free version of the website that people can pull, build and run. But say I wanted to make a huge change (ex. I wanna change the entire UI of the app) then this doesn't typically get done in one change (called a commit), but instead is done in many smaller commits on a separate branch that I'm using
