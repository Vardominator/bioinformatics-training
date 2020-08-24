def hamming_distance(pattern, seq):
    return sum(c1 != c2 for c1, c2 in zip(pattern, seq))

def suffix(pattern):
    if len(pattern)==1:
        return ""
    suffix = pattern[1:]
    return suffix

def first_symbol(pattern):
    x = pattern[0]
    return x

def neighbours(pattern, d):
    if d==0:
        return {pattern}
    if len(pattern)==1:
        x = ['A','C','T','G']
        return x
    neighbourhood = set()
    suffix_neighbours = neighbours(suffix(pattern),d)
    for text in suffix_neighbours:
        if hamming_distance(suffix(pattern),text) < d:
            for y in "ATCG":
                string = y + text
                neighbourhood.add(string)
        else:
            m = first_symbol(pattern) + text
            neighbourhood.add(m)
    neighbourhood = list(neighbourhood)
    return neighbourhood

def motif_enumeration(dna, k, d):
    patterns = set()
    start = dna[0]
    for i in range(len(start) - k + 1):
        gene = start[i:i+k]
        curr_neighbors = neighbours(gene, d)
        for neighbour in curr_neighbors:
            match_count = 0
            for sequence in dna:
                for j in range(len(sequence) - k + 1):
                    if hamming_distance(neighbour, sequence[j:j+k]) <= d:
                        match_count += 1
                        break
            if match_count == len(dna):
                patterns.add(neighbour)

    return patterns

with open('data/dataset_156_8.txt', 'r') as stream:
    k, d = stream.readline().strip().split(' ')
    dna = stream.read().splitlines()

enum = motif_enumeration(dna, int(k), int(d))

with open('data/dataset_156_8_result.txt', 'w') as stream:
    stream.write(' '.join([e for e in enum]))

