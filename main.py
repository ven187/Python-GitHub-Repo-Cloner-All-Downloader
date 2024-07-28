import os
import requests
import subprocess

def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        return [repo['full_name'] for repo in response.json()]
    else:
        print("Failed to retrieve user information.")
        return []

def clone_repo(repo, base_dir):
    url = f"https://github.com/{repo}.git"
    repo_name = repo.split('/')[1]
    repo_dir = os.path.join(base_dir, repo_name)
    subprocess.run(['git', 'clone', url, repo_dir])

username = "username"
repos = get_repos(username)

# Create a directory named after the username
base_dir = os.path.join(os.getcwd(), username)
os.makedirs(base_dir, exist_ok=True)

# Clone each repository into the user directory
for repo in repos:
    clone_repo(repo, base_dir)
