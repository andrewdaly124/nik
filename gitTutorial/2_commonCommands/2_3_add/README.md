### 2.3 git add

***command***
`git add "filename"` (commonly `git add .`)

***function***
Remember when running `git status` it shows all the changed files in your local repo? `git add` will add those files to be tracked and committed into the repo. Basically this is like "collect all my changes and prepare them to be added to the actual github repo". ***This does not push the changes, there are more steps. All this does is collect all your changes***

The way this works is after typing `git add`, you can specify the filename (ex. `git add README.md` or `git add Andrew/scramble.py`), but MOST OFTEN you'll be running `git add .`, `.` is a macro which means "everything". You will usually want to commit everything.

`git add` HAS NO OUTPUT! but, after running, you can check if they are added by running `git status` once again. you'll see something like this:

```
PS C:\Users\andre\Documents\code\nik> git add .
PS C:\Users\andre\Documents\code\nik> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   gitTutorial/2_commonCommands/2_1_status/README.md
        new file:   gitTutorial/2_commonCommands/2_2_pull/README.md
        new file:   gitTutorial/2_commonCommands/2_3_add/README.md
        new file:   gitTutorial/2_commonCommands/README.md
        modified:   gitTutorial/README.md
        deleted:    gitTutorial/testWillRemove
```

