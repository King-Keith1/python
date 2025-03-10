# import matplotlib.pyplot as plt

# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]

# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=3,)

# # Set chart title and label axes.
# ax.set_title("Pierre Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# ax.set_facecolor("black")

# # Set size of tick labels.
# ax.tick_params(labelsize=14)

# plt.show()

# Ethan's code
# import matplotlib.pyplot as plt

# # Group members and their values (each one is 1 lower than the previous)
# members = ["Ethan", "Marvelous", "Pierre", "Ronny"]
# values = [70, 69, 68, 67]  # Descending order for cool effect

# # Convert members to numeric positions
# x_positions = range(len(members))

# # Create an even cooler line graph
# plt.figure(figsize=(10, 6))
# plt.plot(x_positions, values, marker="o", linestyle="-", color="#FF4500", linewidth=4, 
#          markersize=12, markerfacecolor="black", markeredgewidth=2, markeredgecolor="yellow")

# # Add title and labels with more dramatic styling
# plt.title("⚡ 404 Avengers - Power Levels ⚡", fontsize=20, fontweight="bold", color="purple")
# plt.xlabel("Members", fontsize=14, fontweight="bold", color="darkred")
# plt.ylabel("Score", fontsize=14, fontweight="bold", color="darkblue")

# # Set custom x-ticks to display member names
# plt.xticks(x_positions, members)

# # Add value labels with cooler styling
# for i, v in enumerate(values):
#     plt.text(i, v + 1, str(v), ha="center", fontsize=14, fontweight="bold", color="white",
#              bbox=dict(facecolor="blue", edgecolor="white", boxstyle="round,pad=0.5"))

# # Enhanced grid with neon-style glow
# plt.grid(axis="y", linestyle="--", alpha=0.3, color="cyan")

# # Dark background for a futuristic feel
# plt.gca().set_facecolor("#222222")

# # Show the graph
# plt.show()

# Marvelous's code
# import matplotlib.pyplot as plt

# # Group members and their contributions
# members = ["Ethan", "Marvelous", "Pierre", "Ronny"]
# contributions = [48, 46, 27, 22]  # Same values as the bar chart

# # Convert member names to numerical x-axis positions
# x_positions = range(len(members))

# # Create a visually appealing line graph
# plt.figure(figsize=(10, 6))
# plt.plot(x_positions, contributions, marker="o", linestyle="-", color="#FF4500", linewidth=4, 
#          markersize=12, markerfacecolor="black", markeredgewidth=2, markeredgecolor="yellow")

# # Add title and labels with dramatic styling
# plt.title("⚡ 404 Avengers - GitHub Contributions ⚡", fontsize=20, fontweight="bold", color="purple")
# plt.xlabel("Members", fontsize=14, fontweight="bold", color="darkred")
# plt.ylabel("Number of Contributions", fontsize=14, fontweight="bold", color="darkblue")

# # Set custom x-ticks to display member names
# plt.xticks(x_positions, members)

# # Add value labels with enhanced styling
# for i, v in enumerate(contributions):
#     plt.text(i, v + 1, str(v), ha="center", fontsize=14, fontweight="bold", color="white",
#              bbox=dict(facecolor="blue", edgecolor="white", boxstyle="round,pad=0.5"))

# # Enhanced grid with neon-style glow
# plt.grid(axis="y", linestyle="--", alpha=0.3, color="cyan")

# # Dark background for a futuristic feel
# plt.gca().set_facecolor("#222222")

# # Show the graph
# plt.show()

# import matplotlib.pyplot as plt

# # Group members and their contributions
# members = ["Pierre", "Ronny", "Marvelous", "Ethan"]
# contributions = [27, 22, 46, 48]
# colors = ["#ff6361", "#bc5090", "#58508d", "#ffa600"]  # Assign different colors

# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()
# ax.bar(members, contributions, color=colors)

# # Set chart title and labels
# ax.set_title("404 Avengers GitHub Contributions", fontsize=16)
# ax.set_xlabel("Members", fontsize=12)
# ax.set_ylabel("Number of Contributions", fontsize=12)
# ax.set_facecolor("black")  # Set background color

# # Display the chart
# plt.show()

# 15.1

# import matplotlib.pyplot as plt

# # Generate data
# x_small = list(range(1, 6))  # First five numbers
# y_small = [x**3 for x in x_small]

# x_large = list(range(1, 5001))  # First 5000 numbers
# y_large = [x**3 for x in x_large]

# # Plot first five cubic numbers
# plt.figure(figsize=(6, 4))
# plt.plot(x_small, y_small, 'bo-', label="First 5 Cubes")
# plt.xlabel("Number")
# plt.ylabel("Cube")
# plt.title("First Five Cubic Numbers")
# plt.legend()
# plt.grid(True)
# plt.show()

# # Plot first 5000 cubic numbers
# plt.figure(figsize=(10, 5))
# plt.plot(x_large, y_large, 'r-', label="First 5000 Cubes")
# plt.xlabel("Number")
# plt.ylabel("Cube")
# plt.title("First 5000 Cubic Numbers")
# plt.legend()
# plt.grid(True)
# plt.show()

15.2

import matplotlib.pyplot as plt
import numpy as np

# Generate data
x_small = np.arange(1, 6)  # First five numbers
y_small = x_small**3

x_large = np.arange(1, 5001)  # First 5000 numbers
y_large = x_large**3

# Plot first five cubic numbers with colormap
plt.figure(figsize=(6, 4))
plt.scatter(x_small, y_small, c=y_small, cmap='viridis', edgecolor='black', s=100)
plt.xlabel("Number")
plt.ylabel("Cube")
plt.title("First Five Cubic Numbers with Colormap")
plt.colorbar(label="Cube Value")  
plt.grid(True)
plt.show()

# Plot first 5000 cubic numbers with colormap
plt.figure(figsize=(10, 5))
plt.scatter(x_large, y_large, c=y_large, cmap='plasma', edgecolor='none', s=5)
plt.xlabel("Number")
plt.ylabel("Cube")
plt.title("First 5000 Cubic Numbers with Colormap")
plt.colorbar(label="Cube Value")  
plt.grid(True)
plt.show()


