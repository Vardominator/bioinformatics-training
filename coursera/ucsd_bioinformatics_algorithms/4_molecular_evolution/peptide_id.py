from itertools import combinations

INTEGER_MASS_TABLE = {}
PEPTIDE_MASS_TABLE = {}
with open('data/integer_mass_table.txt', 'r') as stream:
    lines = stream.readlines()
    for line in lines:
        amino, mass = line.strip().split()
        INTEGER_MASS_TABLE[int(mass)] = amino
        PEPTIDE_MASS_TABLE[amino] = int(mass)

def peptide_mass(peptide):
    mass = 0
    for p in peptide:
        mass += PEPTIDE_MASS_TABLE[p]
    return mass

def peptide_to_vector(peptide):
    prefixes_masses = []
    for i in range(1, len(peptide) + 1):
        prefixes_masses.append(peptide_mass(peptide[:i]))
    vector = [0]*prefixes_masses[-1]
    for mass in prefixes_masses:
        vector[mass - 1] = 1
    return vector

def score(peptide, spectrum):
    return sum([peptide[i]*spectrum[i] for i in range(len(peptide))])

from collections import defaultdict

def subsequence_sum(masses, k):
    prev_sum = defaultdict(lambda: 0)
    count = 0
    pairs = []
    n = len(masses)
    curr_sum = 0
    for i in range(n):
        curr_sum += masses[i]
        if curr_sum == k:
            count += 1
            pairs.append((0, i))

        keys = list(prev_sum.keys())
        if (curr_sum - k) in prev_sum:
            count += prev_sum[curr_sum - k]
            pairs.append((keys.index(curr_sum - k), i))

        prev_sum[curr_sum] += 1

    return count, pairs

def maximum_scoring_peptide(proteome, spectrum):
    length = len(proteome)
    masses = [peptide_mass(proteome[i]) for i in range(length)]
    max_scoring_peptide = None
    max_score = -1
    count, ranges = subsequence_sum(masses, len(spectrum))
    for r in ranges:
        vector = peptide_to_vector(proteome[r[0]:r[1]])
        if len(vector) == len(spectrum):
            s = score(vector, spectrum)
            if s > max_score:
                max_score = s
                max_scoring_peptide = proteome[r[0]:r[1]]
    return max_scoring_peptide

with open('data/problem12.txt', 'r') as stream:
    spectrum = [int(s) for s in stream.readline().strip().split()]
    proteome = stream.readline().strip()

print(maximum_scoring_peptide(proteome, spectrum))