import os
import requests
import time
from datetime import datetime

class AutoCommentBot:
    def __init__(self, token, repo_owner, repo_name):
        self.token = token
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        self.processed_issues = set()
    
    def get_issues(self, state="open"):
        """Fetch all issues from the repository"""
        url = f"{self.base_url}/issues"
        params = {"state": state}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
    
    def add_comment(self, issue_number, comment_text):
        """Add a comment to a specific issue"""
        url = f"{self.base_url}/issues/{issue_number}/comments"
        data = {"body": comment_text}
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()
    
    def monitor_and_comment(self, interval=60, comment_text="Thank you for your contribution!"):
        """Continuously monitor for new issues and add comments"""
        print(f"Starting auto-comment bot for {self.repo_owner}/{self.repo_name}")
        print(f"Checking for new issues every {interval} seconds...")
        print("Press Ctrl+C to stop\n")
        
        try:
            while True:
                issues = self.get_issues()
                
                for issue in issues:
                    issue_number = issue['number']
                    
                    if issue_number not in self.processed_issues:
                        print(f"New issue #{issue_number} detected: '{issue['title']}'")
                        
                        try:
                            self.add_comment(issue_number, comment_text)
                            print(f"Added comment to issue #{issue_number}")
                            self.processed_issues.add(issue_number)
                        except Exception as e:
                            print(f"Error commenting on issue #{issue_number}: {e}")
                
                time.sleep(interval)
                
        except KeyboardInterrupt:
            print("\nBot stopped by user")

def main():
    # Configuration
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "your_github_token_here")
    REPO_OWNER = "PaintingProgrammer"  # Replace with your GitHub username
    REPO_NAME = "auto-comment-bot-x"    # Replace with your repository name
    
    # Initialize the bot
    bot = AutoCommentBot(GITHUB_TOKEN, REPO_OWNER, REPO_NAME)
    
    # Single use: Comment on all existing open issues
    print("Commenting on existing open issues...")
    issues = bot.get_issues()
    for issue in issues:
        issue_number = issue['number']
        print(f"Processing issue #{issue_number}: '{issue['title']}'")
        try:
            bot.add_comment(issue_number, "Thank you for your contribution!")
            print(f"Successfully commented on issue #{issue_number}")
        except Exception as e:
            print(f"Error: {e}")
    
    print("\nDone! For continuous monitoring, run: auto_comment_bot.py")

if __name__ == "__main__":
    main()