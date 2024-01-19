# If FALSE, indented code will not run
# If TRUE, indented code will run
RUN_INDENTED = True

message = "running unindented"

if RUN_INDENTED:
    message = "running indented"

print(message)


def my_function():
    greet = "Hello"
    return greet

print(my_function())
