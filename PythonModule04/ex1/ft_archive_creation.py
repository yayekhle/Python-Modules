import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename: str = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        f = open(filename, "r")
        print("---\n")
        content: str = f.read()
        print(content)
        print("\n---")
        f.close()
        print(f"File '{filename}' closed.\n")

        print("Transform data:")
        print("---\n")

        new_lines: list[str] = []
        for line in content.splitlines():
            new_line: str = line + "#\n"
            new_lines.append(new_line)
            print(new_line, end="")

        print("\n---")
        new_file: str = input("Enter new file name (or empty): ")

        if new_file == "":
            print("Not saving data.")
            return

        print(f"Saving data to '{new_file}'")
        f = open(new_file, "w")
        f.writelines(new_lines)
        f.close()
        print(f"Data saved in file '{new_file}'.")

    except Exception as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    main()
