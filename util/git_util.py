class GitUtil:
    def __init__(self, git):
        self.git = git
    def clone(self, repo_uri, local_path, branch):
        repo = self.git.Repo.clone_from(repo_uri, local_path, branch=branch)

        # Clone the other branches as needed and setup them tracking the remote
        for b in repo.remote().fetch():
            print(b.name)
            repo.git.checkout('-B', b.name.split('/')[1], b.name)
