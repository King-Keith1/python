# def greet_user():
#  print("Hello!")
# greet_user()

# def fav_book(title):
#     print(f"My favourite book is {title}")

# fav_book("The 48 Laws of Power")
    
# my_name = input("May I have your name please")

# def my_function():
#     print(my_name)
   
# def name(user, age):
#     print(f"Welcome back {user}: It must be nice to be {age} years old")
# name(my_name, 18)     
    
# def get_formatted_name(first_name, last_name):
#  """Return a full name, neatly formatted."""
#  full_name = f"{first_name} {last_name}"
#  return full_name.title()
  
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# def my_lyf(first_name, wud , outside, college, year = 2025):
#     return f"Name's {first_name}, right now I'm doing the {wud}. We gotta be {outside}. I'm in {college}, doing my first year in {year}."

# personal_info = my_lyf("Pierre", "Doing the python", "inside", "code college", )

# print(personal_info)

# def truth_about_me(*stuff):
#     """Building a single-sentence output using a for loop"""
#     collected_stuff = []  # Create an empty list to store values

#     for what_abt_me in stuff:
#         collected_stuff.append(what_abt_me)  # Add each item to the list

#     # Join all collected items into one sentence
#     print(f"You serious bro, me too🫵: I'm also a {', '.join(collected_stuff)}!")

# truth_about_me("Foodie", "Pseudo_gamer", "Pseudo_otaku", "Wanna_be_skater")

# def test(*first, second):
#     print(f"these are my first arguments: {first}")
#     print(f"this aisre my other argument: {second}")

# test(1, 2, 3, 4, second = 5)

# def make_shirt(size="L", message="I have no talent, just hard work"):
#     print(f"Ordering a {size}-sized T-shirt that says: '{message}'. Hope this makes people question their life choices.")

# make_shirt()

# make_shirt("M", "Success is just failure with better PR.")

import post  # Ensure post.py is in the same directory

post.sandwiches("tomato", "cheese")
post.sandwiches("bacon", "sauce", "chips")
post.sandwiches("cheese", "polony", "egg", "russian")