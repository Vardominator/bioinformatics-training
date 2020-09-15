ALPHABET = ['A','C','T','G']

def process_input(lines):
    n = int(lines[0].strip())
    tree = {}
    k_mer_length = 0
    mothers = {}
    for line in lines[1:]:
        v,w = line.strip().split('->')
        mothers[w] = v
        k_mer_length = max(k_mer_length, len(w), len(v))
        if v not in tree:
            tree[v] = [w]
        else:
            tree[v].append(w)
        if w not in tree:
            tree[w] = []
    return n, tree, k_mer_length, mothers

def find_ripe_nodes(tree, tags):
    ripe_nodes = []
    for v in tree.keys():
        children = tree[v]
        if tags[v] == 0 and tags[children[0]] == 1 and tags[children[1]] == 1:
            ripe_nodes.append(v)
    return ripe_nodes

def min_hamming(skv, v):
    min_score, min_k = float('inf'), None
    for k in ALPHABET:
        if skv[k][v] < min_score:
            min_score = skv[k][v]
            min_k = k
    return min_score, min_k

def min_hammings(skv, v):
    min_score, min_k = min_hamming(skv, v)
    min_scores, min_ks = [],[]
    for k in ALPHABET:
        if skv[k][v] == min_score:
            min_scores.append(skv[k][v])
            min_ks.append(k)
    return min_scores, min_ks

def hamming_distance(v, w):
    return sum([1 if v[i] != w[i] else 0 for i in range(len(v))])

def minimum_assignment(skv, k, node):
    min_a = float('inf')
    for i in ALPHABET:
        alpha = 1
        if i == k:
            alpha = 0
        min_a = min(min_a, skv[i][node] + alpha)
    return min_a

def small_parsimony(tree, c, assignments, mothers):
    tags = {v:0 for v in tree.keys()}
    skv = {k:{} for k in ALPHABET}
    for v in tree.keys():
        if len(tree[v]) == 0:
            tags[v] = 1
            for k in ALPHABET:
                if v[c] == k:
                    skv[k][v] = 0
                else:
                    skv[k][v] = float('inf')
    ripe_nodes = find_ripe_nodes(tree, tags)

    while ripe_nodes:
        v = ripe_nodes.pop(0)
        daughter_v = tree[v][0]
        son_v = tree[v][1]
        tags[v] = 1
        for k in ALPHABET:
            skv[k][v] = minimum_assignment(skv, k, daughter_v) + minimum_assignment(skv, k, son_v)
        ripe_nodes = find_ripe_nodes(tree, tags)

    min_root_scores, min_root_ks = min_hammings(skv, v)
    # min_mother_scores, min_mother_ks = min_root_scores, min_root_ks
    # # mother_k = root_k
    stack = [v]
    mother_scores = {}
    while stack:
        v = stack.pop()
        min_scores, min_ks = min_hammings(skv, v)
        if v in mothers:
            # non-root
            # min_mother_scores, min_mother_ks = min_hammings(skv, mothers[v])
            min_mother_k = assignments[mothers[v]][-1]
            
            # intersect = sorted(list(set(min_mother_ks) & set(min_ks)))
            # print(intersect)
            # print()
            if min_mother_k in min_ks:
                assignments[v] += min_mother_k
            else:
                assignments[v] += min_ks[0]
        else:
            assignments[v] += min_ks[0]
        if tree[v]:
            stack.append(tree[v][0])
            stack.append(tree[v][1])
    return min_root_scores[0]


with open('data/problem6.txt', 'r') as stream:
    lines = stream.readlines()

n, tree, k_mer_length, mothers = process_input(lines)

assignments = {k:'' for k in tree.keys()}
total_score = 0

for c in range(k_mer_length):
    total_score += small_parsimony(tree, c, assignments, mothers)


with open('output/problem6.txt', 'w') as stream:
    print(total_score)
    stream.write(str(total_score) + '\n')
    total = 0
    for v in tree.keys():
        if tree[v]:
            hd_daughter = hamming_distance(assignments[v], assignments[tree[v][0]])
            hd_son = hamming_distance(assignments[v], assignments[tree[v][1]])
            total += hd_daughter
            total += hd_son
            stream.write('{}->{}:{}'.format(assignments[v], assignments[tree[v][0]], hd_daughter) + '\n')
            stream.write('{}->{}:{}'.format(assignments[v], assignments[tree[v][1]], hd_son) + '\n')
            stream.write('{}->{}:{}'.format(assignments[tree[v][0]], assignments[v], hd_daughter) + '\n')
            stream.write('{}->{}:{}'.format(assignments[tree[v][1]], assignments[v], hd_son) + '\n')

    print(total)