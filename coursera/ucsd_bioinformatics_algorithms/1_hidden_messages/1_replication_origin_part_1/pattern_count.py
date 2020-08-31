from joblib import Parallel, delayed

def count_patterns(genome, pattern, state):
    matches = 0
    for i in range(0, len(genome) - len(pattern)):
        subset = genome[i:i+len(pattern)]
        if subset == pattern:
            matches += 1
    state[pattern] = matches
    return matches

def frequent_words(genome, k, t):
    frequent_patterns = set()
    # counts = []
    state = {}
    counted = set()
    for i in range(0, len(genome) - k):
        if genome[i:i+k] not in state:
            counts = count_patterns(genome, genome[i:i+k], state)
            if counts == t:
                frequent_patterns.add(genome[i:i+k])

    # for i in range(0, len(genome) - k):
    #     if counts[i] == t:
    #         frequent_patterns.add(genome[i:i+k])

    if len(frequent_patterns) > 0:
        print(set(frequent_patterns))
    return set(frequent_patterns)

with open("E_coli.txt", 'r') as data_file:
    dataset = data_file.readlines()

genome = dataset[0].strip()
# k, L, t = dataset[1].split() 
k, L, t = 9, 500, 3
clumps = set()

# results = Parallel(n_jobs=4)(delayed(frequent_words)(genome[i:i+int(L)], int(k), int(t)) for i in range(0, len(genome) - int(L)))
# # print(results)
# for result in results:
#     clumps.update(result)
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

    # if i % 1000 == 0:
    #     print("{} % completed".format(float(i) / float(len(genome)) * 100.0))
    # sub_genome = genome[i:i+int(L)]
    # clumps.update(frequent_words(sub_genome, int(k), int(t)))

print(" ".join([c for c in clumps]))
print(len(clumps))