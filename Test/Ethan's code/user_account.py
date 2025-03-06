def create_account(username, password, firstname, lastname, location):
    # """Creates and returns a user profile as a dictionary."""
 user_profile = {
        "username": username,
        "password": password,
        "firstname": firstname,
        "lastname": lastname,
        "location": location
    }

 print("Account created successfully!\n")
 return user_profile