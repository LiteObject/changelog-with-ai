import requests
import git_client as git
import ai_assistant as ai
import json
from pprint import pprint
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":  

    token = os.environ.get("GITHUB_TOKEN")

    if not token:
        raise ValueError("GITHUB_TOKEN environment variable is not set")

    owner = "LiteObject"
    repo = "changelog-with-ai"
    pull_number = 4

    try:
        # Example usage
        # github_url = "https://github.com/LiteObject/changelog-with-ai/pull/2"
        # api_url = .convert_github_pr_url_to_api(github_url)

        # if api_url:
        #     print(f"Converted\n\"{github_url}\" to:\n\"{api_url}\"")
        # else:
        #     print("Invalid URL format")

        # print("PR Description:".upper(), "\n")
        # pr_desc = git.read_pull_request_description(token, owner, repo, pull_number)
        # print(pr_desc, "\n")

        # print("Commit Messages:".upper(), "\n")
        # commit_messages = git.get_commit_messages(token, owner, repo, pull_number)
        # print(commit_messages, "\n")

        # commits = git.get_commits_for_day(token, owner, repo, "2024-03-06", 50)
        # print(commits, "\n\n\n")

        # file_changes = git.get_file_changes_for_day(token, owner, repo, '2024-02-05', 100)
        # print(file_changes)

        pr_data = git.get_pull_request_data(token, owner, repo, pull_number)
        print(pr_data)

        ai.create_changelog(pr_data)

        # print("Changes:".upper(), "\n")
        # files = git.get_pull_request_changes(token, owner, repo, pull_number)

        # for file in files:
        #     print(file, "\n")
        #     # print(json.dumps(file))
        #     # pprint(file, indent=4)
    except Exception as e:
        print(f"Error: {e}")