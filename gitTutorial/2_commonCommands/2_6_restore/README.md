### 2.6 git restore

***command***

`git restore` (`git restore FileName`, `git restore .` <- be fucking careful with this)

***function***

`git restore` will revert changes back to what they are on the online repo. This means it ***wipes all of your local changes***, so obviously be very careful when you use this. ***YOU CAN'T UNDO THIS COMMAND***. I usually only use this to rever one file at a time. This function has no output, but here's an example of reverting my changes to `gitTutorial/2_commonCommands/README.md`:

```
PS C:\Users\andre\Documents\code\nik> git restore gitTutorial/2_commonCommands/README.md
```
