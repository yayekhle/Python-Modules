class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow_one_day(self) -> None:
        self.height += 1
        self.age += 1

    def get_info(self) -> None:
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(rose.get_info())
    start__height = rose.height
    for i in range(6):
        rose.grow_one_day()

    print("=== Day 7 ===")
    print(rose.get_info())
    print("Growth this week: +" + str(rose.height - start__height) + "cm")
