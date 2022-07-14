# How to compare two folders and cherry-pick the differences

If you want to compare two specific folders of two separate branch and cherry-pick anything into your target for that specific folder this command might be handy for you:
```bash
git cherry-pick $(git log --format=oneline --no-merges staging...development parent_folder/child_folder | tail -r | cut -d " " -f 1)
```
This will get every commit In reverse order from dev compared to staging

`tail -r`: this is to reverse the order of commits

`cut -d " " -f 1`: this is splitting the log output and takes the first item which is the commit hash

* You can see and assess the result by running the git log first and then cherry pick,

```bash 
git log --format=oneline --no-merges staging...development parent_folder/child_folder | tail -r | cut -d " " -f 1
```

* Good thing about this way is you only pick whatever you have done in your specific folder, like when you worked on a specific dag and you want to cherry pick anything related to your work only.

**For cherry-picking from dev to staging:**

1. Update your dev and staging from remote changes
2. create a branch from staging
3. switch to newly created branch
4. run only the git log to assess the result
5. run the whole git cherry pick command
6. create your PR!

I think some might know this already but I thought it might help sharing it anyway.

[reference stackoverflow question](https://stackoverflow.com/questions/19821749/git-cherry-pick-or-merge-specific-directory-from-another-branch)
