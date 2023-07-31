import secreate
import os
from github import Github

repo_owner = "msshashank1997"
repo_name = 'workflow'
file_path = "powershell_scripts/"  # Replace with the actual file path in the repository

PAT = os.environ.get('MY_SECRET')
g = Github(PAT)
repo = g.get_repo(f"{repo_owner}/{repo_name}")

def replace_value_in_file(repo,file_path, old_value, new_value):
    with open(file_path, 'r') as file:
        # Read the contents of the file
        file_contents = contents.decoded_content.decode('utf-8')
    
    if old_value in file_content:
        file_content = file_content.replace(old_value, new_value)

        # Update the file in the repository
        repo.update_file(contents.path, f"Updated {file_path}", file_content, contents.sha)

    with open(file_path, 'w') as file:
        # Write the modified contents back to the file
        file.write(modified_contents)

DID = 'DeploymentID'
PWD = 'Password'

replace_value_in_file(repo,'parameters.json', PWD, secreate.replace1)
replace_value_in_file(repo,'parameters.json', DID, secreate.replace2)
replace_value_in_file(repo,'deploybicep.ps1', DID, secreate.replace2)
replace_value_in_file(repo,'replace.py', PWD, secreate.PWD)
replace_value_in_file(repo,'replace.py', DID, secreate.DID)