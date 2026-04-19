def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    if not plant_name:
        raise ValueError("Plant name cannot be empty!\n")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)\n"
            )
    if sunlight_hours < 2:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too low (min 2)\n"
            )
    return f"Plant '{plant_name}' is healthy!\n"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")
    try:
        print("Testing good values...")
        print(check_plant_health("tomato", 5, 8))
    except ValueError as e:
        print(f"Error: {e}")
    try:
        print("Testing empty plant name...")
        print(check_plant_health("", 5, 8))
    except ValueError as e:
        print(f"Error: {e}")
    try:
        print("Testing bad water level...")
        print(check_plant_health("tomato", 15, 8))
    except ValueError as e:
        print(f"Error: {e}")
    try:
        print("Testing bad sunlight hours...")
        print(check_plant_health("tomato", 5, 0))
    except ValueError as e:
        print(f"Error: {e}")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
