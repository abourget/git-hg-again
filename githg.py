#!/usr/bin/python
# -=- encoding: utf-8 -=-

"""Git-hg is a bi-directional interface to Mercurial, like git-svn, but for Hg.

  git hg clone hg://blah/repository
  git hg push
  git hg fetch
  git hg pull


Refs:
  Isn't bi-directional: https://github.com/offbytwo/git-hg
  Hard to remember: http://traviscline.com/blog/2010/04/27/using-hg-git-to-work-in-git-and-push-to-hg/

"""

import os
import sys

# TODO: when running a command, ensure the Hg bookmark plugin is active and
#       installed

def clone(url):
    """This makes an hg clone and makes that appear as a Git repository."""
    subdir = os.path.basename(url)
    os.system("hg clone -U %s" % (url,))
    os.system("""
cd %s
hg bookmark hg/default -r default
# Do the import
hg gexport
# Configure the git repo and checkout
ln -s .hg/git .git
git branch master hg/default
git config core.bare false
git reset --hard
# Ignore the .hg stuff
echo '.hg' >> .git/info/exclude
echo "[ui]
ignore = `pwd`/.hg/hgignore" >> .hg/hgrc
echo ".git" >> .hg/hgignore
""" % subdir)

def push():
    """Pushes back to the Hg repository.

    Like ``git push``, but up to the remote Mercurial repo.

    """
    os.system("hg gimport")
    res = raw_input("Import Git commits into Hg local repo. Push back to the Hg remote ?")
    if res.lower() in ('y', 'yes', '1', 'true'):
        os.system("hg push")
        os.system("hg bookmark -f hg/default -r default")

def fetch():
    """Update the local branches with what is up on the remote Mercurial repo.

    Equivalent to ``git fetch`` in Git.

    This updates the Git branches to point to the Mercurial ones.

    """
    os.system("hg pull")
    os.system("hg bookmark -f hg/default -r default")
    os.system("hg gexport")

def pull():
    """Fetch and merge the remote changes to the Hg repo.

    Equivalent to ``git pull`` in Git.

    """
    fetch()
    os.system("git merge hg/default")


if __name__ == '__main__':
    map = {'clone': clone,
           'fetch': fetch,
           'pull': pull,
           'push': push}
    if sys.argv[1] in map:
        map[sys.argv[1]](*(sys.argv[2:]))
