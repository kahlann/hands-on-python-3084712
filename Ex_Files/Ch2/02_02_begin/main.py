# Set some basic strings
greet = "Hello World"
name = "John"

# Concatenate strings
extened_grt = "Hello World, " + "this is a long string"

# f-string (format in-place)
intrupution = f"Hello {name}"

# string to be formatted using the format method
greet_format = "Hello {}"
formatted = greet_format.format(name)

# print both formatted strings - should be identical
print(intrupution, formatted)

# Print one of these strings in upper case
print(formatted.upper())

# Print one of these strings in lower case
print(formatted.lower())

# Replace the name in the string using replace method, print the new string
print(formatted.replace("John", "Kahlan"))
