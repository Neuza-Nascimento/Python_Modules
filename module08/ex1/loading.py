from importlib.metadata import version, PackageNotFoundError


packages: list[tuple[str, str]] = [("pandas", "Data manipulation ready"),
                                   ("numpy", "Numerical computation ready"),
                                   ("matplotlib", "Visualization ready")]


def check_dependencies() -> bool:
    isPackage = True
    for package, description in packages:
        try:
            print(f"[OK] {package} ({version(package)}) - {description}")
        except (PackageNotFoundError):
            print(f"{package} is missing")
            isPackage = False
    return isPackage


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    if check_dependencies():
        import matplotlib.pyplot as plt
        import numpy as np
        import pandas as pd
        print("Analyzing Matrix data...")
        data = np.random.randn(250, 4)
        colunas: list[str] = ["Veronique", "Gabriel", "Felyppe", "Neuza"]
        print("Processing 1000 data points...")
        df = pd.DataFrame(data=data, columns=colunas)
        de_sum = df.cumsum()
        print("Generating visualization..")
        plt.figure(figsize=(10, 6))
        plt.plot(de_sum["Neuza"], label="Neuza", color="blue")
        plt.plot(de_sum["Felyppe"], label="Felyppe", color="green")
        plt.plot(de_sum["Gabriel"], label="Gabriel", color="orange")
        plt.plot(de_sum["Veronique"], label="Veronique", color="pink")
        plt.title("Matrix data", fontsize=14)
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.legend()
        plt.savefig(" matrix_analysis.png", dpi=100)
        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")
    else:
        print("\nTo install missing dependencies use:")
        print("For pip:")
        print(" 'pip install -r requirements.txt'")
        print("For Proety:")
        print(" poetry install'")
        print(" poetry run python loading.py'")


if __name__ == "__main__":
    main()
