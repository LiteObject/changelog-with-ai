import requests

def get_commit_messages(token: str, owner: str, repo: str, pull_number: int) -> list[str]:
        
    # https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#list-commits-on-a-pull-request
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/commits"
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

def read_pull_request_description(token: str, owner: str, repo: str, pull_number: int) -> str:
   
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
     
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}"
    response = requests.get(url, headers=headers)
    data = response.json()
    
    description = ""

    if response.status_code == 200:        
        description = data["body"]
    else:
        print(f"Status Code: {response.status_code}, Error: {data}")

    return description

def get_pull_request_changes(token: str, owner: str, repo: str, pull_number: int) -> str:
    
   # GET /repos/{owner}/{repo}/pulls/{pull_number}/files    
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/files"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None

    data = response.json()    

    return data

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
