# Data structure to store graph edges
class Edge:
	def __init__(self, source, dest, weight):

		self.source = source
		self.dest = dest
		self.weight = weight


# Class to represent a graph object
class Graph:
	# Constructor
	def __init__(self, edges, N):

		# A List of Lists to represent an adjacency list
		self.adjList = [[] for _ in range(N)]

		# add edges to the undirected graph
		for edge in edges:
			self.adjList[edge.source].append(edge)


# Perform DFS on graph and set departure time of all
# vertices of the graph
def DFS(graph, v, discovered, departure, time):

	# mark current node as discovered
	discovered[v] = True

	# set arrival time - not needed
	# time = time + 1

	# do for every edge (v -> u)
	for e in graph.adjList[v]:
		u = e.dest
		# u is not discovered
		if not discovered[u]:
			time = DFS(graph, u, discovered, departure, time)

	# ready to backtrack
	# set departure time of vertex v
	departure[time] = v
	time = time + 1

	return time


# The function performs topological sort on a given DAG and then finds out
# the longest distance of all vertices from given source by running
# one pass of Bellman-Ford algorithm on edges of vertices in topological order
def findLongestDistance(graph, source, N):

	# departure stores vertex number having its departure
	# time equal to the index of it
	departure = [-1] * N

	# stores vertex is discovered or not
	discovered = [False] * N
	time = 0

	# perform DFS on all undiscovered vertices
	for i in range(N):
		if not discovered[i]:
			time = DFS(graph, i, discovered, departure, time)

	cost = [float('inf')] * N
	cost[source] = 0

	# Process the vertices in topological order i.e. in order
	# of their decreasing departure time in DFS
	for i in reversed(range(N)):

		# for each vertex in topological order,
		# relax cost of its adjacent vertices
		v = departure[i]

		for e in graph.adjList[v]:
			# edge e from v to u having weight w
			u = e.dest
			w = e.weight * -1  # negative the weight of edge

			# if the distance to the destination u can be shortened by
			# taking the edge vu, then update cost to the lower value
			if cost[v] != float('inf') and cost[v] + w < cost[u]:
				cost[u] = cost[v] + w

	# print longest paths
	for i in range(N):
		print("dist", (source, i), "=", (cost[i] * -1))


if __name__ == '__main__':

	# List of graph edges as per above diagram
	edges = [
		Edge(0, 1, 5),
        Edge(0, 2, 6),
        Edge(0, 3, 5),
        Edge(1, 2, 2),
        Edge(1, 5, 4),
        Edge(2, 4, 4),
        Edge(2, 5, 3),
        Edge(2, 6, 5),
        Edge(3, 4, 4),
        Edge(3, 5, 5),
        Edge(4, 6, 2),
        Edge(5, 6, 1)
	]

	# Set number of vertices in the graph
	N = 7

	# create a graph from given edges
	graph = Graph(edges, N)

	# source vertex
	source = 0

	# find longest distance of all vertices from given source
	findLongestDistance(graph, source, N)