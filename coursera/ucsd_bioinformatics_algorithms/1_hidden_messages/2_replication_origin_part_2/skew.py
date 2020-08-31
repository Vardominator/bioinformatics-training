def MinimumSkew(Genome):
    positions = [] # output variable
    # your code here
    skew = SkewArray(Genome)
    min_skew = min(skew)
    positions = [i for i,s in enumerate(skew) if s == min_skew]
    return positions

def MaximumSkew(Genome):
    positions = [] # output variable
    # your code here
    skew = SkewArray(Genome)
    max_skew = max(skew)
    positions = [i for i,s in enumerate(skew) if s == max_skew]
    return positions

# Input:  A String Genome
# Output: SkewArray(Genome)
# HINT:   This code should be taken from the last Code Challenge.
def SkewArray(Genome):
    skew = [0]*(1 + len(Genome))
    for i in range(len(Genome)):
        if Genome[i] == 'C':
            skew[i + 1] = skew[i] - 1
        elif Genome[i] == 'G':
            skew[i + 1] = skew[i] + 1
        else:
            skew[i + 1] = skew[i]
    print(skew)
    return skew

with open('data/dataset_7_6.txt', 'r') as f:
    genome = f.read()

min_skew = MinimumSkew(genome)

print(' '.join([str(s) for s in min_skew]))


max_skew = MaximumSkew(genome)

print(' '.join([str(s) for s in max_skew]))
