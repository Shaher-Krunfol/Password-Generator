import random
import string
import os
import json

def generate_password(length=20):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def save_password(password, use):
    # Load existing passwords
    file_path = os.path.join(os.getcwd(), "passwords.json")
    
    try:
        with open(file_path, "r") as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}
    
    # Add the new password
    passwords[use] = password
    
    # Save back to the file
    with open(file_path, "w") as file:
        json.dump(passwords, file, indent=4)  # indent for readability
        
    print(f"Passwords saved to {file_path}")    

    
use = input("Enter the use of the password: ")
password = generate_password()
print(f"Generated password: {password}")

save_password(password, use)
print("Password saved successfully!")
