class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def __str__(self) -> None:
        return (
            f"\n{self.name} (Flower): "
            f"{self.height}cm, {self.age} days")

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def __str__(self) -> None:
        return (
            f"\n{self.name} (Tree): {self.height}cm, "
            f"{self.age} days, {self.trunk_diameter}cm diameter"
        )

    def produce_shade(self) -> None:
        print(f"{self.name} provides "
              f"{self.trunk_diameter * 1.56:.0f} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def __str__(self) -> None:
        return (
            f"\n{self.name} (Vegetable): "
            f"{self.height}cm, {self.age} days, "
            f"{self.harvest_season} harvest"
        )


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 25, "yellow")
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 600, 2000, 40)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 30, 70, "autumn", "beta-carotene")
    print(rose)
    rose.bloom()

    print(oak)
    oak.produce_shade()

    print(tomato)
    print(f"{tomato.name} is rich in {tomato.nutritional_value}")
