#!/usr/bin/python3
"""
Script to list 10 most recent commits of a GitHub repository using GitHub API.
"""
import requests
from sys import argv

def list_commits(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]  # Get the 10 most recent commits
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Error:", response.text)

if __name__ == "__main__":
    if len(argv) == 3:
        repo_owner = argv[1]
        repo_name = argv[2]
        list_commits(repo_owner, repo_name)
    else:
        print("Usage: {} <repo_owner> <repo_name>".format(argv[0]))

