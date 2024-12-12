import requests

# Replace with your details
TRAVIS_API_URL = "https://api.travis-ci.com/repo/sdfsdfsdwe12%2Ftest/requests"
TRAVIS_TOKEN = "dbLr8qyH7iLgKz9vo0uQ0A"

headers = {
    "Travis-API-Version": "3",
    "Authorization": f"token {TRAVIS_TOKEN}"
}

data = {
    "request": {
        "branch": "main"
    }
}

try:
    response = requests.post(TRAVIS_API_URL, json=data, headers=headers)
    if response.status_code == 202:
        print("Build triggered successfully!")
    else:
        print(f"Failed to trigger build: {response.status_code} - {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
