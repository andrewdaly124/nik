### 2.4 git commit

***command***

`git commit` (`git commit -m "Your commit message"`)

***function***

Remember when we ran `git add` to collect all local changes? This will get all those changes marked by `git add`, and package them into a change (commit). ***Unlike git add, where we can unstage files for change, THIS IS PERMANENT, meaning as soon as you run git commit, it will mark the files as an official change, and any future changes MUST be done, in a seperate commit***. It's not that big of a deal if you do make an accidental commit, just a bit annoying since now you have to revert those changes in a seperate commit.

NOTE: Running this does not upload the code to github. it only marks the change in your local repo. to push the changes, you need to run `git push` which I will explain in the next section

To use this, type the following: `git commit -m`, the `-m` tells the `commit` command that the next argument is the commit message, which can be whatever you want. For me as I write this wiki, my commit message will be something along the lines of `"Add documentation for common git commands"`. So the final command will be `git commit -m "Add documentation for common git commands"`. Which outputs this:

```
PS C:\Users\andre\Documents\code\nik> git add .
PS C:\Users\andre\Documents\code\nik> git commit -m "Add documentation for common git commands"
[main a9e89f7] Add documentation for common git commands
 7 files changed, 111 insertions(+), 17 deletions(-)
 create mode 100644 gitTutorial/2_commonCommands/2_1_status/README.md
 create mode 100644 gitTutorial/2_commonCommands/2_2_pull/README.md
 create mode 100644 gitTutorial/2_commonCommands/2_3_add/README.md
 create mode 100644 gitTutorial/2_commonCommands/2_4_commit/README.md
 create mode 100644 gitTutorial/2_commonCommands/README.md
 delete mode 100644 gitTutorial/testWillRemove
```