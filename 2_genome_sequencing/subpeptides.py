def subpeptides(s):
    subs = []
    looped = s + s
    for i in range(len(s)):
        for j in range(1, len(s)):
            subs.append(looped[i:i + j])
    return subs

def spectrum(subpeptides, mass_table):
    masses = [0]
    for peptide in subpeptides:
        curr_sum = 0
        for c in peptide:
            curr_sum += mass_table[c]
        masses.append(curr_sum)
    masses.sort()
    return masses

mass_table = {}
with open('data/integer_mass_table.txt', 'r') as stream:
    for row in stream.read().splitlines():
        subpeptide, mass = row.split(' ')
        mass_table[subpeptide] = int(mass)

# with open('data/dataset_98_4.txt', 'r') as stream:
#     p = stream.readline().strip()
#     peptides = subpeptides(p)

# # peptides = subpeptides("LEQN")
# peptides.append(p)
# masses = [0]
# for peptide in peptides:
#     curr_sum = 0
#     for c in peptide:
#         curr_sum += mass_table[c]
#     masses.append(curr_sum)


# with open('data/dataset_98_4_result.txt', 'w') as stream:
#     stream.write(" ".join([str(m) for m in masses]))


spectrum = [0, 57, 118, 179, 236, 240, 301]
diffs = {}
for n in spectrum:
    for l in spectrum:
        d = abs(n - l)
        if d in diffs:
            diffs[d] += 1
        else:
            diffs[d] = 1

import operator
print(diffs)
print(max(diffs.items(), key=operator.itemgetter(1))[0])