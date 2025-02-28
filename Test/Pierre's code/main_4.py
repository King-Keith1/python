from main_2 import create_account
from main_3 import my_login

# Create an account
user_profile = create_account(
    username=input("What would you like your username to be: "),
    password=input("What would you like your password to be: "),
    firstname=input("What is your first name: "),
    lastname=input("What is your last name: "),
    location=input("Where do you stay: ")
)

# Call the login function
my_login(user_profile)