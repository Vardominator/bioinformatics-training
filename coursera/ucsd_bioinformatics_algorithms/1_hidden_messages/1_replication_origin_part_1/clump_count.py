with open("data/E_coli.txt", 'r') as data_file:
    dataset = data_file.readlines()

genome = dataset[0].strip()
# k, L, t = dataset[1].split() 
k, L, t = 9, 500, 3
clumps = set()
checked_subgenomes = set()

for i in range(0, len(genome) - int(L)):
    if i % 1000 == 0:
        print("{} % completed".format(float(i) / float(len(genome)) * 100.0))
    subgenome = genome[i:i + int(L)]
    if subgenome not in checked_subgenomes:
        frequencies = {}
        for j in range(0, len(subgenome) - int(k)):
            k_mer = subgenome[j:j + int(k)]
            if k_mer not in frequencies:
                frequencies[k_mer] = 1
            else:
                frequencies[k_mer] += 1
            if frequencies[k_mer] == int(t):
                clumps.add(k_mer)
        checked_subgenomes.add(subgenome)

print(" ".join([c for c in clumps]))
print(len(clumps))