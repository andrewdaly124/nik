### 2.5 git push

***command***

`git push` (`git push origin yourBranch` <- don't worry about branches just yet)

***function***

Remember when we ran `git commit` to commit a change to your local repo? The next step is to push these chages to the github repository for everyone else to use. This is as simple as running `git push` if you are on the main branch (which when you read this, is most likely true). If you are NOT on the main branch, you will have to specify that you are not, by typing `git push origin yourBranchName`, but don't worry about this for now. Here is the output for `git push`:

```
PS C:\Users\andre\Documents\code\nik> git push
Enumerating objects: 27, done.
Counting objects: 100% (27/27), done.
Delta compression using up to 8 threads
Compressing objects: 100% (16/16), done.
Writing objects: 100% (24/24), 4.18 KiB | 2.09 MiB/s, done.
Total 24 (delta 5), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (5/5), completed with 2 local objects.
To https://github.com/andrewdaly124/nik.git
   a01c5e7..81c8f2b  main -> main
```

This is a lot of jargon. you usually don't need to pay much attention to what's being said here besides whether it was a successful push or not