# Genome Similarity Analysis Using K-mer Based Metrics

> Comparative analysis of SARS-CoV-2 and SARS-TOR2 genomes using **k-mer decomposition**, **Jaccard similarity**, and **Mash distance**.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![BioPython](https://img.shields.io/badge/BioPython-Latest-green)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## Project Overview

Genome comparison is a fundamental task in computational biology. Traditional sequence alignment algorithms provide accurate results but can become computationally expensive when comparing large genomic datasets.

This project explores an **alignment-free approach** based on **k-mer decomposition** to evaluate genomic similarity between **SARS-CoV-2** and **SARS-TOR2**.

The comparison relies on two widely used similarity metrics:

- **Jaccard Similarity**
- **Mash Distance**

Different **k-mer sizes** and **window shifts** are evaluated to study their influence on similarity measurements.

---

## Objectives

The project aims to:

- Extract unique k-mers from genomic sequences
- Compare genomes using set-based similarity metrics
- Evaluate the impact of different k-mer sizes
- Study the effect of extraction window shifts
- Visualize genomic similarity through graphical analysis

---

## Dataset

Two complete viral genomes are compared:

- SARS-CoV-2
- SARS-TOR2

Sequences are provided in FASTA format.

```
data/
│
├── SARS_COV2.fna
└── SARS_TOR2.fna
```

---

## Methodology

### 1. K-mer Extraction

Each genome is decomposed into overlapping substrings of length **k**.

Example for:

```
Genome : ACTGATC

k = 3
```

Generated k-mers:

```
ACT
CTG
TGA
GAT
ATC
```

Different values of **k** are evaluated:

```
7
11
21
31
41
51
61
71
81
91
101
111
121
```

---

### 2. Jaccard Similarity

The similarity between both genomes is computed using the Jaccard Index:

\[
J(A,B)=\frac{|A\cap B|}{|A\cup B|}
\]

Where:

- A = k-mers from SARS-CoV-2
- B = k-mers from SARS-TOR2

Values close to **1** indicate highly similar genomes.

---

### 3. Mash Distance

Mash distance is derived from the Jaccard similarity and estimates genomic distance.

Lower values indicate genetically similar genomes.

---

### 4. Parameter Evaluation

The analysis compares:

- 13 k-mer sizes
- 2 shift values

This allows evaluation of how parameter selection influences similarity estimation.

---

## Project Structure

```
genome-similarity-kmers/

│
├── data/
│   ├── SARS_COV2.fna
│   └── SARS_TOR2.fna
│
├── src/
│   ├── kmers.py
│   ├── metrics.py
│   ├── comparison.py
│   └── plots.py
│
├── results/
│
├── notebooks/
│   └── Genome_Comparison.ipynb
│
├── figures/
│
├── README.md
│
└── requirements.txt
```

---

## Technologies

- Python
- BioPython
- Matplotlib
- Math

---

## Results

The experiments show that:

- Smaller k values generate higher similarity scores because shorter patterns are more frequently shared.
- Larger k values capture more specific genomic signatures.
- Window shift influences the density of extracted k-mers.
- Some large k values produce a Jaccard similarity of zero, resulting in an infinite Mash distance.

Overall, the analysis highlights the importance of parameter selection when using alignment-free genomic comparison methods.

---

## Example Output

| k | Shift | Jaccard | Mash Distance |
|---|-------|----------|---------------|
| 7 | 1 | 0.693 | 0.029 |
| 11 | 1 | 0.093 | 0.164 |
| 51 | 1 | 0.003 | 0.098 |
| 111 | 2 | 0.000 | ∞ |

---

## Visualization

The project generates graphs illustrating:

- Jaccard Similarity versus k
- Mash Distance versus k

These visualizations facilitate interpretation of the influence of algorithm parameters.

---

## Skills Demonstrated

- Bioinformatics
- Computational Genomics
- Alignment-free sequence comparison
- K-mer analysis
- Scientific Python
- Data visualization
- Algorithm implementation
- BioPython

---

## Limitations

This project focuses on alignment-free comparison using only two viral genomes.

Future work could include:

- Comparison with Needleman-Wunsch alignments
- Comparison with BLAST
- Benchmarking against the Mash software
- Larger viral genome datasets
- Parallel implementation for large-scale genomic analysis

---

## References

- Ondov et al., Mash: Fast genome and metagenome distance estimation using MinHash.
- BioPython Documentation
- Stanford Bioinformatics Resources

---

## Author

**Ceren Dinc**

Master's Degree in Data Management in Biosciences

Passionate about Bioinformatics, Data Science, Machine Learning and AI Engineering.

GitHub: https://github.com/CerenDc
