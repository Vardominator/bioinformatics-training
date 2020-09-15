INTEGER_MASS_TABLE = {}
PEPTIDE_MASS_TABLE = {}
with open('data/integer_mass_table.txt', 'r') as stream:
    lines = stream.readlines()
    for line in lines:
        amino, mass = line.strip().split()
        INTEGER_MASS_TABLE[int(mass)] = amino
        PEPTIDE_MASS_TABLE[amino] = int(mass)

class Vertex:
   """The vertex used in the graph below"""
   def __init__(self, key, data):
       self.adjancencyList = {}
       self.key = key
       self.data = data
       self.currCost = 0  # stores own weight added with followers in path

   def connect(self, otherVertex, weight):
       self.adjancencyList[otherVertex] = weight

   def get_connections(self):
       return self.adjancencyList.keys()

   def get_cost(self, vertex):
       return self.adjancencyList[vertex]

class Graph:
   """graph used to find all paths between two nodes using DFS"""
   def __init__(self):
       self.numberOfVertices = 0
       self.vertices = {}

   def add(self, key, data):
       """adds a vertex to graph and saves vertex based on unique key"""
       if key not in self.vertices:
           self.numberOfVertices += 1
           self.vertices[key] = Vertex(key, data)
           return True

       return False

   def addEdge(self, fromVertex, toVertex, weight):
       """connects two vertices"""
       if fromVertex in self.vertices and toVertex in self.vertices:
           self.vertices[fromVertex].connect(toVertex, weight)
           return True

       return False

   def getAllPaths(self, start, end):
       return self.dfs(start, end, [], [], [])

   def getAllPathsSorted(self, start, end):
       res = self.dfs(start, end, [], [], [])
       return sorted(res, key=lambda k: k['cost'])

   def dfs(self, currVertex, destVertex, visited, path, fullPath):
       """finds all paths between two nodes, returns all paths with their respective cost"""

       # get vertex, it is now visited and should be added to path
       vertex = self.vertices[currVertex]
       visited.append(currVertex)
       path.append(vertex.data)

       # save current path if we found end
       if currVertex == destVertex:
           fullPath.append({"path": list(path), "cost": vertex.currCost})

       for i in vertex.get_connections():
           if i not in visited:
               self.vertices[i].currCost = vertex.get_cost(i) + vertex.currCost
               self.dfs(i, destVertex, visited, path, fullPath)

       # continue finding paths by popping path and visited to get accurate paths
       path.pop()
       visited.pop()

       if not path:
           return fullPath

def generate_spectral_graph(spectrum):
    spectrum = [0] + spectrum
    # graph = {s:[] for s in spectrum}
    graph = Graph()
    for s in spectrum:
        graph.add(s, s)

    for i in range(len(spectrum)):
        for j in range(i+1, len(spectrum)):
            s1 = spectrum[i]
            s2 = spectrum[j]
            diff = abs(s2 - s1)
            if diff in INTEGER_MASS_TABLE:
                # graph[s1].append(s2)
                graph.addEdge(s1, s2, diff)
    return graph

def peptide_mass(peptide):
    mass = 0
    for p in peptide:
        mass += PEPTIDE_MASS_TABLE[p]
    return mass

def masses_to_peptide(masses):
    peptide = ''
    for m in masses:
        peptide += INTEGER_MASS_TABLE[m]
    return peptide

def ideal_spectrum(peptide):
    prefixes_suffixes = []
    for i in range(len(peptide)):
        prefixes_suffixes.append(peptide[:i])
        prefixes_suffixes.append(peptide[i:])
    masses = [peptide_mass(ps) for ps in prefixes_suffixes]
    return sorted(masses)

def decoding_ideal_spectrum(spectrum):
    graph = generate_spectral_graph(spectrum)
    paths = graph.getAllPathsSorted(spectrum[0], spectrum[-1])
    for path in paths:
        path = [0] + path['path']
        weights = [graph.vertices[path[i - 1]].adjancencyList[path[i]] for i in range(1, len(path))]
        peptide = masses_to_peptide(weights)
        if ideal_spectrum(peptide) == [0] + spectrum:
            return peptide

def peptide_to_vector(peptide):
    prefixes_masses = []
    for i in range(1, len(peptide) + 1):
        prefixes_masses.append(peptide_mass(peptide[:i]))
    vector = [0]*prefixes_masses[-1]
    for mass in prefixes_masses:
        vector[mass - 1] = 1
    return vector

def vector_to_peptide(vector):
    cum_masses = [i + 1 for i in range(len(vector)) if vector[i] == 1]
    s = 0
    peptide = ''
    for m in cum_masses:
        curr = m - s
        peptide += INTEGER_MASS_TABLE[curr]
        s += curr
    return peptide

def print_graph(graph):
    res = ''
    for node in graph.keys():
        for neighbor in graph[node]:
            res += '{}->{}:{}\n'.format(node, neighbor, INTEGER_MASS_TABLE[neighbor - node])
    return res

# with open('data/problem9.txt', 'r') as stream:
#     spectrum = [int(s) for s in stream.readline().strip().split()]

# print(decoding_ideal_spectrum(spectrum))

# graph = generate_spectral_graph(spectrum)
# print(graph.getAllPathsSorted(0, spectrum[-1]))
# res = print_graph(graph)

# with open('output/problem8.txt', 'w') as stream:
#     stream.write(res)

# print(ideal_spectrum('GPG'))


# with open('data/problem10.txt', 'r') as stream:
#     peptide = stream.read().strip()

# with open('output/problem10.txt', 'w') as stream:
#     stream.write(' '.join([str(v) for v in peptide_vector(peptide)]))

with open('data/problem11.txt', 'r') as stream:
    vector = [int(s) for s in stream.read().strip().split()]

print(vector_to_peptide(vector))