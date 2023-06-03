import random

rock = """
    _______
---'   ____)
        (_____)
        (_____)
        (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
            _____)
            _____)
            _____)
---.__________)
"""

scissors = """
    _______
---'   ____)____
            _____)
        __________)
        (____)
---.__(___)
"""


def get_user_choice():
    choice = int(
        input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
    )
    if choice < 0 or choice > 2:
        print("You typed an invalid number, you lose!")
        return -1
    return choice


def get_computer_choice():
    choice = random.randint(0, 2)
    return choice


def print_choice(choice):
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    elif choice == 2:
        print(scissors)


def get_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    else:
        print("You lose!")


def main():
    user_choice = get_user_choice()
    if user_choice == -1:
        return
    print_choice(user_choice)
    computer_choice = get_computer_choice()
    print("Computer chose:")
    print_choice(computer_choice)
    get_result(user_choice, computer_choice)


if __name__ == "__main__":
    main()
