# armor.py

import random


class Armor:
    """Represents a hero's armor."""

    def __init__(self, name, max_block):
        """
        Instance properties:
            name (str)
            max_block (int)
        """
        self.name = name
        self.max_block = max_block

    def block(self):
        """
        Return a random block value between
        0 and max_block.
        """
        return random.randint(0, self.max_block)


# -----------------------------------------
# Testing
# -----------------------------------------

if __name__ == "__main__":

    shield = Armor("Captain's Shield", 40)

    print("Armor:", shield.name)
    print("Max Block:", shield.max_block)

    print("\nRandom Blocks:")

    for i in range(5):
        print(shield.block())