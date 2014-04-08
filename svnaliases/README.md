SVN branching aliases
=====================

SVN branching is a little painful on the command line. For all those who worked with giti
a single minute of their lives, it's really frustrating. 

But it doesn't need to be so complicated. This bash aliases (they work on zsh, too) provide
commands for easier svn branching, merging and reintegrating.

Installing
==========

Fetch the branchit.rc file into your home directory and integrate it into your dotfile (.bashrc or .zshrc)

    . ~/branchit.rc

Restart your shell and off you go!

Examples
========

create a branch:

    svnbr "branchname" "commit message"

update a branch from the trunk:

    svnupbr

delete a branch:

    svndelbr $branchname

switch between trunk / branches:

    svnsw trunk
    svnsw branches/$branchname

Reintegrate a branch back into the trunk:

    svnre $branchname "commit message"

Meta
====
Maintained by Gregor Dorfbauer [@dorfbauer](https://twitter.com/dorfbauer)

If you like those scripts, have a look at my startup [Usersnap](http://usersnap.com)
