def compositions(genome, k):
    comps = []
    for i in range(0, len(genome) - k):
        comps.append(genome[i:i+k])
    comps.sort()
    return comps

with open('data/d1.txt', 'r') as f:
    inputs = f.readlines()
    k = int(inputs[0])
    genome = inputs[1]

comps = '\n'.join(c for c in compositions(genome, k))
with open('data/d1results.txt', 'w') as f:
    f.write(comps)