### 2.3 git add

***command***
`git add "filename"` (commonly `git add .`)

***function***
Remember when running `git status` it shows all the changed files in your local repo? `git add` will add those files to be tracked and committed into the repo. Basically this is like "collect all my changes and prepare them to be added to the actual github repo". ***This does not push the changes, there are more steps. All this does is collect all your changes***

The way this works is after typing `git add`, you can specify the filename (ex. `git add README.md` or `git add Andrew/scramble.py`), but MOST OFTEN you'll be running `git add .`, `.` is a macro which means "everything". You will usually want to commit everything.