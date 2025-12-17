import requests
import os

def add_comment_to_issue(issue_number, comment_body):
    """
    Adds a comment to a specific GitHub issue.
    This function requires a GITHUB_TOKEN environment variable with repo permissions.
    """
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print("Error: GITHUB_TOKEN environment variable not set.")
        return

    owner = "PaintingProgrammer"
    repo = "auto-comment-bot-x"
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "body": comment_body
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print(f"Successfully added comment to issue #{issue_number}.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to add comment: {e}")

if __name__ == "__main__":
    # Example usage for testing
    # This would typically be triggered by a webhook event
    print("This script is designed to be run via GitHub Actions or a webhook.")