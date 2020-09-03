def chromosome_to_cycle(chromosome):
    nodes = [0]*(len(chromosome) * 2)
    for j in range(1, len(chromosome) + 1):
        i = chromosome[j - 1]
        if i > 0:
            nodes[2*j - 2] = 2*i - 1
            nodes[2*j - 1] = 2*i
        else:
            nodes[2*j - 2] = -2*i
            nodes[2*j - 1] = -2*i - 1
    return nodes

def cycle_to_chromosome(nodes):
    chromosome = [0]*(len(nodes) // 2)
    for j in range(1, len(nodes) // 2 + 1):
        if nodes[2*j - 2] < nodes[2*j - 1]:
            chromosome[j - 1] = nodes[2*j - 1] // 2
        else:
            chromosome[j - 1] = -1*nodes[2*j - 2] // 2
    return chromosome

def colored_edges(p):
    edges = []
    for chrom in p:
        nodes = chromosome_to_cycle(chrom)
        for j in range(len(chrom)):
            edges.append((nodes[2*j-1], nodes[2*j]))
    return edges

def graph_to_genome(cycles):
    P = []
    for cycle in cycles:
        print(cycle)
        cycle.sort()
        chromosome = cycle_to_chromosome(cycle)
        P.append(chromosome)
    return P

def find_cycles(graph):
    cycles_count = 0
    cycles = []
    while len(graph) > 0:
        cycles_count += 1
        current = list(graph.keys())[0]
        curr_cycles = []
        while current in graph:
            temp = graph[current][0]
            if len(graph[current]) == 1:
                del graph[current]
            else:
                graph[current] = graph[current][1:]
            # Remove the complementary edge.
            if graph[temp] == [current]:
                del graph[temp]
            else:
                graph[temp].remove(current)
            curr_cycles.append(current)
            current = temp
        cycles.append(curr_cycles)
    return cycles_count, cycles

def two_break_dist(P, cycles_count):
    # Theorem: d(P,Q) = blocks(P,W) - cycles(P,Q)
    return sum([len(block) for block in P]) - cycles_count

def two_break_sorting(P,Q):
    red = colored_edges(Q)
    path = [P]
    while two_break_distance(P,Q) > 0:
        cycles = colored_edges_cycles(colored_edges(P),red)
        for c in cycles:
            if len(c) >= 4:
                P = two_break_on_genome(P,c[0],c[1],c[3],c[2])
                path.append(P)
                break          
    return path

def shared_kmers(k,a,b):
    def reverse_complement(pattern):
        rev = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
        reverse = map(lambda c: rev[c], pattern[::-1])
        return ''.join(reverse)
    
    def kmers_dict(k, text):
        kmers = {}
        for i in range(len(text) - k + 1):
            kmer = text[i:i+k]
            kmers[kmer] = kmers.setdefault(kmer,[]) + [i]
            kmers[reverse_complement(kmer)] = kmers[kmer]
        return kmers
    
    shared = []
        
    bkmers = kmers_dict(k,b)
    for i in range(len(a) - k + 1):
        akmer = a[i:i+k]
        if akmer in bkmers:
            shared += [(i,j) for j in bkmers[akmer]]
    
    return sorted(shared)

def generate_graph(edges):
    graph = {}
    for edge in colored:
        if edge[0] in graph:
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]
        if edge[1] in graph:
            graph[edge[1]].append(edge[0])
        else:
            graph[edge[1]] = [edge[0]]
    return graph  

with open('data/week5problem5.txt', 'r') as stream:
    # for line in stream.readlines():
    P, Q = [line.strip().lstrip('(').rstrip(')').split(')(') for line in stream.readlines()]
    P = [list(map(int, block.split())) for block in P]
    Q = [list(map(int, block.split())) for block in Q]