"""
gRNA Analysis for CRISPR-Cas9

This script identifies and evaluates guide RNAs (gRNAs) for CRISPR-Cas9 applications.
It performs the following tasks:
- gRNA Design: Identifies potential gRNA sequences within a target gene.
- Efficiency Prediction: Predicts the efficiency of gRNAs based on sequence features.
- Secondary Structure Analysis: Detects potential secondary structures, like hairpins, that could affect gRNA function.
- Off-Target Analysis: Identifies potential off-target binding sites within a given sequence.

This script is designed to be adaptable to any gene of interest.

Author: KNIDIRI MEHDI
Date: 20/08/2024
"""

import os

# Function to calculate GC content of a gRNA
def calculate_gc_content(gRNA):
    gc_count = gRNA.count('G') + gRNA.count('C')
    return (gc_count / len(gRNA)) * 100

# Function to check for potential secondary structure (simple palindromes)
def check_secondary_structure(gRNA):
    reverse_complement = gRNA[::-1].translate(str.maketrans("ATGC", "TACG"))
    # Look for palindromic sequences
    palindrome_sites = []
    for i in range(len(gRNA) - 3):
        for j in range(i + 4, len(gRNA)):
            if gRNA[i:j] == reverse_complement[len(gRNA) - j:len(gRNA) - i]):
                palindrome_sites.append((i, j))
    return palindrome_sites

# Function to check for off-target effects allowing for 1 mismatch
def check_off_target_extended(gRNA, sequence):
    off_target_sites = []
    for i in range(len(sequence) - len(gRNA) + 1):
        subseq = sequence[i:i + len(gRNA)]
        mismatches = sum(1 for a, b in zip(gRNA, subseq) if a != b)
        if mismatches <= 1:
            off_target_sites.append((i, mismatches))
    return off_target_sites

# Function to simulate efficiency prediction based on GC content and motif presence
def simulate_efficiency(gRNA):
    gc_content = calculate_gc_content(gRNA)
    efficiency = "High" if 40 <= gc_content <= 60 else "Low"
    if gRNA.endswith("GG"):
        efficiency += " + Good Motif"
    return efficiency

# Main function
def main():
    # Example gene sequence (replace with actual sequence)
    sequence = "AGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC"

    # List of gRNAs (replace with actual designed gRNAs)
    gRNAs = [
        'TGAATTAGGGGTCCCCGGA', 
        'TGAATGAATTAGGGGTCCC', 
        'ATGAATTAGGGGTCCCCGG'
    ]
    
    results = []
    for gRNA in gRNAs:
        secondary_structures = check_secondary_structure(gRNA)
        off_target_sites = check_off_target_extended(gRNA, sequence)
        efficiency = simulate_efficiency(gRNA)
        results.append({
            "gRNA": gRNA,
            "GC_Content": calculate_gc_content(gRNA),
            "Secondary_Structures": secondary_structures,
            "Off_Target_Sites": len(off_target_sites),
            "Efficiency": efficiency
        })

    # Save results to a file
    output_file = os.path.join("results", "gRNA_analysis_results.txt")
    os.makedirs("results", exist_ok=True)
    with open(output_file, "w") as f:
        for result in results:
            f.write(f"gRNA: {result['gRNA']}\n")
            f.write(f"GC Content: {result['GC_Content']}%\n")
            f.write(f"Secondary Structures: {result['Secondary_Structures']}\n")
            f.write(f"Off-Target Sites (1 mismatch allowed): {result['Off_Target_Sites']}\n")
            f.write(f"Efficiency Prediction: {result['Efficiency']}\n\n")

if __name__ == "__main__":
    main()
