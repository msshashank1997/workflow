import string
import random
import requests
import base64

def replace_value_on_github(repo_owner, repo_name, file_path, old_value, new_value, access_token):
    # Get the current content of the file from GitHub
    headers = {
        "Authorization": f"token {access_token}"
    }
    response = requests.get(f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}", headers=headers)
    
    if response.status_code == 200:
        response_json = response.json()

        # Decode the content from base64
        try:
            content = base64.b64decode(response_json['content']).decode()
        except KeyError:
            print("Error: 'content' field not found in the API response. Make sure the file exists.")
            return

    # Replace the old value with the new value
    updated_content = content.replace(old_value, new_value)

    # Encode the updated content to base64
    updated_content_bytes = updated_content.encode()
    updated_content_base64 = base64.b64encode(updated_content_bytes).decode()

    # Update the file on GitHub
    data = {
        "message": "Replace value in file",
        "content": updated_content_base64,
        "sha": response_json['sha']
    }
    response = requests.put(f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}", json=data, headers=headers)
    if response.status_code == 200:
        print("File updated successfully!")
    else:
        print("Failed to update the file.")


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


if __name__ == "__main__":
    repo_owner = "msshashank1997"
    repo_name = "workflow"
    repo_owner = "msshashank1997"
    file_path1 = "powershell_scripts/replace.py"  # Replace with the actual path of the file you want to modify
    file_path2 = "powershell_scripts/parameters.json"
    file_path3 = "powershell_scripts/deploybicep.ps1"
    access_token = "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"
    
    # Replacing the Value of UPA and Password in bpa
    replace_value_on_github(repo_owner, repo_name,file_path2, replace1, pwd, access_token)
    replace_value_on_github(repo_owner, repo_name,file_path2, replace2, DepID, access_token)
    replace_value_on_github(repo_owner, repo_name,file_path3, replace2, DepID, access_token)
    replace_value_on_github(repo_owner, repo_name,file_path1, DID, DepID, access_token)
    replace_value_on_github(repo_owner, repo_name,file_path1, PWD, pwd, access_token)