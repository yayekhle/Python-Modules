import random

ACHIEVEMENTS = [
        "Crafting Genius", "Strategist", "World Savior",
        "Speed Runner", "Survivor", "Master Explorer",
        "Treasure Hunter", "Unstoppable", "First Steps",
        "Collector Supreme", "Untouchable", "Sharp Mind",
        "Boss Slayer"
    ]


def gen_player_achievements():
    return set(random.sample(ACHIEVEMENTS, random.randint(3, 5)))


def main():
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print("Alice:", alice)
    print("Bob:", bob)
    print("Charlie:", charlie)
    print("Dylan:", dylan)

    all_ach = alice.union(bob, charlie, dylan)
    print("\nAll achievements:", all_ach)

    common = alice.intersection(bob, charlie, dylan)
    print("Common achievements:", common)

    print("\nOnly Alice:", alice.difference(bob.union(charlie, dylan)))
    print("Only Bob:", bob.difference(alice.union(charlie, dylan)))
    print("Only Charlie:", charlie.difference(alice.union(bob, dylan)))
    print("Only Dylan:", dylan.difference(alice.union(bob, charlie)))

    print("\nAlice is missing:", all_ach.difference(alice))
    print("Bob is missing:", all_ach.difference(bob))
    print("Charlie is missing:", all_ach.difference(charlie))
    print("Dylan is missing:", all_ach.difference(dylan))


if __name__ == "__main__":
    main()
