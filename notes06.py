# Numbers and Operations
# Author: Ubial
# 5 November 2025

# Work with numbers and operations

# Create an algorithm to gather
# data to find the most popular
# bubble tea place around us

# Version 1
def vote_listed_choices():
    """Display all choices
    5 users vote for their choice
    Results will be printed"""
    CHOICES = [
        "A. Blenz",
        "B. Bubble Queen",
        "C. Sun Tea",
        "D. heytea",
        "E. CoCo",
        "F. Fresh T",
    ]

    # buckets to hold all votes
    blenz = 0
    bubble_queen = 0
    sun_tea = 0
    heytea = 0
    coco = 0
    fresh_t = 0
    spoiled_votes = 0

    # Show all the choices
    print("Vote for your favourite from the list. ")
    print("Give the letter of your choice.")
    for choice in CHOICES:
        print(choice)

    # Ask the user for their choice
    vote = input("Your vote: ").strip(",.?! ").lower()
    # Keep track of a tally
    if vote == "a":
        blenz = blenz + 1
    elif vote == "b":
        bubble_queen += 1
    elif vote == "c":
        sun_tea += 1
    elif vote == "d":
        heytea += 1
    elif vote == "e":
        coco += 1
    elif vote == "f":
        fresh_t += 1
    else:
        spoiled_votes += 1

    # Data analysis
    # Give the raw scores
    print("Voting Results ---")
    print(f"Blenz: {blenz} votes")
    print(f"Bubble Queen: {bubble_queen} votes")
    print(f"Sun Tea: {sun_tea} votes")
    print(f"hey tea: {heytea} votes")
    print(f"CoCo: {coco} votes")
    print(f"Fresh T: {fresh_t} votes")
    print(f"Spoiled votes: {spoiled_votes} votes")
    # Give scores as a percentage
    print("Vote share percentage ---")
    total = blenz + bubble_queen + sun_tea + heytea + coco + fresh_t + spoiled_votes
    print(f"Blenz: {blenz / total * 100} %")
    print(f"Bubble Queen: {bubble_queen / total * 100} %")
    print(f"Sun Tea: {sun_tea / total * 100} %")
    print(f"hey tea: {heytea / total * 100} %")
    print(f"CoCo: {coco / total * 100} %")
    print(f"Fresh T: {fresh_t / total * 100} %")
    print(f"Spoiled votes: {spoiled_votes / total * 100} votes")


# Version 2
# Ask the user to give their
# favourite bubble tea place
# Keep track of a tally
# Data analysis
# Give the raw scores
# Give scores as a percentage


def chip_rater():
    """help gather data about chip crispness and quality"""
    questions = [
        "how crispy is the chip? out of 5 where 0 is muchy and 5 is super cripsy."
    ]


def main():
    vote_listed_choices()


if __name__ == "__main__":
    main()
