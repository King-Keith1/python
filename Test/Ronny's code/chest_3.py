from chest_1 import create_account  # Import create_account
from chest_1 import user_profile    # Import user_profile (but will stop using global)

# Function to log the user in
def my_login(user_profile):
    logged_in = False

    while not logged_in:  # Cleaner loop condition
        print("\nPlease Login:")

        un = input("What is your Username: ")
        pw = input("What is your Password: ")

        if un == user_profile["username"] and pw == user_profile["password"]:
            logged_in = True
            print(f"\nLogin successful! Here is your profile:\n{user_profile}")
        else:
            print("Incorrect username or password. Try again.")

# Call create_account and store the returned user_profile
user_profile = create_account(
    username = input("What would you like your username to be: "),
    password = input("What would you like your password to be: "), 
    firstname = input("What is your first name: "),
    lastname = input("What is your last name: "),
    location = input("Where do you stay: ")
)

# Pass the updated user_profile to my_login
my_login(user_profile)