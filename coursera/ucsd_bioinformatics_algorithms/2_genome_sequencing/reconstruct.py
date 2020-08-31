def reconstruct(path):
    genome = path[0].strip()
    for i in range(1, len(path)):
        genome += path[i].strip()[-1]
    return genome

with open('data/d2.txt', 'r') as f:
    path = f.readlines()
    genome = reconstruct(path)
    with open('data/d2results.txt', 'w') as fout:
        fout.write(genome)