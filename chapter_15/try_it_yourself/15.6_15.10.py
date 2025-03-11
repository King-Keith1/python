# 15.6
# import random
# import matplotlib.pyplot as plt


# # Simulate rolling two 8-sided dice 1,000 times
# rolls = [random.randint(1, 8) + random.randint(1, 8) for _ in range(1000)]

# # Plot the histogram
# plt.hist(rolls, bins=range(2, 18), edgecolor='black', align='left')
# plt.title('Sum of Two D8 Dice Rolls (1000 Rolls)')
# plt.xlabel('Sum of Dice')
# plt.ylabel('Frequency')
# plt.xticks(range(2, 17))
# plt.show()

15.7

# import random
# import matplotlib.pyplot as plt

# rolls_three_dice = [random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) for _ in range(1000)]

# # Plot the histogram
# plt.hist(rolls_three_dice, bins=range(3, 19), edgecolor='black', align='left')
# plt.title('Sum of Three D6 Dice Rolls (1000 Rolls)')
# plt.xlabel('Sum of Dice')
# plt.ylabel('Frequency')
# plt.xticks(range(3, 19))
# plt.show()

15.8

# import random
# import matplotlib.pyplot as plt

# multiplication_rolls = [random.randint(1, 8) * random.randint(1, 8) for _ in range(1000)]

# # Plot the histogram
# plt.hist(multiplication_rolls, bins=range(1, 65), edgecolor='black', align='left')
# plt.title('Product of Two D8 Dice Rolls (1000 Rolls)')
# plt.xlabel('Product of Dice')
# plt.ylabel('Frequency')
# plt.xticks(range(1, 65, 4))
# plt.show()

15.9

# import random
# import matplotlib.pyplot as plt

# # Simulate rolling two 8-sided dice 1,000 times using a traditional loop
# rolls = []
# for _ in range(1000):
#     roll = random.randint(1, 8) + random.randint(1, 8)
#     rolls.append(roll)

# # Plot the histogram
# plt.hist(rolls, bins=range(2, 18), edgecolor='black', align='left')
# plt.title('Sum of Two D8 Dice Rolls (1000 Rolls)')
# plt.xlabel('Sum of Dice')
# plt.ylabel('Frequency')
# plt.xticks(range(2, 17))
# plt.show()

15.10

# import plotly.graph_objects as go
# import random

# # Random walk
# steps = 1000
# walk = [0]
# for _ in range(steps):
#     walk.append(walk[-1] + random.choice([-1, 1]))

# # Create the plot
# fig = go.Figure(data=go.Scatter(x=list(range(steps + 1)), y=walk, mode='lines'))
# fig.update_layout(title='Random Walk Simulation',
#                   xaxis_title='Steps',
#                   yaxis_title='Position')
# fig.show()