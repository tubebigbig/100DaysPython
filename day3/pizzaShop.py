from enum import Enum


class SIZE(Enum):
    S = 1
    M = 2
    L = 3


class CONDITINO(Enum):
    Y = "Y"
    N = "N"


def calculate_bill(size: SIZE, add_pepperoni: CONDITINO, extra_cheese: CONDITINO):
    total_price = 0
    if size == SIZE.S:
        total_price += 15
    elif size == SIZE.M:
        total_price += 20
    elif size == SIZE.L:
        total_price += 25
    else:
        print("Invalid size")
        return

    if add_pepperoni == CONDITINO.Y:
        total_price += size == SIZE.S and 2 or 3

    if extra_cheese == CONDITINO.Y:
        total_price += 1

    return total_price


def welcome_message():
    print("Welcome to Python Pizza Deliveries!")
    print("Small Pizza: $15")
    print("Medium Pizza: $20")
    print("Large Pizza: $25")
    print("")
    print("Pepperoni for Small Pizza: +$2")
    print("Pepperoni for Medium or Large Pizza: +$3")
    print("")
    print("Extra cheese for any size pizza: + $1")
    print("")
    return


def main():
    welcome_message()
    size: SIZE
    add_pepperoni: CONDITINO
    extra_cheese: CONDITINO

    while True:
        _size = input("What size pizza do you want? S, M, or L: ").upper()
        if _size in ["S", "M", "L"]:
            size = SIZE[_size]
            break
        print("Invalid size")
        print("")
    while True:
        _add_pepperoni = input("Do you want pepperoni? Y or N: ").upper()
        if _add_pepperoni in ["Y", "N"]:
            add_pepperoni = CONDITINO[_add_pepperoni]
            break
        print("Invalid option")
        print("")
    while True:
        _extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
        if _extra_cheese in ["Y", "N"]:
            extra_cheese = CONDITINO[_extra_cheese]
            break
        print("Invalid option")
        print("")

    bill = calculate_bill(size, add_pepperoni, extra_cheese)
    print(f"Your final bill is: ${bill}")
    return


if __name__ == "__main__":
    main()
