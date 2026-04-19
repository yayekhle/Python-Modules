from ex0 import FlameFactory, AquaFactory


def test_factory(factory):
    print("Testing factory")

    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())

    print(evolved.describe())
    print(evolved.attack())
    print()


def main():
    test_factory(FlameFactory())
    test_factory(AquaFactory())


if __name__ == "__main__":
    main()
