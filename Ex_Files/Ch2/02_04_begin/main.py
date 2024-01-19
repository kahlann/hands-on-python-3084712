# Set some lists for names and ages
NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

# Set counter
i = 0
# While the counter is less than the number of items in the list
while i < len(NAMES):
    # Print the name and age of each person
    print(f"{NAMES[i]} is {AGES[i]} years old")
    # increment the counter
    i += 1

# Print each name in the names list - more concise way of doing the above while loop for the names only
for name in NAMES:
    print(name)

# Iterate through two lists at once using zip - efficient, does not create a new list in memory
for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

# Print the names in reverse order
for name in reversed(NAMES):
    print(name)

# print the numbers up to 5 - this does not create an object in memory for the range, efficient
# 0-indexed, so i will take the values 0 to 4 inclusive
for i in range(5):
    print(i)

# enumerate - get the index of iteration through the for loop
# 0-indexed
for i, name in enumerate(NAMES):
    print(f"Beatle {i}: {name}")
