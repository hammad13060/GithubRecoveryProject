import json

class GithubToken:
    def __init__(self, path):
        with open(path, 'r') as token_file:
            self.token = json.loads(token_file.read())["access_token"]
