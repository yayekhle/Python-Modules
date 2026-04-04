import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    filename: str = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        f = open(filename, "r")
        print("---\n")
        lines: list[str] = f.readlines()
        for line in lines:
            print(line, end="")
        print("\n---")
        f.close()
        print(f"File '{filename}' closed.\n")

        print("Transform data:")
        print("---\n")

        new_lines: list[str] = []
        for line in lines:
            new_line = line.rstrip("\n") + "#\n"
            new_lines.append(new_line)
            print(new_line, end="")

        print("\n---")
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        new_file: str = sys.stdin.readline().strip()

        if new_file == "":
            print("Not saving data.")
            return

        print(f"Saving data to '{new_file}'")

        try:
            f = open(new_file, "w")
            for line in new_lines:
                f.write(line)
            f.close()
            print(f"Data saved in file '{new_file}'.")
        except Exception as e:
            sys.stderr.write(f"[STDERR] Error opening file'{new_file}': {e}\n")
            print("Data not saved.")

    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")


if __name__ == "__main__":
    main()
