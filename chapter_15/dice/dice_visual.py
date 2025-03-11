from die import Die
# Create a D6.
die = Die(6)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(10):
    result = die.roll()
    results.append(result)
    print(results)