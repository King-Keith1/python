import matplotlib.pyplot as plt
from die import Die

die_1 = Die(8)
die_2 = Die(8)

multiplication_rolls = [die_1.roll() * die_2.roll() for _ in range(1000)]

plt.hist(multiplication_rolls, bins=range(1, 65), edgecolor='black', align='left')
plt.title('Product of Two D8 Dice Rolls (1000 Rolls) through multiplication')
plt.xlabel('Product of Dice')
plt.ylabel('Frequency')
plt.xticks(range(1, 65, 4))
plt.show()
