import operator

def completement(substring):
    complements = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    complement = "".join([complements[c] for c in substring][::-1])
    return complement

def SkewArray(Genome):
    skew = [0]*(1 + len(Genome))
    for i in range(len(Genome)):
        if Genome[i] == 'C':
            skew[i + 1] = skew[i] - 1
        elif Genome[i] == 'G':
            skew[i + 1] = skew[i] + 1
        else:
            skew[i + 1] = skew[i]
    return skew

def HammingDistance(p, q):
    return len([i for i in range(len(p)) if p[i] != q[i]])

def ApproximatePatternMatching(Text, Pattern, d):
    positions = []
    matched_patterns = []
    for i in range(len(Text) - len(Pattern) + 1):
        subgenome = Text[i:i+len(Pattern)]
        if HammingDistance(subgenome, Pattern) <= d:
            positions.append(i)
            matched_patterns.append(subgenome)
    return positions, matched_patterns


def frequent_words(k, d, genome):
    frequencies = {}
    for i in range(len(genome) - k + 1):
        subgenome = genome[i:i+k]
        if subgenome not in frequencies:
            rev_comp_subgenome = completement(subgenome)
            positions, matched_patterns = ApproximatePatternMatching(genome, subgenome, d)
            rev_comp_positions, rev_comp_matched_patterns = ApproximatePatternMatching(genome, rev_comp_subgenome, d)
            print(matched_patterns)
            # frequencies[subgenome] = len(ApproximatePatternMatching(genome, subgenome, d)) + len(ApproximatePatternMatching(genome, rev_comp_subgenome, d))
    return frequencies

with open("data/dataset_9_8.txt", 'r') as f:
    data = f.read().splitlines()

genome = data[0]
k, d = data[1].split(' ')

# frequencies = frequent_words(int(k), int(d), genome)

# m = max(frequencies.items(), key=operator.itemgetter(1))[1]

# max_freqs = []
# for key, value in frequencies.items():
#     if value == m:
#         max_freqs.append(key)
#         max_freqs.append(completement(key))

# print(' '.join([s for s in max_freqs]))

print(HammingDistance("CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG", "ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT"))

positions, matched_patterns = ApproximatePatternMatching("CGTGACAGTGTATGGGCATCTTT", "TGT", 1)

print(len(positions))