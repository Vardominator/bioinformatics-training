import re

def find_match_indices(text, pattern):
    return [m.start() for m in re.finditer(pattern, text)]

with open('data/part3.txt', 'r') as stream:
    text = stream.readline().strip()
    patterns = stream.read().splitlines()
    indices = []
    for pattern in patterns:
        indices.extend(find_match_indices(text, pattern))

    indices = set(indices)
    indices = list(indices)
    indices.sort()
    with open('output/part3.txt', 'w') as stream:
        stream.write(' '.join([str(i) for i in indices]))