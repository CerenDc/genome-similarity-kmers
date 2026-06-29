def extract_kmers(sequence: str, k: int, shift: int) -> dict[str, bool]:
    """Return the unique k-mers observed in a sequence for a given shift."""
    kmers: dict[str, bool] = {}

    for i in range(0, len(sequence) - k + 1, shift):
        kmers[sequence[i:i + k]] = True

    return kmers
