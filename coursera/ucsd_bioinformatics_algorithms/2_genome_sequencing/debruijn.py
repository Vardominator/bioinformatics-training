from collections import OrderedDict

def prefix(s, k):
    return s[0:k - 1]

def suffix(s, k):
    return s[-k + 1:]

with open('data/d5.txt', 'r') as f:
    k_mers = f.read().splitlines()
print(k_mers)

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


with open('data/d5results.txt', 'w') as fout:
    for s in graph:
        if graph[s]:
            fout.write('{} -> {}\n'.format(s, ','.join(n for n in graph[s])))