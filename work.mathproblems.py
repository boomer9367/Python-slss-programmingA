# Solutions
# Author: Justin L
# Heavily based on ubial's code
# 17 November


def age_in_2049():
    cur_age = int(input("How old are you? "))
    print(f"In 2049, you will be {2049 - 2025 + cur_age} years old!")


def olympic_judging(num_judges: int):
    total = 0

    for n in range(num_judges):
        cur_score = float(input(f"Judge {n + 1}: "))

        total += cur_score

    print(f"Your Olympic score: is {total / num_judges}")


def mcdolands(tax: float):
    """
    Params:
        tax - tax as a percentage e.g. 14% -> 14"""
    burger = input("Would you like a burger for $5? (Yes/No)\n").lower().strip(",.?! ")
    fries = input("Would you like fries for $3? (Yes/No)\n").lower().strip(",.?! ")

    total = 0

    if burger == "yes":
        total += 5 * (1 + tax / 100)
    if fries == "yes":
        total += 3 * (1 + tax / 100)

    print(f"Your total is ${round(total, 2):.2f}")


def main():
    age_in_2049()
    olympic_judging(5)
    mcdolands(14)


if __name__ == "__main__":
    main()
