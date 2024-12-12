import time
import requests
import base64
import os

TOKEN = "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"  # Use an environment variable for the token
REPO = "username/repo"  # Replace with your repository
FILE_PATH = ".travis.yml"
BRANCH = "main"

HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_file_sha():
    """Get the SHA of the file to modify."""
    url = f"https://api.github.com/repos/{REPO}/contents/{FILE_PATH}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()["sha"]

def get_file_content():
    """Fetch the base64-encoded content of the file."""
    url = f"https://api.github.com/repos/{REPO}/contents/{FILE_PATH}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()["content"]

def update_file(new_content, sha):
    """Update the file content in the repository."""
    url = f"https://api.github.com/repos/{REPO}/contents/{FILE_PATH}"
    data = {
        "message": "Add space to the end of the file",
        "content": new_content,
        "sha": sha,
        "branch": BRANCH
    }
    response = requests.put(url, json=data, headers=HEADERS)
    response.raise_for_status()

def main():
    while True:
        try:
            print("Fetching file details...")
            sha = get_file_sha()
            current_content = get_file_content()

            decoded_content = base64.b64decode(current_content).decode("utf-8")
            updated_content = decoded_content + " "
            encoded_content = base64.b64encode(updated_content.encode("utf-8")).decode("utf-8")

            # Update the file
            update_file(encoded_content, sha)
            print("Successfully added a space to the file.")

        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        print("Sleeping for 30 minutes...")
        time.sleep(1800)

if __name__ == "__main__":
    if not TOKEN:
        print("Error: GitHub token not found. Set the GITHUB_TOKEN environment variable.")
    else:
        main()
