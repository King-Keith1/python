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

# class Restaurant:
    
#     def __init__(self, restaurant_name, cuisine_name):
#         self.restaurant_name = restaurant_name
#         self.cuisine_name = cuisine_name
        
#     def open_restaurant(self):
#         print(f"The automatic doors open for {kitchen.restaurant_name}")
    
#     def describe_restaurant(self):
#         print(f"Your eyes adjust to the surroundings you notice a HUGE american flag set as the centre piece and the smell of cooked prime meat everywhere. This is {kitchen.cuisine_name}")
    
# kitchen = Restaurant("Pierre's kitchen", "American-styled steakhouse")

# kitchen.open_restaurant()
# kitchen.describe_restaurant()

# class Person:
#     def __init__(self, name, age, team):  #
#         self.name = name
#         self.age = age
#         self.team = team

#     def greet(self):
#         return f"Hello, {self.name} here! Nice to meet you ✌🏽!"

#     def how_old_are_you(self):
#         return f"WOW, you're old! You're {self.age} years old."

#     def team_name(self, new_team):
#         old_team = self.team
#         self.team = new_team  
#         return f"{self.name} has switched from {old_team} to {new_team}."

# # Example usage
# person1 = Person("Pierre", 18, "404 Avengers")  

# print(person1.greet())  
# print(person1.how_old_are_you())  
# print(person1.team_name("Stack overflow"))
# print(person1.team_name("Function Junction"))   
# print(f"Current Team: {person1.team}")  

class Car:
 
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles