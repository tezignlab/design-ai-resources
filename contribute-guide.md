# 🛠Contribute to Design AI Resources

>Follow the instructions to contribute, click [here](https://www.bilibili.com/video/BV1kv411i7ms/) to see the supporting video.  
>
>Links you will need:
>- [Visual Studio Code](https://code.visualstudio.com/)
>- [Git](https://git-scm.com/)
>- [markdown](https://markdown-zh.readthedocs.io/en/latest/)

Fork this repo by clicking the `Fork` button on the top of this page.  

Clone your repo to local.  

```shell
git clone %URL_OF_YOUR_REPO
```

Add your notes.  

Push your updates to your repo.  

```shell
git add README.md   # let git know which files you want to push
```

```shell
git commit -m "%YOUR_MESSAGE"   # leave the message, so everyone can know what you have done
```

```shell
git push    # push the updates and message to your repo
```

Create a new `Pull Request` on your repo's page.  

## ⚠Notice: make sure you are up to date  

>You don't need to do this every time, but you need when original repo updates.  

### Configure `upstream`  

List the current configured remote repository for your fork. You should only see `origin`.  

```shell
git remote -v
```

Specify a new remote `upstream` repository that will be synced with the fork.  

```shell
git remote add upstream https://github.com/tezignlab/ai-design-papers.git
```

Verify the new upstream repository you've specified for your fork. You should see both `origin` and `upstream`.

```shell
git remote -v
```

### Sync your fork

Fetch the branches and their respective commits from upstream repo.  

```shell
git fetch upstream
```

Check out your fork's local master branch.

```shell
git checkout master
```

Merge the changes from upstream/master into your local master branch.

```shell
git merge upstream/master
```
