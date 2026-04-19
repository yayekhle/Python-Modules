import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename: str = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        f = open(filename, "r")
        print("---\n")
        content = f.read()
        print(content)
        print("\n---")
        f.close()
        print(f"File '{filename}' closed.")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    main()
