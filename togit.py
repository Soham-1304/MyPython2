import os
import subprocess
from datetime import datetime

# Function to read code snippets from a text file
def read_code_snippets(file_path):
    with open(file_path, 'r') as file:
        code_snippets = file.read().split('\n\n')  # Assuming each code block is separated by two newlines
    return code_snippets

# Function to save each code snippet as a separate Python file
def save_code_snippets(snippets, output_folder, start_idx):
    file_paths = []
    for idx, snippet in enumerate(snippets[start_idx:], start=start_idx + 1):
        file_name = f"code_{idx}.py"  # Each code file will be named code_1.py, code_2.py, etc.
        file_path = os.path.join(output_folder, file_name)
        with open(file_path, 'w') as code_file:
            code_file.write(snippet)
        print(f"Saved: {file_name}")
        file_paths.append(file_name)
    return file_paths

# Function to push the files to GitHub
def git_push(file_paths, repo_path):
    # Navigate to the GitHub repository directory
    os.chdir(repo_path)

    # Stage the files for commit
    for file_path in file_paths:
        subprocess.run(["git", "add", file_path])

    # Commit the files with a timestamped message
    commit_message = f"Auto commit: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    subprocess.run(["git", "commit", "-m", commit_message])

    # Push the changes to the remote repository
    subprocess.run(["git", "push"])

# Function to read the last pushed code index from a file
def read_last_pushed_index(last_pushed_file):
    if os.path.exists(last_pushed_file):
        with open(last_pushed_file, 'r') as file:
            return int(file.read().strip())
    return 0  # Default to 0 if the file doesn't exist

# Function to update the last pushed code index
def update_last_pushed_index(last_pushed_file, index):
    with open(last_pushed_file, 'w') as file:
        file.write(str(index))

if __name__ == "__main__":
    # Define the path to the file containing code snippets (inside 'gitcodes' folder)
    codes_file_path = '/Users/sohamkarandikar/Documents/gitcodess/generated_python_codes.txt'  # Update with the actual path

    # Define the path to the GitHub repository (inside 'gitreview' folder)
    repo_path = './gitreview'  # Update with the actual path to your repo

    # Folder in the repo where the code files will be saved
    output_folder = repo_path  # Save directly in the repo root folder, or adjust as needed

    # Define the path to the file that stores the index of the last pushed code
    last_pushed_file = './lastpushed.txt'  # Update with the actual path

    # Read the code snippets from the file
    code_snippets = read_code_snippets(codes_file_path)
    print(f"Number of snippets read: {len(code_snippets)}")

    # Read the last pushed index from the file
    last_pushed_index = read_last_pushed_index(last_pushed_file)

    # Save the new code snippets as separate Python files, starting from the next one
    file_paths = save_code_snippets(code_snippets, output_folder, last_pushed_index)

    # Push the files to the repository
    if file_paths:
        git_push(file_paths, repo_path)
        print("Code files pushed to GitHub repository!")

        # Update the last pushed index
        update_last_pushed_index(last_pushed_file, last_pushed_index + len(file_paths))
    else:
        print("No new code snippets to push.")



