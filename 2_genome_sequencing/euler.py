import random

def construct_graph(graph_str):
    graph = {}
    for s in graph_str:
        edges = s.split('->')
        node = edges[0].strip()
        neighbors = edges[1].strip().split(',')
        graph[node] = neighbors
    return graph

def find_euler_cycle(graph):
    v0 = random.choice(graph.keys())
    visited_edges = set()
    cycle = []
    def find_cycle(node):
        for neighbor in graph[node]:
            edge = "{} -> {}".format(node, neighbor)
            if edge not in visited_edges:
                visited_edges.add(edge)
                find_cycle(neighbor)
        cycle.append(node)
                
    find_cycle(v0)
    return cycle

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
    def find_path(node):
        for neighbor in graph[node]:
            edge = "{} -> {}".format(node, neighbor)
            if edge not in visited_edges:
                visited_edges.add(edge)
                if neighbor in graph:
                    find_path(neighbor)
                else:
                    path.append(neighbor)
        path.append(node)
                
    find_path(v0)
    return path

with open('data/d6.txt', 'r') as f:
    graph_str = f.read().splitlines()

graph = construct_graph(graph_str)
path = find_euler_path(graph)

with open('data/d6result.txt', 'w') as f:
    f.write('->'.join([c for c in path[::-1]]))