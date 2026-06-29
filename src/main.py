import csv
from pathlib import Path

from .comparison import compare
from .plots import plot_jaccard, plot_mash


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
FIGURES_DIR = PROJECT_ROOT / "figures"
RESULTS_DIR = PROJECT_ROOT / "results"
K_VALUES = [7, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121]
SHIFT_VALUES = [1, 2]


def write_results_csv(results, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["k", "shift", "jaccard", "mash_distance"],
        )
        writer.writeheader()
        writer.writerows(results)


def print_results(results) -> None:
    for row in results:
        print(
            f"k = {row['k']:<3} | "
            f"shift = {row['shift']:<2} | "
            f"Jaccard Index = {row['jaccard']:.4f} | "
            f"Mash Distance = {row['mash_distance']:.4f}"
        )


def main() -> None:
    results = compare(
        file1=DATA_DIR / "SARS_COV2.fna",
        file2=DATA_DIR / "SARS_TOR2.fna",
        k_values=K_VALUES,
        shift_values=SHIFT_VALUES,
    )

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    write_results_csv(results, RESULTS_DIR / "comparison_results.csv")
    plot_jaccard(
        results,
        output_path=FIGURES_DIR / "jaccard_similarity.png",
    )
    plot_mash(
        results,
        output_path=FIGURES_DIR / "mash_distance.png",
    )

    print_results(results)


if __name__ == "__main__":
    main()
