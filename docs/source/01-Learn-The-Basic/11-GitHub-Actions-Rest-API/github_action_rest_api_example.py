# -*- coding: utf-8 -*-

"""
Reference:

- PyGitHub: https://pygithub.readthedocs.io/en/stable/introduction.html
"""

from pathlib import Path

from github import Github, Auth
from rich import print as rprint

token = Path.home().joinpath(".alfred-afwf_github", "default").read_text()
auth = Auth.Token(token)
gh = Github(auth=auth)
repo = gh.get_repo("MacHu-GWU/learn_github_action-project")
workflow = repo.get_workflow("01_02_minimal_workflow.yml")
workflow.create_dispatch(ref="main")
