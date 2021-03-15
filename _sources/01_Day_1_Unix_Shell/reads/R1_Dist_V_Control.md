#### **Distributed version control**
In distributed version control, each user gets his or her own repository and working copy. After you commit, others have no access to your changes until you push your changes to the central repository. When you update, you do not get others' changes unless you have first pulled those changes into your repository. For others to see your changes, 4 things must happen:

- You commit
- You push
- They pull
- They update

Notice that the commit and update commands only move changes between the working copy and the local repository, without affecting any other repository. By contrast, the push and pull commands move changes between the local repository and the central repository, without affecting your working copy.

It is sometimes convenient to perform both pull and update, to get all the latest changes from the central repository into your working copy. The hg fetch and git pull commands do both pull and update. (In other words, git pull does not follow the description above, and git push and git pull commands are not symmetric. git push is as above and only affects repositories, but git pull is like hg fetch: it affects both repositories and the working copy, performs merges, etc.)
[Taken from Version Control Concepts and best practices](https://homes.cs.washington.edu/~mernst/advice/version-control.html)