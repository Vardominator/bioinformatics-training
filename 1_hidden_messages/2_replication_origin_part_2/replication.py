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
    for i in range(len(Text) - len(Pattern) + 1):
        if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d:
            positions.append(i)
    return positions


print(HammingDistance("CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG", "ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT"))
