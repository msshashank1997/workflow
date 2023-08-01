import string
import random

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

# Replacing the Value of UPA and Password in bpa
replace_value_in_file(file_path2, replace1, pwd)
replace_value_in_file(file_path2, replace2, DepID)
replace_value_in_file(file_path3, replace2, DepID)
replace_value_in_file(file_path1, DID, DepID)
replace_value_in_file(file_path1, PWD, pwd)