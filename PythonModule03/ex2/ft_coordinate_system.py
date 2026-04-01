import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input("Enter new coordinates"
                           "as floats in format 'x,y,z': ")
        parts = user_input.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            x = float(parts[0])
            y = float(parts[1])
            z = float(parts[2])
            return (x, y, z)
        except ValueError:
            for i in parts:
                try:
                    float(i)
                except ValueError:
                    print(f"Error on parameter {i}: could not"
                          f" convert string to float: {i}")
                    break


def distance(p1: tuple[float, float, float],
             p2: tuple[float, float, float]) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def main() -> None:
    print("=== Game Coordinate System ===")

    print("\nGet a first set of coordinates")
    p1 = get_player_pos()
    x, y, z = p1

    print("Got a first tuple:", p1)
    print(f"It includes: X={x}, Y={y}, Z={z}")

    d1 = math.sqrt(p1[0]**2 + p1[1]**2 + p1[2]**2)
    print("Distance to center:", round(d1, 4))

    print("\nGet a second set of coordinates")
    p2 = get_player_pos()

    d2 = distance(p1, p2)
    print("Distance between the 2 sets of coordinates:", round(d2, 4))


if __name__ == "__main__":
    main()
