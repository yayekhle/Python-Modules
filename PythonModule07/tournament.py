from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy


def battle(opponents):
    print("\n*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):

            f1, s1 = opponents[i]
            f2, s2 = opponents[j]

            c1 = f1.create_base()
            c2 = f2.create_base()

            print("* Battle *")
            print(c1.describe())
            print("vs.\n")
            print(c2.describe())
            print("now fight!\n")

            try:
                s1.act(c1)
                s2.act(c2)
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                return

            print()


def main():
    battle([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ])

    battle([
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ])

    battle([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ])


if __name__ == "__main__":
    main()
