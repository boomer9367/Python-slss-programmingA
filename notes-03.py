# Functions
# Author: Justin L
# # Heavily based on ubial's code
# 8 October

# function to print "hello"
def say_hello():
    print("hello")


# function to print a personalized hello
def say_hello_nicely(name: str):
    print(f"hello {name}!")


def normalize_input(user_input: str):
    """Takes user input and cleans it up."""
    output = user_input.lower().strip(",.?! ")
    return output


def normalized_input():
    """Takes user input and cleans it up."""
    output = input().lower().strip(",.?! ")
    return output


def some_fun():
    print("hello!")


def some_fun_return() -> str:
    print("hello!")
    return "hello!"


return_val = some_fun_return()
print(return_val)
