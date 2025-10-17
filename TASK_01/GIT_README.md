This commands are used to complete a series of Git exercises, focusing on key Git concepts and workflows. Each exercise builds on fundamental Git skills, from initializing a repository
to handling merge conflicts and manipulating commit history.

Exercise 01: Initialize a Repository (Master Branch)
Objective: Initialize a new Git repository and make the first commit.
Commands Used:
git start: Initializes the repository (similar to git init; triggers start.sh in the repository).
git verify: Submits the exercise for verification.
Explanation: This exercise introduces repository creation and the custom git verify command to check completion.


Exercise 02: Commit One File
Objective: Create and commit a single file (A.txt) to the repository.
Commands Used:
git add A.txt: Stages the A.txt file.
git commit -m "commit A.txt file": Commits the staged file with a message.
git verify: Verifies the exercise completion.
Explanation: This exercise focuses on staging and committing a specific file to the repository.


Exercise 03: Commit One File (Staged)
Objective: Stage and commit only A.txt while unstaging B.txt.
Commands Used:
git reset -- B.txt: Unstages B.txt while keeping it in the working directory.
git add A.txt: Stages A.txt.
git commit -m "Add A.txt only": Commits only A.txt.
git verify: Verifies the exercise completion.
Explanation: This exercise teaches how to selectively stage files and unstage unwanted changes.


Exercise 04: Ignore Files with .gitignore
Objective: Create a .gitignore file to ignore unwanted files.
Commands Used:
echo "<file-patterns>" > .gitignore: Creates or edits the .gitignore file to specify ignored files.
git add .: Stages all modified files (including .gitignore).
git commit -m "commit useful files": Commits the changes.
git verify: Verifies the exercise completion.
Explanation: The .gitignore file prevents Git from tracking specified files (e.g., temporary files, IDE-specific files, or sensitive data).


Exercise 05: Merge Branches
Objective: Merge the escaped branch into the chase-branch.
Commands Used:
git checkout chase-branch: Switches to the chase-branch.
git merge escaped: Merges the escaped branch into chase-branch.
git verify: Verifies the exercise completion.
Explanation: This exercise demonstrates merging two branches, combining their changes into a single branch.


Exercise 06: Resolve Merge Conflicts
Objective: Resolve a merge conflict caused by changes to the same line in equation.txt.
Commands Used:
git checkout merge-conflict: Switches to the merge-conflict branch.
git merge another-piece-of-work: Attempts to merge, resulting in a conflict.
nano equation.txt: Edits the file to resolve the conflict manually.
git add equation.txt: Stages the resolved file.
git commit -m "solved merge conflict": Commits the resolved changes.
git verify: Verifies the exercise completion.
Explanation: This exercise teaches how to handle merge conflicts when two branches modify the same line in a file.


Exercise 07: Fix a Bug and Update Main Branch
Objective: Fix a bug in bug.txt on the bugfix branch and update the main branch.
Commands Used:
git switch bugfix: Switches to the bugfix branch.
nano bug.txt: Removes the buggy line in bug.txt.
git add bug.txt: Stages the changes.
git commit -m "Fixed bug in bug.txt": Commits the changes.
git switch main: Switches back to the main branch.
nano bug.txt: Adds a newline to bug.txt.
git add bug.txt: Stages the changes.
git commit -m "Added newline in bug.txt": Commits the changes.
git verify: Verifies the exercise completion.
Explanation: This exercise demonstrates switching between branches and making independent changes on each.


Exercise 08: Rebase a Feature Branch
Objective: Rebase the my-feature-branch onto the hot-bugfix branch and resolve conflicts.
Commands Used:
git switch my-feature-branch: Switches to the my-feature-branch.
git rebase hot-bugfix: Rebases the branch onto hot-bugfix, potentially causing conflicts.
nano <conflicted-file>: Resolves conflicts manually.
git add <conflicted-file>: Stages the resolved file.
git rebase --continue: Continues the rebase process.
git log --oneline: Verifies the updated commit history.
git verify: Verifies the exercise completion.
Explanation: This exercise introduces rebasing, which rewrites commit history to incorporate changes from another branch, and handling conflicts during the process.


Exercise 09: Stop Tracking a File
Objective: Stop tracking ignored.txt while keeping it locally, and update .gitignore.
Commands Used:
echo "ignored.txt" >> .gitignore: Adds ignored.txt to .gitignore.
git add .gitignore: Stages the updated .gitignore.
git rm --cached ignored.txt: Removes ignored.txt from Git tracking without deleting it locally.
git commit -m "Stop tracking ignored.txt": Commits the changes.
git verify: Verifies the exercise completion.
Explanation: This exercise shows how to stop tracking a file while keeping it in the working directory using git rm --cached.


Exercise 10: Inspect Changes with git diff
Objective: Inspect changes before and after staging using git diff.
Commands Used:
nano feature.txt: Edits feature.txt by adding a test line.
git diff: Shows unstaged changes in feature.txt.
git add feature.txt: Stages the changes.
git diff --staged: Shows staged changes.
git commit -m "Added test line to feature.txt": Commits the changes.
git verify: Verifies the exercise completion.
Explanation: This exercise demonstrates how to use git diff to review changes before and after staging.


Exercise 11: Explore Commit History
Objective: Inspect the commit history using different git log options.
Commands Used:
git log: Displays the full commit history with details (e.g., author, date, message).
git log --oneline: Shows a concise, one-line summary of commits.
git log --oneline --graph --all: Visualizes the commit history as a graph, including all branches.
git verify: Verifies the exercise completion.
Explanation: This exercise explores various ways to view the commit history for better understanding of repository changes.


Exercise 12: Amend Commit Date
Objective: Amend the latest commit to set its date to October 26, 1987, and verify the change.
Commands Used:
git commit --amend --no-edit --date="1987-10-26 10:00:00": Amends the latest commit to set the specified date without changing the message.
git log -1: Displays the latest commit to confirm the updated date.
git verify: Verifies the exercise completion.
Explanation: This exercise demonstrates how to modify a commit’s metadata (e.g., date) using git commit --amend. 
