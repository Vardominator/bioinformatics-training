def construct_debruijn(k_mers):
    graph = {}
    for i in range(0, len(k_mers)):
        snip1 = k_mers[i][:-1]
        if snip1 not in graph:
            graph[snip1] = []
        snip2 = k_mers[i][1:]
        if snip2 not in graph:
            graph[snip2] = []

    for g in graph:
        for i in range(0, len(k_mers)):
            if g + k_mers[i][-1] == k_mers[i]:
                graph[g].append(k_mers[i][1:])
    return graph

def find_euler_path(graph):
    incoming_edges = {}
    for node in graph:
        incoming_edges[node] = 0
    for node in graph:
        for neighbor in graph[node]:
            if neighbor not in incoming_edges:
                incoming_edges[neighbor] = 1
            else:
                incoming_edges[neighbor] += 1
    
    v0 = None
    for node in graph:
        print("Node:{} ; Outgoing:{} ; Incoming:{}".format(node, len(graph[node]), incoming_edges[node]))
        if len(graph[node]) > incoming_edges[node]:
            v0 = node
            break

    visited_edges = set()
    path = []
    stack = [v0]
    while stack:
        node = stack.pop(0)
        for neighbor in graph[node]:
            edge = "{} -> {}".format(node, neighbor)
            if edge not in visited_edges:
                visited_edges.add(edge)
                if neighbor in graph:
                    stack.insert(0, neighbor)
                else:
                    path.insert(0, neighbor)
        path.insert(0, node)

    return path

def construct_genome(path):
    path = path[::-1]
    genome = path[0]
    for n in path[1:]:
        genome += n[-1]
    return genome

with open('data/d7.txt', 'r') as f:
    k_mers_size = f.readline()
    k_mers = f.read().splitlines()

debruijn = construct_debruijn(k_mers)
path = find_euler_path(debruijn)
genome = construct_genome(path)

with open('data/d7result.txt', 'w') as f:
    f.write(genome)