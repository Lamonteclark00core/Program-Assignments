# arena.py

from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team


class Arena:

    def __init__(self):
        """Create the two teams."""
        self.team_one = Team("Team One")
        self.team_two = Team("Team Two")

    def create_ability(self):
        """Create an Ability from user input."""
        name = input("Ability name: ")
        max_damage = int(input("Maximum damage: "))
        return Ability(name, max_damage)

    def create_weapon(self):
        """Create a Weapon from user input."""
        name = input("Weapon name: ")
        max_damage = int(input("Maximum weapon damage: "))
        return Weapon(name, max_damage)

    def create_armor(self):
        """Create Armor from user input."""
        name = input("Armor name: ")
        max_block = int(input("Maximum block: "))
        return Armor(name, max_block)

    def create_hero(self):
        """Create one hero."""

        hero_name = input("\nHero name: ")
        hero = Hero(hero_name)

        while True:

            print("\n1 - Add Ability")
            print("2 - Add Weapon")
            print("3 - Add Armor")
            print("4 - Done")

            choice = input("Choice: ")

            if choice == "1":
                hero.add_ability(self.create_ability())

            elif choice == "2":
                hero.add_weapon(self.create_weapon())

            elif choice == "3":
                hero.add_armor(self.create_armor())

            elif choice == "4":
                break

            else:
                print("Invalid choice.")

        return hero

    def build_team_one(self):
        """Build Team One."""

        number = int(input("\nHow many heroes on Team One? "))

        for i in range(number):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        """Build Team Two."""

        number = int(input("\nHow many heroes on Team Two? "))

        for i in range(number):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        """Battle the two teams."""

        print("\n==========================")
        print("      TEAM BATTLE!")
        print("==========================\n")

        self.team_one.attack(self.team_two)

    def show_stats(self):
        """Display battle statistics."""

        print("\n==============================")
        print("FINAL RESULTS")
        print("==============================")

        self.team_one.stats()
        print()
        self.team_two.stats()

        print("\nSurvivors")

        print("\nTeam One:")

        for hero in self.team_one.heroes:
            if hero.is_alive():
                print(hero.name)

        print("\nTeam Two:")

        for hero in self.team_two.heroes:
            if hero.is_alive():
                print(hero.name)

        team1_alive = sum(hero.is_alive() for hero in self.team_one.heroes)
        team2_alive = sum(hero.is_alive() for hero in self.team_two.heroes)

        print()

        if team1_alive > team2_alive:
            print("🏆 Team One Wins!")
        elif team2_alive > team1_alive:
            print("🏆 Team Two Wins!")
        else:
            print("It's a draw!")

    def play_game(self):
        """Run the simulator."""

        print("===================================")
        print(" SUPERHERO BATTLE SIMULATOR")
        print("===================================")

        self.build_team_one()
        self.build_team_two()

        self.team_battle()

        self.show_stats()


# -----------------------------------
# Run the Game
# -----------------------------------

if __name__ == "__main__":

    arena = Arena()

    arena.play_game()