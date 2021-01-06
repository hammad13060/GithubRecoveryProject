import requests
import git
from util import GitUtil
from accessor import GitHubAccessor
from manager import GithubManager
from apptoken import GithubToken
import os

if __name__ == "__main__":
    base_path = os.getcwd()
    git_util = GitUtil(git)
    github_token = GithubToken("{}/config/github_token.json".format(base_path))
    github_accessor = GitHubAccessor(github_token, requests)
    github_manager = GithubManager(github_accessor, git_util, "{}/backup".format(base_path))
    github_manager.create_and_push_repo_data()
