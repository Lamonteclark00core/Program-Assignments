# team.py

import random


class Team:
    """Represents a team of heroes."""

    def __init__(self, name):
        """
        Instance properties:
            name (str)
            heroes (list)
        """
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        """Add a hero to the team."""
        self.heroes.append(hero)

    def remove_hero(self, name):
        """Remove a hero from the team by name."""
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                break

    def view_all_heroes(self):
        """Display all heroes on the team."""
        print(f"\n{self.name} Heroes")
        print("-" * 25)

        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        """
        Battle this team against another team.
        """

        living_heroes = [hero for hero in self.heroes if hero.is_alive()]
        living_opponents = [hero for hero in other_team.heroes if hero.is_alive()]

        while living_heroes and living_opponents:

            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            hero.battle(opponent)

            living_heroes = [h for h in self.heroes if h.is_alive()]
            living_opponents = [h for h in other_team.heroes if h.is_alive()]

    def revive_heroes(self):
        """Restore every hero's health."""
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        """Print each hero's battle statistics."""
        print(f"\n{self.name} Statistics")
        print("-" * 30)

        for hero in self.heroes:
            print(
                f"{hero.name} | "
                f"Kills: {hero.kills} | "
                f"Deaths: {hero.deaths}"
            )


# -----------------------------------------
# Testing
# -----------------------------------------

if __name__ == "__main__":

    from hero import Hero

    team = Team("Avengers")

    hero1 = Hero("Iron Man")
    hero2 = Hero("Captain America")
    hero3 = Hero("Black Widow")

    team.add_hero(hero1)
    team.add_hero(hero2)
    team.add_hero(hero3)

    team.view_all_heroes()

    print("\nRemoving Black Widow...\n")

    team.remove_hero("Black Widow")

    team.view_all_heroes()