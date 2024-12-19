# Comparative Analysis of SARS-COV2 and SARS-TOR2 Genomes Using K-mer Based Metrics #genome-comparison-sars-cov2-sars-tor2
 
## Overview

This project involves a comparative analysis of the SARS-COV2 and SARS-TOR2 genomes using k-mer based metrics, including the Jaccard index and Mash distance. The analysis helps in understanding the genomic similarities and differences between these two viruses by calculating pairwise distances between their k-mer sets.

## Table of Contents

- [Introduction](#introduction)
- [Methodology](#methodology)
  - [Indexing k-mers](#indexing-k-mers)
  - [Computing the Jaccard Index](#computing-the-jaccard-index)
  - [Computing Mash Distance](#computing-mash-distance)
  - [Comparison](#comparison)
- [Results](#results)
- [Conclusion](#conclusion)
- [Discussion](#discussion)
- [Dependencies](#dependencies)
- [Usage](#usage)

## Introduction

This project compares the genomes of SARS-COV2 and SARS-TOR2 using two main k-mer based metrics: the Jaccard index and Mash distance. The analysis uses Python and several libraries for genomic sequence processing and distance calculations.

## Methodology

### Indexing k-mers
The first step is to index the k-mers from both genomes. A k-mer is a substring of length `k` extracted from the genome sequence. We use a Python function to extract all k-mers, storing them in a dictionary to ensure all k-mers are unique.

### Computing the Jaccard Index
The Jaccard index is calculated to measure the similarity between two sets of k-mers. The formula for the Jaccard index is:

```
J(A, B) = |A ∩ B| / |A ∪ B|
```

Where:
- `A` and `B` are the sets of k-mers extracted from the two genomes.
- The function `jaccard_similarity` computes this index for each combination of k-mer sizes and shifts.

### Computing Mash Distance
Mash distance is derived from the Jaccard index. It quantifies the genomic distance between two sets of k-mers. If the Jaccard index is zero, the Mash distance is set to infinity. Otherwise, it is computed as:

```
Mash Distance = -log(1 - J(A, B))
```

### Comparison
We perform comparisons using different values of `k` (k-mer sizes) and shift values (how much to slide the window when extracting k-mers). The results are stored and visualized to observe how these parameters affect the similarity measurements.

## Results

The results provide a detailed table of Jaccard indices and Mash distances for various combinations of k and shift. Key observations include:

- Mash distance at k=7 is lower, indicating high similarity between genomes.
- Mash distance becomes infinite for k=111 and k=121 with shift 2, where the genomes are highly dissimilar.

### Visualization
A graph is provided that plots Mash distances for both shift values against various k values, highlighting the effects of the k-mer size and shift on similarity.

## Conclusion

Our findings show that shorter k-mers result in greater genomic similarity, while longer k-mers provide more nuanced differences. The shift parameter also plays a crucial role in determining the density of k-mers and the resulting similarity measurements.

## Discussion

Future work could involve comparing these results with pairwise sequence alignments performed using algorithms like Needleman-Wunsch on the JobDispatcher platform. This would provide further validation and highlight the strengths and weaknesses of the k-mer based methods versus traditional sequence alignment approaches.

## Dependencies

This project requires the following Python libraries:

- **BioPython**: For genomic sequence handling.
- **Matplotlib**: For visualizations.
- **Math**: For mathematical computations.

To install the required dependencies, run:

```
pip install biopython matplotlib
```

## Usage

1. **Clone the repository**:
   ```
   git clone https://github.com/your-username/Comparative-Analysis-SARS-COV2-SARS-TOR2.git
   ```

2. **Run the script to perform the analysis**:
   ```
   python genome_comparison.py
   ```

3. **View the results** in the console or as output files (e.g., graphs).
