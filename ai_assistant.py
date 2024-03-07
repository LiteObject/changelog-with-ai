from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

def create_changelog(pr_data: str) -> str:

    # gets API Key from environment variable OPENAI_API_KEY
    client = OpenAI()
    client.api_key = os.environ["OPENAI_API_KEY"] 

    # Create the prompt for the OpenAI API
    # prompt = f"Create a CHANGELOG.md file based on the following pull request data:\n\n{pr_data}"

    # Call the OpenAI API to generate the CHANGELOG.md content    
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to write software changelog."},
            {"role": "user", "content": f"Create a CHANGELOG.md file based on the following pull request data:\n\n{pr_data}"}
        ]
    )

    # Extract the generated CHANGELOG.md content
    changelog_content = response.choices[0].message.content

    # Save the CHANGELOG.md file
    with open("CHANGELOG.md", "w", encoding="utf-8") as file:
        file.write(changelog_content)

    print("CHANGELOG.md file created successfully!")
    return changelog_content