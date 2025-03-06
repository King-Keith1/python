def my_login(user_profile):
    """Handles user login by verifying credentials."""
    logged_in = False

    while not logged_in:
        print("Please Login:")    

        un = input("What is your Username: ")
        pw = input("What is your Password: ")

        if un == user_profile["username"] and pw == user_profile["password"]:
            logged_in = True
            print(f"Here is your master , Welcome back:\n{user_profile}")
        else:
            print("Are you a scammer🤔, why would you get your stuff wrong. HUH!")
