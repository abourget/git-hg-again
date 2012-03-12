git-hg bi-directional interface
-------------------------------

This does the job "hg-git" does for Mercurial, but the reverse.  It actually uses
the same tool (the gexport / gimport feature of Hg-Git), written by GitHub.

This is based on the Blog post by Travis Cline

  http://traviscline.com/blog/2010/04/27/using-hg-git-to-work-in-git-and-push-to-hg/

To install:

  sudo ln -s `pwd`/githg.py /usr/lib/git-core/git-hg

Make sure you have hg-git installed.  See http://hg-git.github.com/

  git hg clone https://bitbucket.org/user/project

Work on your Git repo, do some commits.

  git hg push

which pushes to the local .hg repo, and offers to push upstream.

When new changes arrive from upstream, run:

  git hg fetch

or

  git hg pull

which map to the same Git semantics: ``fetch`` updates your branch with new stuff, and ``pull`` adds a merge to the mix.

This code is not yet tested with complex topologies, additions, comments and pull requests are welcome.



TODO
----

git-hg should check for a same bookmarks Hg configuration, etc.

The first release was written at PyCon 2012, by Alexandre Bourget
