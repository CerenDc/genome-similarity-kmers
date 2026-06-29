import math
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = PROJECT_ROOT / ".cache"
os.environ.setdefault("MPLCONFIGDIR", str(CACHE_DIR / "matplotlib"))
os.environ.setdefault("XDG_CACHE_HOME", str(CACHE_DIR))

import matplotlib.pyplot as plt


def _replace_inf(values: list[float]) -> list[float | None]:
    return [None if math.isinf(value) else value for value in values]


def _values_for_shift(results, metric, shift):
    return [row[metric] for row in results if row["shift"] == shift]


def plot_jaccard(results, output_path: Path | None = None, show: bool = False) -> None:
    k_values = sorted(set(row["k"] for row in results))
    jaccard_shift1 = _values_for_shift(results, "jaccard", 1)
    jaccard_shift2 = _values_for_shift(results, "jaccard", 2)

    plt.figure(figsize=(10, 5))
    plt.plot(
        k_values,
        jaccard_shift1,
        marker="o",
        label="Jaccard Index - Shift = 1",
        color="#00BFFF",
    )
    plt.plot(
        k_values,
        jaccard_shift2,
        marker="o",
        label="Jaccard Index - Shift = 2",
        color="#1E90FF",
    )
    plt.title("Jaccard Index by k-mer size")
    plt.xlabel("k-mer size")
    plt.ylabel("Jaccard Index")
    plt.grid(True)
    plt.legend()

    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, dpi=300, bbox_inches="tight")

    if show:
        plt.show()

    plt.close()


def plot_mash(results, output_path: Path | None = None, show: bool = False) -> None:
    k_values = sorted(set(row["k"] for row in results))
    mash_shift1 = _replace_inf(_values_for_shift(results, "mash_distance", 1))
    mash_shift2 = _replace_inf(_values_for_shift(results, "mash_distance", 2))

    plt.figure(figsize=(10, 5))
    plt.plot(
        k_values,
        mash_shift1,
        marker="o",
        label="Mash Distance - Shift = 1",
        color="#FF8C00",
    )
    plt.plot(
        k_values,
        mash_shift2,
        marker="o",
        label="Mash Distance - Shift = 2",
        color="#FFD700",
    )
    plt.title("Mash Distance by k-mer size")
    plt.xlabel("k-mer size")
    plt.ylabel("Mash Distance")
    plt.grid(True)
    plt.legend()

    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, dpi=300, bbox_inches="tight")

    if show:
        plt.show()

    plt.close()
