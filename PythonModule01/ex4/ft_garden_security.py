class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        if height < 0:
            self.__height = 0
        else:
            self.__height = height
        if age < 0:
            self.__age = age
        else:
            self.__age = age

    def set_height(self, height: int) -> None:
        if height >= 0:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print("Invalid operation attempted: height "
                  f"{height} cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self.__age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print("Invalid operation attempted: age", age, "[REJECTED]")

    def get_height(self) -> None:
        return self.__height

    def get_age(self):
        return self.__age

    def show_info(self) -> None:
        return f"{self.name} ({self.get_height()}cm, {self.get_age()} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 0, 0)
    print(f"Plant created: {plant.name}")
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-10)
    print(f"\nCurrent plant: Rose {plant.show_info()}")
