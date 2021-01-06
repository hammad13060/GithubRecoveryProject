import os
from util import DirectoryUtil

class GithubManager:
    def __init__(self, github_accessor, git_util, backup_path_prefix):
        self.github_accessor = github_accessor
        self.git_util = git_util
        self.backup_path_prefix = backup_path_prefix
        #DirectoryUtil.delete_dir_if_exist(self.backup_path_prefix)

    def download_all_git_repos(self, username):
        user_repos = self.github_accessor.get_all_git_repos(username)
        self._download_all_git_repos_helper(user_repos)

    def _download_all_git_repos_helper(self, user_repos):
        for repo in user_repos:
            path = "{}/personal_repos/{}".format(self.backup_path_prefix, repo["name"])
            if repo["fork"]:
                path = "{}/forked_repos/{}".format(self.backup_path_prefix, repo["name"])
            DirectoryUtil.make_dir(path)
            self.git_util.clone(repo["git_url"], path, "master")

    def create_and_push_repo_data(self):
        repo_list = DirectoryUtil.get_child_directory_list("{}/personal_repos/".format(self.backup_path_prefix))
        for repo_name in repo_list:
            self.github_accessor.create_repo(repo_name)
