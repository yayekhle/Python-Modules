import sys
import importlib


def check_package(name, label):
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__")
        print(f"[OK] {name} ({version}) - {label}")
        return module
    except ImportError:
        print(f"[MISSING] {name} - Install it")
        return None


def main() -> None:
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")

    pandas = check_package("pandas", "Data manipulation ready")
    numpy = check_package("numpy", "Numerical computation ready")
    requests = check_package("requests", "Network access ready")
    matplotlib = check_package("matplotlib", "Visualization ready")

    if not all([numpy, pandas, requests, matplotlib]):
        print("\nInstall missing packages with:")
        print("pip install -r requirements.txt")
        print("or")
        print("poetry install")
        sys.exit(1)

    print("\nAnalyzing Matrix data...")

    data = numpy.random.rand(1000)

    import matplotlib.pyplot as plt
    plt.plot(data)
    plt.title("Matrix Data Stream")
    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Generating visualization...")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
