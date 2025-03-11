# 15.3

# import matplotlib.pyplot as plt
# from random_walk import RandomWalk

# # Generate a random walk
# rw = RandomWalk(5000)  # Reduce points from 50,000 to 5,000
# rw.fill_walk()

# # Set up the plot
# plt.style.use('classic')
# fig, ax = plt.subplots(figsize=(10, 6))
# ax.plot(rw.x_values, rw.y_values, linewidth=1)

# # Remove the axes for a cleaner look
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_visible(False)

# plt.show()


# 15.3 FIXED

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Generate a random walk
rw = RandomWalk(5000)  # Reduce points from 50,000 to 5,000
rw.fill_walk()

# Set up the plot
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the walk
ax.plot(rw.x_values, rw.y_values, linewidth=1)

# Highlight the start and end points using plot with marker styles
ax.plot(rw.x_values[0], rw.y_values[0], 'go', markersize=10, label="Start")  # Green start point
ax.plot(rw.x_values[-1], rw.y_values[-1], 'ro', markersize=10, label="End")  # Red end point

# Remove the axes for a cleaner look
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

# Show legend
ax.legend()

plt.show()