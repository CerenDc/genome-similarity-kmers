import math


def jaccard_similarity(kmers1: dict[str, bool], kmers2: dict[str, bool]) -> float:
    intersection = len(set(kmers1.keys()).intersection(set(kmers2.keys())))
    union = len(set(kmers1.keys()).union(set(kmers2.keys())))

    if union == 0:
        return 0

    return intersection / union


def mash_distance(jaccard: float, k: int) -> float:
    if jaccard == 0:
        return float("inf")

    return -1 / k * math.log(2 * jaccard / (1 + jaccard))
