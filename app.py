import requests
import csv
import os

# Get token and username from environment variables
token = os.getenv("GITHUB_TOKEN")
username = os.getenv("GITHUB_USERNAME")
if not token or not username:
    print("Please set the GITHUB_TOKEN and GITHUB_USERNAME environment variables.")
    exit(1)

url = "https://api.github.com/user/repos"

headers = {
    "Authorization": f"token {token}"
}

params = {
    "per_page": 100,  # Increase or paginate if you have more
    "visibility": "all"
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    repos = response.json()
    with open("repos_list.csv", "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([
            "Repository Name",
            "Description",
            "URL",
            "Created At",
            "Updated At",
            "Language",
            "Forks Count",
            "Stars Count"
        ])
        for repo in repos:
            writer.writerow([
                repo['name'],
                repo['description'] or "No description",
                repo['html_url'],
                repo['created_at'],
                repo['updated_at'],
                repo['language'] or "None",
                repo['forks_count'],
                repo['stargazers_count']
            ])

    print("Repository list saved to repos_list.csv")
else:
    print("Error:", response.status_code, response.text)