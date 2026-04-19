import sys


def main() -> None:

    print("=== Command Quest ===")
    print("Program name:", sys.argv[0])

    argc = len(sys.argv)

    if argc == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {argc - 1}")
        for i in range(1, argc):
            print(f"Argument {i}:", sys.argv[i])

    print("Total arguments:", argc)


if __name__ == "__main__":
    main()
