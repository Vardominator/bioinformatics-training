def prefix(s, k):
    return s[0:k - 1]

def suffix(s, k):
    return s[-k + 1:]

def overlap(patterns):
    k = len(patterns[0])
    overlaps = {}
    for i in range(len(patterns)):
        overlaps[patterns[i]] = []
        for j in range(len(patterns)):
            if i != j and suffix(patterns[i], k) == prefix(patterns[j], k):
                overlaps[patterns[i]].append(patterns[j])
    return overlaps

with open('data/d4.txt', 'r') as f:
    patterns = f.read().splitlines()
    overlaps = overlap(patterns)
    with open('data/d4results.txt', 'w') as fout:
        for k in overlaps:
            if overlaps[k]:
                fout.write('{} -> {}\n'.format(k, ','.join(n for n in overlaps[k])))