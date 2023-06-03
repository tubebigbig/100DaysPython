from array_slice import fruit

my_fruit = ["watermelon", "orange"]


def main():
    fruit.append("fig")
    print(f"fruit after append 'fig':\n{fruit}\n")

    fruit.insert(0, "badapple")
    print(f"fruit after insert 'badapple':\n{fruit}\n")

    fruit.remove("badapple")
    print(f"fruit after remove 'badapple':\n{fruit}\n")

    qoo = fruit.pop()
    print(f"fruit after pop:\n{fruit}\n")
    print(f"pop item qoo:\n{qoo}\n")

    fruit.extend(my_fruit)
    print(f"fruit after extend my_fruit:\n{fruit}\n")

    fruit.reverse()
    print(f"fruit after reverse:\n{fruit}\n")

    fruit.sort()
    print(f"fruit after sort:\n{fruit}\n")


if __name__ == "__main__":
    main()
