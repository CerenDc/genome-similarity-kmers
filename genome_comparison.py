import matplotlib.pyplot as plt
import math
from Bio import SeqIO

def read_seq(seq, k, shift):
    D = {}
    for i in range(0, len(seq) - k + 1, shift):
        D[seq[i:i + k]] = True
    return D

def jaccard_similarity(kmers1, kmers2):
    intersection = len(set(kmers1.keys()).intersection(set(kmers2.keys())))
    union = len(set(kmers1.keys()).union(set(kmers2.keys())))
    if union == 0:  
        return 0
    return intersection / union

def mash_distance(jaccard, k):
    if jaccard == 0: 
        return float('inf')  
    return -1 / k * math.log(2 * jaccard / (1 + jaccard))

file1 = "/Users/dincceren/Downloads/SARS_COV2.fna"
file2 = "/Users/dincceren/Downloads/SARS_TOR2.fna"

for record in SeqIO.parse(file1, "fasta"):
    seq1 = str(record.seq)

for record in SeqIO.parse(file2, "fasta"):
    seq2 = str(record.seq)

k_values = [7, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121]
shift_values = [1, 2]

mash_shift1 = []
mash_shift2 = []

for k in k_values:
    for shift in shift_values:
        kmers1 = read_seq(seq1, k, shift)
        kmers2 = read_seq(seq2, k, shift)
        
        jaccard = jaccard_similarity(kmers1, kmers2)
        mash = mash_distance(jaccard, k)
        
        print(f"k = {k:<3} | shift = {shift:<2} | Jaccard Index = {jaccard:.4f} | Mash Distance = {mash:.4f}")
        
        if shift == 1:
            mash_shift1.append(mash)
        elif shift == 2:
            mash_shift2.append(mash)

plt.figure(figsize=(10, 5))
plt.plot(k_values, mash_shift1, marker='o', label="Shift = 1", color='#FF8C00')  
plt.plot(k_values, mash_shift2, marker='o', label="Shift = 2", color='#FFD700') 
plt.title("Distance Mash en fonction de k")
plt.xlabel("Valeur de k")
plt.ylabel("Distance Mash")
plt.grid()
plt.legend()
plt.show()