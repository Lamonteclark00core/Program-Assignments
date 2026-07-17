# weapon.py

import random
from ability import Ability


class Weapon(Ability):
    """
    A Weapon is a special type of Ability.
    It always deals between half and full damage.
    """

    def attack(self):
        """
        Return a random attack value between
        half of max_damage and max_damage.
        """
        half_damage = self.max_damage // 2
        return random.randint(half_damage, self.max_damage)


# -----------------------------------------
# Testing
# -----------------------------------------

if __name__ == "__main__":

    sword = Weapon("Excalibur", 80)

    print("Weapon:", sword.name)
    print("Max Damage:", sword.max_damage)

    print("\nRandom Weapon Attacks:")

    for i in range(5):
        print(sword.attack())