import secreate

def replace_value_in_file(file_path, old_value, new_value):
    with open(file_path, 'r') as file:
        # Read the contents of the file
        file_contents = file.read()

        # Replace the old value with the new value
        modified_contents = file_contents.replace(old_value, new_value)

    with open(file_path, 'w') as file:
        # Write the modified contents back to the file
        file.write(modified_contents)

DID = 'DeploymentID'
PWD = 'Password'

replace_value_in_file('parameters.json', PWD, secreate.replace1)
replace_value_in_file('parameters.json', DID, secreate.replace2)
replace_value_in_file('deploybicep.ps1', DID, secreate.replace2)
replace_value_in_file('replace.py', PWD, secreate.PWD)
replace_value_in_file('replace.py', DID, secreate.DID)