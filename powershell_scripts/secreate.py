import string
import random
from github import Github

PAT = os.environ.get('MY_SECRET')

def generate_password(n):
    # Define the set of allowed characters
    allowed_chars = string.ascii_letters + string.digits + "!#$%^&*-"

    # Define the set of disallowed special characters
    disallowed_special_chars = "@()_=+[]|;:,.<>?~'"

    # Remove disallowed special characters from the allowed character set
    allowed_chars = ''.join(
        char for char in allowed_chars if char not in disallowed_special_chars)

    # Generate the password using the allowed character set
    password = ''.join(random.choice(allowed_chars) for _ in range(n))

    return password

repo_owner = "msshashank1997"
repo_name = "workflow"
file_path = "powershell_scripts/"  # Replace with the actual file path in the repository

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


replace1 = 'GEN-PASSWORD'
replace2 = 'DepID'

# Generate a password of length 12
n = 12
pwd = generate_password(n)
print(pwd)

d = 6
DepID = random.randint(int('1'+'0'*(d-1)), int('9'*d))
DepID = str(DepID)
print(DepID)

DID = 'DeploymentID'
PWD = 'Password'

g = Github(PAT)
repo = g.get_repo(f"{repo_owner}/{repo_name}")

# Replacing the Value of UPA and Password in bpa
replace_value_in_file(repo,'parameters.json', replace1, pwd)
replace_value_in_file(repo,'parameters.json', replace2, DepID)
replace_value_in_file(repo,'deploybicep.ps1', replace2, DepID)
replace_value_in_file(repo,'replace.py', DID, DepID)
replace_value_in_file(repo,'replace.py', PWD, pwd)