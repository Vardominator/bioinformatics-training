def hamming_distance(pattern, seq):
    return sum(c1 != c2 for c1, c2 in zip(pattern, seq))

def extract_kmers(dna, k):
    k_mers = set()
    for gene in dna:
        for i in range(len(gene) - k + 1):
            k_mer = gene[i:i+k]
            k_mers.add(k_mer)
    return list(k_mers)

def min_d(pattern, text, k):
    min_dist = len(pattern)
    for i in range(len(text) - k + 1):
        if hamming_distance(pattern, text[i:i+k]) < min_dist:
            min_dist = hamming_distance(pattern, text[i:i+k])
    return min_dist

def min_d_all(pattern, dna, k):
    return sum([min_d(pattern, gene, k) for gene in dna])

def median_string(dna, k):
    k_mers = extract_kmers(dna, k)
    min_d = 100000000
    min_k_mer = None
    for k_mer in k_mers:
        curr_min_d = min_d_all(k_mer, dna, k)
        if curr_min_d <= min_d:
            min_d = curr_min_d
            min_k_mer = k_mer
            print(min_k_mer)
    return min_k_mer

# with open('data/dataset_158_9.txt', 'r') as stream:
#     k = stream.readline().strip()
#     dna = stream.read().splitlines()

# with open('data/dataset_158_9_result.txt', 'w') as stream:
#     stream.write(median_string(dna, int(k)))

k = 7
dna = ['CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC','GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC','GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG']

print(median_string(dna, k))