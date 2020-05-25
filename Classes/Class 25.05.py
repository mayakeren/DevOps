In Terminal:

Last login: Mon May 25 18:56:29 on ttys000
maya.keren@Mayas-MacBook-Pro ~ % mkdir DevOpsDir
maya.keren@Mayas-MacBook-Pro ~ % cd DevOpsDir
maya.keren@Mayas-MacBook-Pro DevOpsDir % git init
Initialized empty Git repository in /Users/maya.keren/DevOpsDir/.git/
maya.keren@Mayas-MacBook-Pro DevOpsDir % git statuse
git: 'statuse' is not a git command. See 'git --help'.

The most similar command is
	status
maya.keren@Mayas-MacBook-Pro DevOpsDir % git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
maya.keren@Mayas-MacBook-Pro DevOpsDir % git config user.name "mayakeren"
maya.keren@Mayas-MacBook-Pro DevOpsDir % git config user.name "mayakeren"
maya.keren@Mayas-MacBook-Pro DevOpsDir % git config user.name "mayakeren"
maya.keren@Mayas-MacBook-Pro DevOpsDir % git config user.name "mayakeren"
maya.keren@Mayas-MacBook-Pro DevOpsDir % echo Maya > tetsfile.txt
maya.keren@Mayas-MacBook-Pro DevOpsDir % open .
maya.keren@Mayas-MacBook-Pro DevOpsDir % git add testfile.txt
fatal: pathspec 'testfile.txt' did not match any files
maya.keren@Mayas-MacBook-Pro DevOpsDir % git add tetsfile.txt
maya.keren@Mayas-MacBook-Pro DevOpsDir % git commit -m "Add my first file"
[master (root-commit) daa9a2c] Add my first file
 1 file changed, 1 insertion(+)
 create mode 100644 tetsfile.txt
maya.keren@Mayas-MacBook-Pro DevOpsDir % ech "Hi, I'm another file" > anotherfile.txt
zsh: command not found: ech
maya.keren@Mayas-MacBook-Pro DevOpsDir % echo "Hi, I'm another file" > anotherfile.txt
maya.keren@Mayas-MacBook-Pro DevOpsDir % git add
Nothing specified, nothing added.
Maybe you wanted to say 'git add .'?
maya.keren@Mayas-MacBook-Pro DevOpsDir % git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
	add
maya.keren@Mayas-MacBook-Pro DevOpsDir % git add .
maya.keren@Mayas-MacBook-Pro DevOpsDir % git commit-m "add another file"
git: 'commit-m' is not a git command. See 'git --help'.

The most similar command is
	commit-tree
maya.keren@Mayas-MacBook-Pro DevOpsDir % git commit -m "add another file"
[master 1eb6811] add another file
 1 file changed, 1 insertion(+)
 create mode 100644 anotherfile.txt
maya.keren@Mayas-MacBook-Pro DevOpsDir % git branch branchy
maya.keren@Mayas-MacBook-Pro DevOpsDir % git branch
  branchy
* master
maya.keren@Mayas-MacBook-Pro DevOpsDir % git checkout branchy
Switched to branch 'branchy'
maya.keren@Mayas-MacBook-Pro DevOpsDir % echo Hi >> anotherfile.txt
maya.keren@Mayas-MacBook-Pro DevOpsDir % git add .
maya.keren@Mayas-MacBook-Pro DevOpsDir % git commit -m "changed again"
[branchy 99b4f46] changed again
 1 file changed, 1 insertion(+)
maya.keren@Mayas-MacBook-Pro DevOpsDir % cut anotherfile.txt
usage: cut -b list [-n] [file ...]
       cut -c list [file ...]
       cut -f list [-s] [-d delim] [file ...]
maya.keren@Mayas-MacBook-Pro DevOpsDir % cat anotherfile.txt
Hi, I'm another file
Hi
maya.keren@Mayas-MacBook-Pro DevOpsDir % git chechout master
git: 'chechout' is not a git command. See 'git --help'.

The most similar command is
	checkout
maya.keren@Mayas-MacBook-Pro DevOpsDir % git branch
* branchy
  master
maya.keren@Mayas-MacBook-Pro DevOpsDir % git checkout branchy
Already on 'branchy'
maya.keren@Mayas-MacBook-Pro DevOpsDir % git checkout master
Switched to branch 'master'
maya.keren@Mayas-MacBook-Pro DevOpsDir % git branch
  branchy
* master
maya.keren@Mayas-MacBook-Pro DevOpsDir % echo "Hi I was changed in master" >> anotherfile.txt
maya.keren@Mayas-MacBook-Pro DevOpsDir % git commit -d -m "add line on sample.txt"
error: unknown switch `d'
usage: git commit [<options>] [--] <pathspec>...

    -q, --quiet           suppress summary after successful commit
    -v, --verbose         show diff in commit message template

Commit message options
    -F, --file <file>     read message from file
    --author <author>     override author for commit
    --date <date>         override date for commit
    -m, --message <message>
                          commit message
    -c, --reedit-message <commit>
                          reuse and edit message from specified commit
    -C, --reuse-message <commit>
                          reuse message from specified commit
    --fixup <commit>      use autosquash formatted message to fixup specified commit
    --squash <commit>     use autosquash formatted message to squash specified commit
    --reset-author        the commit is authored by me now (used with -C/-c/--amend)
    -s, --signoff         add Signed-off-by:
    -t, --template <file>
                          use specified template file
    -e, --edit            force edit of commit
    --cleanup <mode>      how to strip spaces and #comments from message
    --status              include status in commit message template
    -S, --gpg-sign[=<key-id>]
                          GPG sign commit

Commit contents options
    -a, --all             commit all changed files
    -i, --include         add specified files to index for commit
    --interactive         interactively add files
    -p, --patch           interactively add changes
    -o, --only            commit only specified files
    -n, --no-verify       bypass pre-commit and commit-msg hooks
    --dry-run             show what would be committed
    --short               show status concisely
    --branch              show branch information
    --ahead-behind        compute full ahead/behind values
    --porcelain           machine-readable output
    --long                show status in long format (default)
    -z, --null            terminate entries with NUL
    --amend               amend previous commit
    --no-post-rewrite     bypass post-rewrite hook
    -u, --untracked-files[=<mode>]
                          show untracked files, optional modes: all, normal, no. (Default: all)

maya.keren@Mayas-MacBook-Pro DevOpsDir % git commit -a -m "add line on sample.txt"
[master d3c85f7] add line on sample.txt
 1 file changed, 1 insertion(+)
maya.keren@Mayas-MacBook-Pro DevOpsDir % git merge new_feature
merge: new_feature - not something we can merge
maya.keren@Mayas-MacBook-Pro DevOpsDir % git merge branchy
Auto-merging anotherfile.txt
CONFLICT (content): Merge conflict in anotherfile.txt
Automatic merge failed; fix conflicts and then commit the result.
maya.keren@Mayas-MacBook-Pro DevOpsDir % git commit -a -m "fixed conflicts"
[master 3a12124] fixed conflicts
maya.keren@Mayas-MacBook-Pro DevOpsDir % git log
commit 3a12124ee6aa2a01627b4fd81e505491b055b15c (HEAD -> master)
Merge: d3c85f7 99b4f46
Author: mayakeren <maya.keren@gmail.com>
Date:   Mon May 25 20:33:38 2020 +0300

    fixed conflicts

commit d3c85f743e8dbae2e94645645432102f81ecac93
Author: mayakeren <maya.keren@gmail.com>
Date:   Mon May 25 20:21:29 2020 +0300

    add line on sample.txt

commit 99b4f46a84157d06b7809f0e3e14cd37f05bddfc (branchy)
Author: mayakeren <maya.keren@gmail.com>
Date:   Mon May 25 19:53:55 2020 +0300

    changed again

commit 1eb681180dfedfbbc66d4c0d099fdaa926e228f4
Author: mayakeren <maya.keren@gmail.com>
Date:   Mon May 25 19:34:27 2020 +0300

    add another file

commit daa9a2cf66f20dcbb6b1797f61888ea3f9b6b991
Author: mayakeren <maya.keren@gmail.com>
Date:   Mon May 25 19:25:12 2020 +0300

    Add my first file
maya.keren@Mayas-MacBook-Pro DevOpsDir % git checkout 1eb681180dfedfbbc66d4c0d099fdaa926e228f4
Note: switching to '1eb681180dfedfbbc66d4c0d099fdaa926e228f4'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 1eb6811 add another file
maya.keren@Mayas-MacBook-Pro DevOpsDir % git commit
HEAD detached at 1eb6811
nothing to commit, working tree clean
maya.keren@Mayas-MacBook-Pro DevOpsDir % git checkout master
Previous HEAD position was 1eb6811 add another file
Switched to branch 'master'
maya.keren@Mayas-MacBook-Pro DevOpsDir %
