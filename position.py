"""
Suppose a list contains 20 integers generated randomly. Receive a number from the keyboard and report position of all occurrences of this number in the list.


"""

import random

# Step 1: Generate a list of 20 random integers between 1 and 10
random_list = [random.randint(1, 10) for _ in range(20)]
print("Random List:", random_list)

# Step 2: Receive a number from the keyboard
number = int(input("Enter a number to search for: "))

# Step 3: Find all occurrences of the number in the list
positions = [index for index, value in enumerate(random_list) if value == number]

# Step 4: Report the positions
if positions:
    print(f"The number {number} is found at positions: {positions}")
else:
    print(f"The number {number} is not found in the list.")
