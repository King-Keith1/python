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

import matplotlib.pyplot as plt

# Group members and their contributions
members = ["Pierre", "Ronny", "Marvelous", "Ethan"]
contributions = [27, 22, 46, 48]
colors = ["#ff6361", "#bc5090", "#58508d", "#ffa600"]  # Assign different colors

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.bar(members, contributions, color=colors)

# Set chart title and labels
ax.set_title("404 Avengers GitHub Contributions", fontsize=16)
ax.set_xlabel("Members", fontsize=12)
ax.set_ylabel("Number of Contributions", fontsize=12)
ax.set_facecolor("black")  # Set background color

# Display the chart
plt.show()


