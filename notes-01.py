# Notes - Introduction
# 16 September
# Justin L
# # Heavily based on ubial's code


# Create an algorithm to solve a problem
# Problem: Create our own chatbot
#          MeGPT

# 1. Greet the user with a predetermined statement
greeting = "Hello! I am a chatbot."

# 1a. Print the greeting
print(greeting)

# 2. Introduce the bot
print("I am MeGPT.")
print("I'm not like the other chatbots.")
print("I'm completely deterministic.")

# 3. Wow the user with some maths
print("I bet you don't know what 8*8 is.")
print("I can do it.")
print(f"8*8 is actually {8 * 8}.")

print("What is pi squared?")
print("I'm smart and can do it.")
print(f"It is {3.141592653**2}.")

# 4. Get the name of the user and store it
user_name = input("So... what's your name? ")
print(f"It's nice to meet you, {user_name}.")

# ...

# 8. Try out branching
want_cookies = True
want_chips = True

if want_cookies and want_chips:
    print("You get both!")
else:
    print("You get none.")  # this will print
