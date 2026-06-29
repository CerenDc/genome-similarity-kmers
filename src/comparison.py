from pathlib import Path

from Bio import SeqIO

from .kmers import extract_kmers
from .metrics import jaccard_similarity, mash_distance


def read_fasta_sequence(file_path: Path) -> str:
    for record in SeqIO.parse(file_path, "fasta"):
        return str(record.seq)

    raise ValueError(f"No sequence found in {file_path}")


def compare(
    file1: Path,
    file2: Path,
    k_values: list[int],
    shift_values: list[int],
) -> list[dict[str, float | int]]:
    seq1 = read_fasta_sequence(file1)
    seq2 = read_fasta_sequence(file2)

    results = []

    for k in k_values:
        for shift in shift_values:
            kmers1 = extract_kmers(seq1, k, shift)
            kmers2 = extract_kmers(seq2, k, shift)

            jaccard = jaccard_similarity(kmers1, kmers2)
            mash = mash_distance(jaccard, k)

            results.append(
                {
                    "k": k,
                    "shift": shift,
                    "jaccard": jaccard,
                    "mash_distance": mash,
                }
            )

    return results
