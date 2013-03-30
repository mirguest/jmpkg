#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lintao

# parse the command line.

import git

# 1. get the repo
# $ jmpkg get-repo URL
def get_repo(repo_url):
    # make sure we are in a git repo or not
    try:
        repo = git.Repo(".")
    except:
        repo = repo.clone(repo_url)

    # make set sparse checkout
    writer = repo.config_writer()
    writer.set("core", "sparseCheckout", True)
    # make all file hide
    with open("%s/info/sparse-checkout"%repo.git_dir, "a") as f:
        f.write("")

    gitcmd = repo.git
    gitcmd.read_tree("-m", "-u", "HEAD")
    
 
if __name__ == "__main__":

    repo_url = "/home/ihep/git/REPO"
    get_repo(repo_url)
