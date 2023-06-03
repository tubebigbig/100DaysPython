import array
from random import randint
from enum import Enum


class ICON(Enum):
    BOX = "📦"
    ORANGE = "🍊"
    TREASURE = "💰"
    PLAYER = "🤠"


class main:
    TREASURE_POSITION = (0, 0)
    TREASURE_MAP = []
    IS_TREASURE = False

    def __init__(self, size=3):
        # 1. Create a 3x3 treasure map using a list:
        self.generate_map(size)
        # 2. Create a random position for the treasure within the map:
        self.TREASURE_POSITION = self.gen_random_position(size)
        # 3. print the treasure map to the console using a for loop
        self.print_map()
        print(f"Treasure position: {self.TREASURE_POSITION}")

    def gen_random_position(self, size):
        return randint(1, size), randint(1, size)

    def generate_map(self, size):
        for i in range(size):
            self.TREASURE_MAP.append([ICON.BOX.value] * size)

    def print_map(self):
        for row in self.TREASURE_MAP:
            print(row)

    def is_treasure(self, row, column):
        return (
            int(row) == self.TREASURE_POSITION[0]
            and int(column) == self.TREASURE_POSITION[1]
        )

    def update_map(self, row, column, is_treasure=True):
        self.TREASURE_MAP[int(row) - 1][int(column) - 1] = (
            ICON.TREASURE.value if is_treasure else ICON.ORANGE.value
        )

    def get_input(self):
        position = input("Where do you want to put the treasure? ex: 2,3:")
        row, column = position.split(",")
        return row, column

    def run(self):
        row, column = self.get_input()
        self.IS_TREASURE = self.is_treasure(row, column)
        self.update_map(row, column, self.IS_TREASURE)
        self.print_map()
        # if win print "You get a orange!" else print "YOU GET THE TREASURE!!!" and run again
        print(
            f"You get a orange!" if not self.IS_TREASURE else f"YOU GET THE TREASURE!!!"
        )
        if not self.IS_TREASURE:
            self.run()


if __name__ == "__main__":
    print("Welcome to Treasure Map!")
    size = int(input("Please input the size of the map: "))
    main(size).run()
