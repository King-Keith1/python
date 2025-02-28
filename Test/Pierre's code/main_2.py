def create_account(username, password, firstname, lastname, location):
    """Creates and returns a user profile with the provided details."""
    return {
        "username": username,
        "password": password,
        "firstname": firstname,
        "lastname": lastname,
        "location": location
    }