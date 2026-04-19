import sys
import os
import site


def is_virtual_environment() -> bool:
    return sys.prefix != sys.base_prefix


def show_global_info():
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")

    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate   # On Windows")


def show_venv_info():
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}\n")

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")

    try:
        paths = site.getsitepackages()
        print("Package installation path:")
        for path in paths:
            print(path)
    except Exception:
        print("Could not determine site-packages location.")


def main():
    if is_virtual_environment():
        show_venv_info()
    else:
        show_global_info()


if __name__ == "__main__":
    main()
