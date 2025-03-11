import matplotlib.pyplot as plt
from die import Die

die_1 = Die(8)
die_2 = Die(8)

rolls = []
for _ in range(1000):
    roll = die_1.roll() + die_2.roll()
    rolls.append(roll)

plt.hist(rolls, bins=range(2, 18), edgecolor='black', align='left')
plt.title('Sum of Two D8 Dice Rolls (1000 Rolls)')
plt.xlabel('Sum of Dice')
plt.ylabel('Frequency')
plt.xticks(range(2, 17))
plt.show()