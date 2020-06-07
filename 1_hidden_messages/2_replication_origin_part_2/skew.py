def MinimumSkew(Genome):
    positions = [] # output variable
    # your code here
    skew = SkewArray(Genome)
    min_skew = min(skew)
    positions = [i for i,s in enumerate(skew) if s == min_skew]
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
    return skew

print(MinimumSkew("CATTCCAGTACTTCGATGATGGCGTGAAGA"))


x=0
for y in range(0,5):
    x+=y
print(x)