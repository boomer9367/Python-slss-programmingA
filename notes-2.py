# Methods
# Author: Justin L
# # Heavily based on ubial's code
# 6 October

# Ask the user what the weather is like
weather = input("What's the weather like right now?")

if weather.lower().strip("!,.?") == "rainy":
    # "RAINY!"
    print("You should bring an umbrella.")
elif weather.lower().strip("!.,?") == "sunny":
    # "SUNNY" "sunny!" "sunny."
    print("You should bring sunscreen.")
else:
    print("I see...")

# Ask the customer if they want fries
fries_reply = input("Do you want fries?")
#   "yes!"
#   "Yes!"
if "yes" in fries_reply.lower():
    print("Here are your fries.")
else:
    print("OK, you will not have fries.")
