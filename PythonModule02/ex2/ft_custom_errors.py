class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(plant_name: str) -> None:
    raise PlantError(f"The {plant_name} plant is wilting!")


def check_water_tank(level: int) -> None:
    if level < 10:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("\nTesting PlantError...")
    try:
        check_plant("tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        check_water_tank(5)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    errors = [PlantError("The tomato plant is wilting!"),
              WaterError("Not enough water in the tank!")]
    for err in errors:
        try:
            raise err
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_custom_errors()
