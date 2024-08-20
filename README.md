# gRNA Analysis for CRISPR-Cas9

## Overview
This project provides a Python-based tool for designing and evaluating guide RNAs (gRNAs) for use in CRISPR-Cas9 gene editing. The tool analyzes gRNAs for their potential efficiency, secondary structure, and off-target effects. This pipeline can be applied to any gene of interest.

## Features
- **gRNA Design**: Identifies potential gRNA sequences targeting specific regions of a gene.
- **Efficiency Prediction**: Evaluates gRNA efficiency based on GC content and sequence motifs.
- **Secondary Structure Analysis**: Detects potential secondary structures (e.g., hairpins) within gRNAs.
- **Off-Target Analysis**: Identifies potential off-target sites within a given sequence.

## Requirements
- Python 3.x
- No additional packages required (standard Python library is sufficient).

## Usage
1. Place your gene sequence in a FASTA file inside the `data/` directory.
2. Modify the script to point to your gene sequence file.
3. Run the script using Python.

## Example
```bash
python gRNA_analysis.py
