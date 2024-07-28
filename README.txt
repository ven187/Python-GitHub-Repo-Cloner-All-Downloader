# GitHub Repo Cloner

This script allows you to clone all repositories of a specified GitHub user into a directory on your local machine.

## Prerequisites

- Python 3.x
- `requests` library (install using `pip install requests`)
- Git

## Usage

1. Clone this repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script with the desired GitHub username.

### Example

```bash
python main.py
```

### Script Details
The script performs the following steps:

Get Repositories: Fetches the list of all repositories for a given GitHub username.
Create Directory: Creates a directory named after the GitHub username in the current working directory.
Clone Repositories: Clones each repository into the created directory.
