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

