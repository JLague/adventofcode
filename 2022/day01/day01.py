import numpy as np

calories = [0]
i = 0

# Read input and get sum by elf
with open("input.txt") as f:
    for line in f:
        if line == '\n':
            calories.append(0)
            i += 1
            continue
        calories[i] += int(line)

# Create and sort array
arr = np.sort(np.array(calories))

# Print result
print(f"Max : {arr.max()}")
print(f"Sum top 3 : {arr[-3:].sum()}")