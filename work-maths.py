def main():
    pass


num1 = float(input("input frist number "))
num2 = float(input("input second number "))
operator = int(
    input(
        " for add press 1 for subtraction press 2 for multily press 3 for division press 4 "
    )
)
if operator == 1:
    print(num1 + num2)
if operator == 2:
    print(num1 - num2)
if operator == 3:
    print(num1 * num2)
if operator == 4:
    print(num1 / num2)
else:
    print("invalide please reinput")


def ave():
    pass


num1 = float(input("input frist number "))
num2 = float(input("input second number "))
num3 = float(input("input third number "))
num4 = float(input("input fourth number "))
num5 = float(input("input fifth number "))

print((num1 + num2 + num3 + num4 + num5) / 2)


def mcDo():
    total = 0
    print("Hello! How can i help you?")
    burger = input("Would you like a burger for $5? (Yes/No)\n")
    if burger.strip("!?.,").lower() == "yes":
        total = total + 5
    elif burger.strip("!?.,").lower() == "no":
        pass
    else:
        print("Please enter a valid input.")
        mcDo()
    fries = input("Would you like fries for $5? (Yes/No)\n")
    if fries.strip("!?.,").lower() == "yes":
        total = total + 3
    elif fries.strip("!?.,").lower() == "no":
        pass
    else:
        print("Please enter a valid input.")
        mcDo()
    total = round(total * 1.14, 2)
    print(f"Your total is ${total}.")
