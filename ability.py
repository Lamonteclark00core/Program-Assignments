# ability.py

import random


class Ability:
    """Represents a hero's special ability."""

    def __init__(self, name, max_damage):
        """
        Instance properties:
            name (str)
            max_damage (int)
        """
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        """
        Return a random attack value between
        0 and max_damage.
        """
        return random.randint(0, self.max_damage)


# -----------------------------------------
# Testing
# -----------------------------------------

if __name__ == "__main__":

    fireball = Ability("Fireball", 50)

    print("Ability:", fireball.name)
    print("Max Damage:", fireball.max_damage)

    print("\nRandom Attacks:")

    for i in range(5):
        print(fireball.attack())