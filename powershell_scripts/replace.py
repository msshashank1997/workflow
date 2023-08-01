import secreate
import requests

def replace_value_on_github(repo_owner, repo_name, file_path, old_value, new_value, access_token):
    # Get the current content of the file from GitHub
    headers = {
        "Authorization": f"token {access_token}"
    }
    response = requests.get(f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}", headers=headers)
    response_json = response.json()

    # Decode the content from base64
    import base64
    content = base64.b64decode(response_json['content']).decode()

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

    replace_value_on_github(repo_owner, repo_name,file_path2, PWD, secreate.replace1, access_token)
    replace_value_on_github(repo_owner, repo_name,file_path2, DID, secreate.replace2, access_token)
    replace_value_on_github(repo_owner, repo_name,file_path3, DID, secreate.replace2, access_token)
    replace_value_on_github(repo_owner, repo_name,file_path1, PWD, secreate.PWD, access_token)
    replace_value_on_github(repo_owner, repo_name,file_path1, DID, secreate.DID, access_token)