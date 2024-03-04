import requests
import os
from dotenv import load_dotenv
load_dotenv() 


def get_commit_messages(pull_request_id):
    """
    Retrieves the commit messages for a given pull request ID.

    Parameters:
        pull_request_id (int): The ID of the pull request.

    Returns:
        A list of commit messages.
    """
    owner = "LiteObject"
    repo_name = "changelog-with-ai"
    token = os.environ.get("GITHUB_TOKEN")
    # https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#list-commits-on-a-pull-request
    url = f"https://api.github.com/repos/{owner}/{repo_name}/pulls/{pull_request_id}/commits"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    commits = response.json()

    commit_messages = []
    for commit in commits:
        # print(commit)
        commit_messages.append(commit["commit"]["message"])

    return commit_messages

if __name__ == "__main__":
    pull_request_id = 1 #"YOUR_PULL_REQUEST_ID"
    commit_messages = get_commit_messages(pull_request_id)
    print(commit_messages)
    
    # Example output:
    # ['Update README.md', 'Add more details', 'Fix bug']
    
    # To test it, you can replace YOUR_PULL_REQUEST_ID with a valid pull request ID.
    # For example, if the pull request ID is 123, you can replace it with "YOUR_PULL_REQUEST_ID/123".
    # This will retrieve the commit messages for the pull request with ID 123.
    # The token you use to access GitHub must be provided in the Authorization header.
    # You can replace "YOUR_GITHUB_TOKEN" with your actual GitHub token.
    # The Accept header specifies the format of the response.
    # In this case, it is set to "application/json" to indicate that the response is in JSON format.
    # The response is a list of dictionaries, where each dictionary represents a commit.