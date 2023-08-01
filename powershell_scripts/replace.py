import secreate

file_path1 = "powershell_scripts/replace.py"  # Replace with the actual path of the file you want to modify
file_path2 = "powershell_scripts/parameters.json"
file_path3 = "powershell_scripts/deploybicep.ps1"

def replace_value_in_file(file_path, old_value, new_value):
    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()    
    content = content.replace(old_value, new_value)

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

DID = 'DeploymentID'
PWD = 'Password'

replace_value_in_file(file_path2, PWD, secreate.replace1)
replace_value_in_file(file_path2, DID, secreate.replace2)
replace_value_in_file(file_path3, DID, secreate.replace2)
replace_value_in_file(file_path1, PWD, secreate.PWD)
replace_value_in_file(file_path1, DID, secreate.DID)