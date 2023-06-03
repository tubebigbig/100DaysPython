fruit = ["apple", "banana", "cherry", "durian", "elderberry"]


def main():
    print(fruit[0])
    print(fruit[1])
    print(fruit[2])
    print(fruit[-1])
    print(fruit[-2])
    print(fruit[-3])
    # slice
    # [start:stop]
    print(fruit[1:3])
    print(fruit[:2])
    print(fruit[1:])
    print(fruit[:])
    # step
    # [start:stop:step]
    print(fruit[::2])
    print(fruit[::-1])
    print(fruit[1:3:2])
    print(fruit[1:4:-1])
    print(fruit[3:1:-1])


if __name__ == "__main__":
    main()
