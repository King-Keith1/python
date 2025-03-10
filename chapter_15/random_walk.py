# from random import choice

# class RandomWalk:
#     """A class to generate random walks."""

#     def __init__(self, num_points=5000):
#         self.num_points = num_points
#         self.x_values = [0]
#         self.y_values = [0]

#     def get_step(self):
#         """Determine the direction and distance for a step."""
#         direction = choice([1, -1])
#         distance = choice([0, 1, 2, 3, 4])
#         return direction * distance

#     def fill_walk(self):
#         """Calculate all the points in the walk."""
#         while len(self.x_values) < self.num_points:
#             x_step = self.get_step()
#             y_step = self.get_step()

#             if x_step == 0 and y_step == 0:
#                 continue

#             self.x_values.append(self.x_values[-1] + x_step)
#             self.y_values.append(self.y_values[-1] + y_step)


# 15.4
# from random import choice

# class RandomWalk:

#     def __init__(self, num_points=5000):
#         self.num_points = num_points
#         self.x_values = [0]
#         self.y_values = [0]

#     def get_step(self): # modified
#         direction = choice([1])  # Only moves in one direction
#         distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8]) # Extended distance choices
#         return direction * distance

#     def fill_walk(self):
#         while len(self.x_values) < self.num_points:
#             x_step = self.get_step()
#             y_step = self.get_step()

#             if x_step == 0 and y_step == 0:
#                 continue

#             self.x_values.append(self.x_values[-1] + x_step)
#             self.y_values.append(self.y_values[-1] + y_step)
            
15.5

from random import choice

class RandomWalk:

    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()  
            y_step = self.get_step()  

            if x_step == 0 and y_step == 0:
                continue

            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)
            
            
            
            