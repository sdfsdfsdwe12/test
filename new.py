import requests

# Replace these with your values
TRAVIS_API_URL = "https://https://app.travis-ci.com/github/sdfsdfsdwe12/test/requests"
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

response = requests.post(TRAVIS_API_URL, json=data, headers=headers)

if response.status_code == 200:
    print("Build triggered successfully!")
else:
    print(f"Failed to trigger build: {response.status_code}")
