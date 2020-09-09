import numpy as np
from collections import OrderedDict

def process_file(filename):
    with open(filename) as f:
        for i, line in enumerate(f):
            line = line.strip()
            if i == 0:
                dim = int(line)
                # matrix = np.zeros((dim, dim), dtype=np.int32)
                matrix = [[0]*dim for _ in range(dim)]
            else:
                # rowData = np.array(line.split()).astype(np.int32)
                rowData = [int(v) for v in line.split()]
                matrix[i-1] = rowData
    return (dim, matrix)

def lowest_cell(matrix):
    min_cell = float("inf")
    x, y = -1, -1
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] < min_cell and i != j:
                min_cell = matrix[i][j]
                x, y = i, j
    return x,y

def closest_clusters(clusters, matrix):
    cluster_keys = list(clusters.keys())
    min_d_avg = float('inf')
    ci, cj = None, None
    for i in range(len(cluster_keys)):
        for j in range(len(cluster_keys)):
            d = dist_avg(clusters[cluster_keys[i]], clusters[cluster_keys[j]], matrix)
            if d < min_d_avg and i != j:
                min_d_avg = d
                ci = cluster_keys[i]
                cj = cluster_keys[j]
    return ci, cj, min_d_avg

def merge_clusters(clusters, x, y):
    cluster_keys = list(clusters.keys())
    ci = cluster_keys[x]
    cj = cluster_keys[y]
    return clusters[ci] + clusters[cj], ci, cj
    # clusters['c_new'] = new_cluster

def update_matrix(matrix, c_new):
    pass

def join_table(matrix, ci, cj):
    new_row = []
    for i in range(0, len(matrix)):
        new_row.append((matrix[ci][i] + matrix[cj][i]) / 2)
    matrix.pop(cj)
    matrix.pop(ci)
    for i in range(len(matrix)):
        row = matrix[i]
        row.pop(cj)
        row.pop(ci)
    for i in range(len(matrix)):
        row = matrix[i]
        row.append(new_row[i])
    matrix.append(new_row[:len(matrix)])
    if len(matrix) > 1:
        matrix[-1].append(0)


def upgma(matrix, n):
    clusters = OrderedDict({str(i):[i] for i in range(n)})
    tree = OrderedDict({str(i):{} for i in range(n)})
    age = {str(i):0 for i in range(n)}
    last_c_new = len(matrix)
    while len(clusters) > 1:
        x, y = lowest_cell(matrix)
        c_new, ci, cj = merge_clusters(clusters, x, y)
        c_new_name = str(last_c_new)
        last_c_new += 1
        tree[c_new_name] = {ci:0, cj:0}
        tree[ci].update({c_new_name:0})
        tree[cj].update({c_new_name:0})
        age[c_new_name] = matrix[x][y] / 2
        join_table(matrix, x, y)
        del clusters[ci]
        del clusters[cj]
        clusters[c_new_name] = c_new

    root = list(clusters.keys())[0]
    edge_count = 0
    for node in tree:
        neighbors = tree[node]
        neighbor_keys = neighbors.keys()
        for neighbor in neighbor_keys:
            neighbors[neighbor] = abs(age[node] - age[neighbor])
            edge_count += 1
    return tree

n, matrix = process_file('data/problem4.txt')
tree = upgma(matrix, n)

for node in tree:
    neighbors = tree[node]
    neighbor_keys = neighbors.keys()
    for neighbor in neighbor_keys:
        print('{}->{}:{}'.format(node,neighbor, neighbors[neighbor]))
    