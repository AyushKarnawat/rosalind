# Bioinformatics Stronghold, Problem 1: Counting DNA Nucleotides
#
# A string is simply an ordered collection of symbols selected from some alphabet and
# 	formed into a word; the length of a string is the number of symbols that it contains.
# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
#
# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
#
# Sample Input: AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
# Sample Output: 20 12 17 21

from enum import Enum


class DNA(Enum):
    """Represents the various nucleotides that can be within a given DNA string."""
    A = "A"
    C = "C"
    G = "G"
    T = "T"


def count_nucleotides(dna):
    """
    Counts the total number of each type of nucleotide in the given DNA string.

    Params:
    -------
    dna: (str)
        A collection of various nucleotides

    Returns:
    --------
    dna_counts: (list)
        Represents the number of each type of nucleotide in the order (A,C,T,G)
    """
    return dna.count(DNA.A.value), dna.count(DNA.C.value), dna.count(DNA.G.value), dna.count(DNA.T.value)


if __name__ == "__main__":
    with open("datasets/rosalind_dna.txt", "r") as dna:
        sequence = dna.read()

    # Compute total number of nucletides each
    num_a, num_c, num_g, num_t = count_nucleotides(sequence)
    print(num_a, num_c, num_g, num_t)

    # Save output
    with open("output/001_rosalind_dna.txt", "w") as out:
        out.write(str(num_a) + " ")
        out.write(str(num_c) + " ")
        out.write(str(num_g) + " ")
        out.write(str(num_t))