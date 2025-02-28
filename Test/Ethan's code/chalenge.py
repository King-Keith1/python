# MAIN CHALLENGE (all that is needed to solve the problem):
# Separate the following program into atleast 2 separate modules

# TIPS:
# A third module is possible in order to neaten your code even further.
# The more Python practices you utilize, the more points you get.
# You can neaten up one of the functions to make your code even more easy to manage.

# THE ZEN OF PYTHON:

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!


# main.py
from user_account import create_account
from authentication import my_login

def main():
    # Get user details and create an account
    user_profile = create_account(
        username=input("What would you like your username to be: "),
        password=input("What would you like your password to be: "),
        firstname=input("What is your first name: "),
        lastname=input("What is your last name: "),
        location=input("Where do you stay: ")
    )

    # Log the user in
    my_login(user_profile)

if __name__ == "__main__":
    main()