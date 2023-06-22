import git
import os
import datetime

def get_recently_edited_files(repo_path, num_files):
    repo = git.Repo(repo_path)
    today = datetime.datetime.now().date()
    commits = repo.iter_commits('main', max_count=num_files)

    for commit in commits:
        if commit.authored_datetime.date() == today:
            print(f"Commit: {commit.hexsha}")
            print(f"Author: {commit.author.name} <{commit.author.email}>")
            print(f"Date: {commit.authored_datetime}")
            print("Changes:")

            for item in commit.diff(None):
                if item.a_path:
                    if item.b_path:
                        # File modified
                        print(f"File: {item.b_path}")
                        print("Change Type: Modified")
                    else:
                        # File deleted
                        print(f"File: {item.a_path}")
                        print("Change Type: Deleted")
                elif item.b_path:
                    # File added
                    print(f"File: {item.b_path}")
                    print("Change Type: Added")
                
                print(f"Last Modified: {commit.authored_datetime}")
                print("-" * 50)

# Example usage
repo_path = ''
num_files = 5

get_recently_edited_files(repo_path, num_files)
