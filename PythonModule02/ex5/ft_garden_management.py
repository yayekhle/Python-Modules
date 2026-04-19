class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:

    def __init__(self) -> None:
        self.plants: dict[str, dict[str, int]] = {}

    def add_plant(self, name: str, water: int, sun: int) -> None:
        if not name:
            raise PlantError("Plant name cannot be empty!")
        self.plants[name] = {"water": water, "sun": sun}
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plant_health(self) -> None:
        for plant, stats in self.plants.items():
            try:
                if stats["water"] > 10:
                    raise ValueError(
                        f"Water level {stats['water']} is too high (max 10)\n"
                    )
                if stats["sun"] < 2:
                    raise ValueError(
                        f"Sunlight hours {stats['sun']} is too low (min 2)"
                    )
                print(f"{plant}: healthy (water:",
                      f"{stats['water']}, sun: {stats['sun']})")
            except ValueError as e:
                print(f"Error checking {plant}: {e}")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    manager = GardenManager()
    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato", 5, 8)
        manager.add_plant("lettuce", 15, 8)
        manager.add_plant("", 5, 8)
    except GardenError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    manager.water_plants()

    print("Checking plant health...")
    manager.check_plant_health()

    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
