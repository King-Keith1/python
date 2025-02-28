# class Dog:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def sit(self):
#         print(f"{self.name} is now sitting.")

#     # def roll_over(self):
#     # print(f"{self.name} rolled over!")
    
# my_dog = Dog("Willie", 6)
# your_dog = Dog("Lucy", 3)

# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")

# print(f"\nYour dog's name is {your_dog.name}.")
# print(f"Your dog is {your_dog.age} years old.")

class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_name):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name
        
    def open_restaurant(self):
        print(f"The automatic doors open for {kitchen.restaurant_name}")
    
    def describe_restaurant(self):
        print(f"Your eyes adjust to the surroundings you notice a HUGE american flag set as the centre piece and the smell of cooked prime meat everywhere. This is {kitchen.cuisine_name}")
    
kitchen = Restaurant("Pierre's kitchen", "American-styled steakhouse")

kitchen.open_restaurant()
kitchen.describe_restaurant()