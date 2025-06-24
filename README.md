# get-github-repo-list

A simple Python script to fetch all your GitHub repositories using the GitHub API and save their details to a CSV file.

## Features

- Fetches all repositories for the authenticated user
- Saves repository details such as:
  - Name
  - Description
  - URL
  - Created At
  - Updated At
  - Language
  - Forks Count
  - Stars Count
- Output is saved as `repos_list.csv`

## Requirements

- Python 3.x
- `requests` library

## Setup

1. **Clone this repository:**
   ```sh
   git clone https://github.com/ajiteveryone8/get-github-repo-list
   cd get-github-repo-list
   ```

2. **Install dependencies:**
   ```sh
   pip install requests
   ```

3. **Set your GitHub credentials as environment variables:**
   ```sh
   set GITHUB_TOKEN=your_github_token
   set GITHUB_USERNAME=your_github_username
   ```

   > On Linux/macOS, use `export` instead of `set`.

4. **Run the script:**
   ```sh
   python app.py
   ```

5. **Check the output:**  
   The repository details will be saved in `repos_list.csv`.
   

## Example GitHub Repo List CSV

```csv
Repository Name,Description,URL,Created At,Updated At,Language,Forks Count,Stars Count
my-awesome-project,An awesome project for demo purposes,https://github.com/example/my-awesome-project,2024-01-01T10:00:00Z,2024-06-01T12:00:00Z,Python,5,42
weather-dashboard,A dashboard to display weather data,https://github.com/example/weather-dashboard,2023-11-15T09:30:00Z,2024-05-20T08:45:00Z,JavaScript,2,17
ml-models,Machine learning models for various tasks,https://github.com/example/ml-models,2022-07-10T14:20:00Z,2024-04-10T16:10:00Z,Jupyter Notebook,8,101
portfolio-site,Personal portfolio website,https://github.com/example/portfolio-site,2023-03-05T11:00:00Z,2024-03-10T13:00:00Z,HTML,1,7
data-cleaner,Tool for cleaning and preprocessing data,https://github.com/example/data-cleaner,2024-02-20T15:00:00Z,2024-06-15T10:00:00Z,Python,0,3
```

## License

This project is licensed under the MIT License.

