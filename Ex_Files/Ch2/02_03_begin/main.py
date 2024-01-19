# Set lists to hold names and ages
NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

# Acces the first name, assign to the variable JOHN
JOHN = NAMES[0]
# Access the first age, assign to the variable PAUL
PAUL = NAMES[1]

# Slice strings [start:end:step]
# Get the names to the left of position 2
JOHN_PAUL = NAMES[:2]
# Get the names at position 2 and to the right of position 2
GEORGE_RINGO = NAMES[2:]
# Reverse the string by taking negative steps
REVERSE = NAMES[::-1]
# Get every other name by taking a step of 2
EVERY_OTHER = NAMES[::2]

# Get some stats on the ages
print("Sum of the ages: {}".format(sum(AGES)))
print("Minimum age: {}".format(min(AGES)))
print("Maximum age: {}".format(max(AGES)))

# Print the sliced lists
print(JOHN_PAUL)
print(GEORGE_RINGO)
print(REVERSE)
