import math 
import random

def distance(v, w):
    d = 0
    for i in range(len(v)):
        d += pow((v[i] - w[i]), 2)
    return math.sqrt(d)

def min_distance(v, centers):
    min_d = 10000000
    min_distance_center = None
    center_i = None
    for i in range(len(centers)):
        # min_d = min(min_d, distance(v, center))
        if distance(v, centers[i]) <= min_d:
            min_d = distance(v, centers[i])
            min_distance_center = centers[i]
            center_i = i
    return min_d, min_distance_center, center_i

def max_distance(data, centers):
    max_distance = -10000000
    max_distance_point = None
    for datapoint in data:
        min_d = min_distance(datapoint, centers)
        if min_d >= max_distance:
            max_distance = min_d
            max_distance_point = datapoint
    return max_distance, max_distance_point

def distortion(data, centers):
    return float("{:.3f}".format(sum([pow(min_distance(d, centers), 2) for d in data]) / len(data)))

def farthest_first_traversal(data, k):
    # centers = [random.choice(data)]
    centers = [data[0]]
    while len(centers) < k:
        _, new_datapoint = max_distance(data, centers)
        centers.append(new_datapoint)
    return centers

def center_of_gravity(data):
    return [float("{:.3f}".format(sum(x)/len(data))) for x in zip(*data)]

def k_means_plusplus_init(data, k):
    centers = [random.choice(data)]
    while len(centers) < k:
        weights = [0]*len(data)
        for i in range(len(data)):
            min_d,_,_ = min_distance(data[i], centers)
            weights[i] = min_d
        new_point = random.choices(data, weights=weights, k=1)[0]
        centers.append(new_point)
    return centers

def k_means(data, k):
    last_centers = k_means_plusplus_init(data, k)
    while True:
        cluster_assignments = {i:[] for i in range(k)}
        for d in data:
            _, nearest_center, center_i = min_distance(d, last_centers)
            cluster_assignments[center_i].append(d)
        centers = []
        for i in cluster_assignments.keys():
            new_center = center_of_gravity(cluster_assignments[i])
            centers.append(new_center)
        if centers == last_centers:
            break
        last_centers = list(centers)
    return last_centers
        

# with open('data/problem1.txt', 'r') as stream:
#     k = int(stream.readline().strip().split(' ')[0])
#     data = []
#     point_strs = stream.readlines()
#     for point_str in point_strs:
#         data.append([float(p) for p in point_str.strip().split(' ')])

# with open('output/problem1.txt', 'w') as stream:
#     for point in farthest_first_traversal(data, k):
#         stream.write(' '.join([str(p) for p in point]) + '\n')

# with open('data/problem2.txt', 'r') as stream:
#     k = int(stream.readline().strip().split(' ')[0])
#     centers = []
#     data = []
#     line = stream.readline()
#     while '-' not in line:
#         centers.append([float(p) for p in line.strip().split(' ')])
#         line = stream.readline()

#     point_strs = stream.readlines()
#     for point_str in point_strs:
#         data.append([float(p) for p in point_str.strip().split(' ')])

with open('data/problem3.txt', 'r') as stream:
    k = int(stream.readline().strip().split(' ')[0])
    data = []
    point_strs = stream.readlines()
    for point_str in point_strs:
        data.append([float(p) for p in point_str.strip().split(' ')])

clusters = k_means(data, k)

with open('output/problem3.txt', 'w') as stream:
    for point in clusters:
        stream.write(' '.join([format(p, '.3f') for p in point]) + '\n')
