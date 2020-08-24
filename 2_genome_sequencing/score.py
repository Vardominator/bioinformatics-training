def subpeptides(s):
    subs = []
    looped = s + s
    for i in range(0, len(s)):
        for j in range(1, len(s)):
            subs.append(looped[i:i + j])
    subs.append(s)
    return subs

def linear_subpeptides(s):
    subs = []
    for i in range(0, len(s)):
        for j in range(i, len(s)):
            subs.append(s[i:i + j])
    subs.append(s)
    # print(subs)
    return subs

def spectrum_masses(subpeptides, mass_table):
    masses = [0]
    for peptide in subpeptides:
        curr_sum = 0
        for c in peptide:
            curr_sum += mass_table[c]
        masses.append(curr_sum)
    masses.sort()
    return masses

def score(peptide, spectrum, mass_table):
    cyclospectrum = spectrum_masses(subpeptides(peptide), mass_table)
    score = 0
    for m in set(spectrum):
        score += min(cyclospectrum.count(m), spectrum.count(m))
    return score

def linear_score(peptide, spectrum, mass_table):
    linear_spectrum = spectrum_masses(linear_subpeptides(peptide), mass_table)
    score = 0
    for m in set(spectrum):
        score += min(linear_spectrum.count(m), spectrum.count(m))
    return score

mass_table = {}
with open('data/integer_mass_table.txt', 'r') as stream:
    for row in stream.read().splitlines():
        subpeptide, mass = row.split(' ')
        mass_table[subpeptide] = int(mass)


with open('data/dataset_4913_1.txt', 'r') as stream:
    peptide = stream.readline().strip()
    spectrum = [int(s) for s in stream.readline().strip().split(' ')]


# print(score("MAMA", [0, 71, 98, 99, 131, 202, 202, 202, 202, 202, 299, 333, 333, 333, 503], mass_table))
print(linear_score(peptide, spectrum, mass_table))