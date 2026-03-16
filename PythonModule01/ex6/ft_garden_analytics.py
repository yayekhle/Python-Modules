class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def info(self) -> str:
        return f"{self.name}: {self.height}cm"

    def score(self) -> int:
        return self.height


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def info(self) -> str:
        return (
            f"{self.name}: {self.height}cm, "
            f"{self.color} flowers (blooming)"
        )

    def score(self) -> int:
        return self.height + 10


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, pts: int) -> None:
        super().__init__(name, height, color)
        self.pts = pts

    def info(self) -> str:
        return f"{super().info()}, Prize points: {self.pts}"

    def score(self) -> int:
        return super().score() + self.pts * 2


class GardenManager:
    total_gardens = 0

    class GardenStats:
        @staticmethod
        def count(plants) -> int:
            return len(plants)

        @staticmethod
        def types(plants) -> tuple:
            return tuple(
                sum(isinstance(p, t) for p in plants)
                for t in (Plant, FloweringPlant, PrizeFlower)
            )

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        self.growth = 0
        GardenManager.total_gardens += 1

    def add(self, plant: Plant) -> None:
        print(f"Added {plant.name} to {self.owner}'s garden")
        self.plants.append(plant)

    def grow_all(self) -> None:
        print(f"\n{self.owner} is helping all plants grow...")
        for p in self.plants:
            p.grow()
            self.growth += 1

    def score(self) -> int:
        return sum(p.score() for p in self.plants)

    def report(self) -> None:
        r, f, pr = GardenManager.GardenStats.types(self.plants)
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            print(f"- {p.info()}")
        print(
            f"\nPlants added: {GardenManager.GardenStats.count(self.plants)}, "
            f"Total growth: {self.growth}cm"
        )
        print(f"Plant types: {r} regular, {f} flowering, {pr} prize flowers")

    @classmethod
    def network(cls, owners):
        return [cls(o) for o in owners]

    @staticmethod
    def valid_height(h: int) -> bool:
        return h >= 0


def main() -> None:
    print("=== Garden Management System Demo ===\n")
    alice, bob = GardenManager.network(["Alice", "Bob"])
    alice.add(Plant("Oak Tree", 100))
    alice.add(FloweringPlant("Rose", 25, "red"))
    alice.add(PrizeFlower("Sunflower", 50, "yellow", 10))
    bob.plants += [Plant("Pine", 70), FloweringPlant("Tulip", 12, "pink")]
    alice.grow_all()
    alice.report()
    print(f"\nHeight validation test: {GardenManager.valid_height(10)}")
    print(f"Garden scores - Alice: {alice.score()}, Bob: {bob.score()}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    main()
