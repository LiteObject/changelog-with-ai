import requests
import git_client as git
import os
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":

    token = os.environ.get("GITHUB_TOKEN")

    if not token:
        raise ValueError("GITHUB_TOKEN environment variable is not set")

    owner = "LiteObject"
    repo = "changelog-with-ai"
    pull_number = 3

    # Example usage
    # github_url = "https://github.com/LiteObject/changelog-with-ai/pull/2"
    # api_url = .convert_github_pr_url_to_api(github_url)

    # if api_url:
    #     print(f"Converted\n\"{github_url}\" to:\n\"{api_url}\"")
    # else:
    #     print("Invalid URL format")

    # print("\n")
    # pr_desc = git.read_pull_request_description(token, owner, repo, pull_number)
    # print(pr_desc)

    # print("\n")
    # commit_messages = git.get_commit_messages(token, owner, repo, pull_number)
    # print(commit_messages)

    files = git.get_pull_request_changes(token, owner, repo, pull_number)
    print(files)