### 2.1 git status

***command***

`git status`

***function***

Shows you at a high level the things you have changed locally versus what is uploaded to the repo. For example, as I write this README, this is the output of `git status`:

```
PS C:\Users\andre\Documents\code\nik> git status 
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   gitTutorial/README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        gitTutorial/commonCommands/
```

This means that `gitTutorial/README.md` is already a file in the repo, but I have modified it locally. On the other hand, I just added the folder `gitTutorial/commonCommands/` and that does not exist on the repo, and is untracked. I can track this folder and all the files inside of it by running `git add .`, which I will explain in a seperate section. Understand that `git status` is only used to show you what changed in your local directory. Another perhaps important part is `Your branch is up to date with 'origin/main'.` which just means you have the most updated version of the repo. If you didn't, it would tell you how many commits behind you are:

```
PS C:\Users\andre\Documents\code\nik> git status
On branch main
Your branch is behind 'origin/main' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   gitTutorial/README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        gitTutorial/commonCommands/
```

