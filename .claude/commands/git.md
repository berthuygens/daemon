# Git PR Workflow

Create a pull request and optionally approve + merge it immediately using admin privileges.

## Instructions

1. First, check the current git status and branch:
   - Run `git status` to see changes
   - Run `git branch --show-current` to get current branch name
   - If on `main`, warn the user they should create a feature branch first

2. If there are uncommitted changes, ask if the user wants to commit them first

3. Check if the branch has been pushed to remote:
   - Run `git log origin/$(git branch --show-current)..HEAD 2>/dev/null` to see unpushed commits
   - If there are unpushed commits, push to remote with `git push -u origin $(git branch --show-current)`

4. Create a Pull Request:
   - Use `gh pr create` with a clear title and description
   - Generate the PR body based on the commits in the branch
   - Format: `gh pr create --title "Title" --body "Description"`

5. After PR is created, use AskUserQuestion to ask the user:
   - Question: "PR created! Do you want to approve and merge it now?"
   - Options:
     - "Yes, approve and merge to main" (recommended)
     - "No, just leave the PR open"

6. If user chooses to merge:
   - Approve the PR with admin rights: `gh pr review --approve`
   - Merge the PR: `gh pr merge --admin --squash --delete-branch`
   - Confirm success to the user

7. Return the PR URL to the user
