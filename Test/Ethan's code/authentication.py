def my_login(user_profile):
    # """Handles user login with retry attempts."""
    max_attempts = 3  # Allow the user 3 attempts to log in
    attempts = 0

    while attempts < max_attempts:
        username_attempt = input("Enter your username: ")
        password_attempt = input("Enter your password: ")

        if username_attempt == user_profile["username"] and password_attempt == user_profile["password"]:
            print(f"Welcome, {user_profile['firstname']}!")
            return
        else:
            attempts += 1
            print("Incorrect username or password. Please try again.")
    
    print("Too many failed login attempts. Access denied.")