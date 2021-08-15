### 2.2 git pull

***command***
`git pull`

***function***
Pulls the most updated version of the repo from the branch you are currently on. Don't worry too much about what branches are for now. If you already have the most updated version of the code, this should output:

```
PS C:\Users\andre\Documents\code\nik> git pull
Already up to date.
```

Otherwise it'll output something along the lines of this:

```
PS C:\Users\andre\Documents\code\nik> git pull
Updating 92244b0..a01c5e7
Fast-forward
 gitTutorial/testWillRemove | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 gitTutorial/testWillRemove
```