SVN branching aliases
=====================

small examples:

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
Maintained by Gregor Dorfbauer @dorfbauer

If you like those scripts, have a look at my startup [Usersnap](http://usersnap.com)
