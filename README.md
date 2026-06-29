# Genome Similarity with k-mers

This project compares two coronavirus genomes using an alignment-free k-mer
similarity workflow. It extracts unique k-mers from FASTA sequences, evaluates
their Jaccard similarity across multiple k values and shifts, and converts the
similarity scores into Mash-style distances.

The repository is organized as a small, reproducible Python bioinformatics
project suitable for a data science or computational biology portfolio.

## Project Structure

```text
.
├── data/
│   ├── SARS_COV2.fna
│   └── SARS_TOR2.fna
├── figures/
│   ├── jaccard_similarity.png
│   └── mash_distance.png
├── results/
│   └── comparison_results.csv
├── src/
│   ├── comparison.py
│   ├── kmers.py
│   ├── main.py
│   ├── metrics.py
│   └── plots.py
├── README.md
└── requirements.txt
```

## Method

The analysis keeps the original algorithm:

1. Read SARS-CoV-2 and SARS-CoV/Tor2 genomes from FASTA files.
2. Generate unique k-mer dictionaries for each genome.
3. Compute the Jaccard index between k-mer sets.
4. Estimate Mash distance from the Jaccard score.
5. Repeat for k values from 7 to 121 and shifts of 1 and 2.
6. Save the numerical results and plots.

## Outputs

Running the pipeline creates:

- `results/comparison_results.csv`: pairwise Jaccard and Mash distance values
- `figures/jaccard_similarity.png`: Jaccard similarity across k-mer sizes
- `figures/mash_distance.png`: Mash distance across k-mer sizes

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

Run the full analysis from the project root:

```bash
python -m src.main
```

The script uses project-root relative paths through `pathlib`, so it does not
depend on local absolute paths.

## Skills Demonstrated

- Bioinformatics sequence parsing with Biopython
- Alignment-free genome comparison
- k-mer based feature extraction
- Jaccard similarity and Mash distance calculation
- Reproducible Python project structure
- Automated result and figure generation
