import requests
import os
from dotenv import load_dotenv
load_dotenv() 

owner = "LiteObject"
repo = "changelog-with-ai"
token = os.environ.get("GITHUB_TOKEN")

def get_commit_messages(pull_request_id) -> list[str]:
        
    # https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#list-commits-on-a-pull-request
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_request_id}/commits"
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

def read_pull_request_description(github_api_url: str) -> str:
   
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
     
    response = requests.get(github_api_url, headers=headers)

    data = response.json()
    
    if response.status_code == 200:        
        description = data["body"]
    else:
        print(f"Status Code: {response.status_code}, Error: {data}")

    return description

def convert_github_pr_url_to_api(url):

  # Check if the URL is valid and has the expected format
  if not url.startswith("https://github.com/") or "/pull/" not in url:
    return None

  # Split the URL into parts
  parts = url.split("/")

  # Extract owner, repo, and pull number
  owner = parts[3]
  repo = parts[4]
  pull_number = parts[6]

  # Construct the API URL
  api_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}"

  return api_url


if __name__ == "__main__":
    pull_request_id = 1 #"YOUR_PULL_REQUEST_ID"

    # Example usage
    github_url = "https://github.com/LiteObject/changelog-with-ai/pull/2"
    api_url = convert_github_pr_url_to_api(github_url)

    if api_url:
        print(f"Converted\n\"{github_url}\" to:\n\"{api_url}\"")
    else:
        print("Invalid URL format")

    pr_desc = read_pull_request_description(api_url)
    print(pr_desc)

    # commit_messages = get_commit_messages(pull_request_id)
    # print(commit_messages)
    
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