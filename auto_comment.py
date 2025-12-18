import requests

def add_comment_to_issue(issue_number, comment_text):
    """
    Adds a comment to a specific issue in this repository.
    This function is intended to be used by a webhook or automation script.
    """
    # In a real GitHub Action, GITHUB_TOKEN would be used.
    # For this example, we simulate the logic.
    print(f"Adding comment to issue #{issue_number}: {comment_text}")
    # Logic to post comment to GitHub API would go here

if __name__ == "__main__":
    # Test logic
    add_comment_to_issue(1, "Thank you for your contribution!")
