import json
GITHUB_WELL_KNOWN_API_DICT = {
    "user_data": "https://api.github.com/users/{}",
    "user_repos": "https://api.github.com/user/repos"
}

class GitHubAccessor:
    def __init__(self, github_token, requests):
        self.github_token = github_token
        self.requests = requests

    def get_all_git_repos(self, username):
        user_data = self.get_user_data(username)
        user_repos = self._get(user_data["repos_url"])
        return user_repos

    def get_user_data(self, username):
        uri = GITHUB_WELL_KNOWN_API_DICT["user_data"].format(username)
        return self._get(uri)

    def create_repo(self, repo_name):
        headers = {
            "Authorization": "token {}".format(self.github_token.token)
        }
        payload = {
            "name": repo_name
        }
        res = self.requests.post(GITHUB_WELL_KNOWN_API_DICT["user_repos"], data=json.dumps(payload), headers=headers)
        if res.status_code == self.requests.codes.unprocessable_entity:
            print("Repository {} already exists".format(repo_name))
        elif res.status_code != self.requests.codes.created:
            raise Exception("POST: {} failed for {} with status code {}".format(GITHUB_WELL_KNOWN_API_DICT["user_repos"], repo_name, res.status_code))

    def _get(self, uri):
        res = self.requests.get(uri)
        if res.status_code == self.requests.codes.ok:
            return res.json()
        raise Exception("GET: {} failed with status code {}".format(uri, res.status_code))
