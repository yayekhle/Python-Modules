def garden_operations(data: str):
    if data == "1":
        try:
            int("abc")
        except ValueError:
            print("\nTesting ValueError...")
            print("Caught ValueError: invalid literal for int()")
    elif data == "2":
        try:
            5 / 0
        except ZeroDivisionError:
            print("\nTesting ZeroDivisionError...")
            print("Caught ZeroDivisionError: division by zero")
    elif data == "3":
        try:
            open("Readme.md")
        except FileNotFoundError:
            print("Testing FileNotFoundError...")
            print("Caught FileNotFoundError: No such file 'Readme.txt'")
    elif data == "4":
        try:
            test = {}
            print(test["key"])
        except KeyError:
            print("Testing KeyError...")
            print("Caught KeyError: 'missing\\_plant'\n")
    elif data == "5":
        try:
            int("abc")
            2/0
            open("Readme.md")
            test = {}
            print(test["key"])
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            print("Testing multiple errors together...")
            print("Caught an error, but program continues!\n")


def test_error_types():

    print("=== Garden Error Types Demo ===")
    garden_operations("1")
    garden_operations("2")
    garden_operations("3")
    garden_operations("4")
    garden_operations("5")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
