# hero.py

import random
from ability import Ability
from armor import Armor


class Hero:
    """Represents a superhero."""

    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

        # Lists to hold abilities and armor
        self.abilities = []
        self.armors = []

        # Battle statistics
        self.kills = 0
        self.deaths = 0

    def add_ability(self, ability):
        """Add an Ability object to this hero."""
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        """Weapons are stored with abilities."""
        self.abilities.append(weapon)

    def add_armor(self, armor):
        """Add an Armor object to this hero."""
        self.armors.append(armor)

    def attack(self):
        """Return the total attack damage from all abilities."""
        total_damage = 0

        for ability in self.abilities:
            total_damage += ability.attack()

        return total_damage

    def defend(self):
        """Return the total block value from all armor."""
        total_block = 0

        for armor in self.armors:
            total_block += armor.block()

        return total_block

    def take_damage(self, damage):
        """Reduce health after armor blocks some damage."""
        blocked = self.defend()
        damage_taken = damage - blocked

        if damage_taken < 0:
            damage_taken = 0

        self.current_health -= damage_taken

    def is_alive(self):
        """Return True if hero still has health."""
        return self.current_health > 0

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self):
        self.deaths += 1

    def battle(self, opponent):
        """Battle another hero."""

        if len(self.abilities) == 0 or len(opponent.abilities) == 0:
            print("Draw")
            return

        print(f"\n{self.name} battles {opponent.name}!\n")

        while self.is_alive() and opponent.is_alive():

            opponent.take_damage(self.attack())

            if opponent.is_alive():
                self.take_damage(opponent.attack())

        if self.is_alive():
            print(f"{self.name} won!")
            self.add_kill(1)
            opponent.add_death()
        else:
            print(f"{opponent.name} won!")
            opponent.add_kill(1)
            self.add_death()


# -----------------------------------------
# Testing
# -----------------------------------------

if __name__ == "__main__":

    hero = Hero("Grace Hopper", 200)

    print(hero.name)
    print(hero.current_health)