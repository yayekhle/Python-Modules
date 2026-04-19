from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main():
    print("Testing Creature with healing capability")

    factory = HealingCreatureFactory()

    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())

    print("\nTesting Creature with transform capability")

    factory = TransformCreatureFactory()

    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    main()
