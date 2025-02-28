# Store user profile
user_profile = {}

# Function to create a user account
def create_account(**profile):
    global user_profile
    user_profile = profile  # Store the user profile
    return user_profile  # Return it explicitly