import requests
import git_client as git
import ai_assistant as ai
import file_helper as file_helper
import datetime
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
    pull_number = 6

    try:       
        pr_data = git.get_pull_request_data(token, owner, repo, pull_number)        
        changelog_content = ai.create_changelog(pr_data)
        
        file_name = f"CHANGELOG_PR{pull_number}_{datetime.datetime.now().timestamp()}.md"
        file_helper.create_file(file_name, changelog_content)

        # file_helper.create_file(file_name, "changelog_content")

    except Exception as e:
        print(f"Error: {e}")