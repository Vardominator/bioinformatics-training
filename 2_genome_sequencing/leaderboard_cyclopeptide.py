import heapq

# MASS_TABLE = {}
# with open('data/integer_mass_table.txt', 'r') as stream:
#     for row in stream.read().splitlines():
#         subpeptide, mass = row.split(' ')
#         MASS_TABLE[subpeptide] = int(mass)

def mass(peptide):
    masses = [0]
    for p in peptide:
        curr_sum = 0
        for c in p:
            curr_sum += MASS_TABLE[c]
        masses.append(curr_sum)
    return sum(masses)

def parent_mass(peptide_masses):
    return peptide_masses[-1]

def linear_spectrum(peptide):
    prefix_mass = [0]*(len(peptide) + 1)
    for i in range(1, len(peptide) + 1):
        prefix_mass[i] = prefix_mass[i - 1] + MASS_TABLE[peptide[i - 1]]

    spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
    spectrum.sort()
    return spectrum

def score(peptide, spectrum):
    cyclospectrum = spectrum_masses(subpeptides(peptide))
    score = 0
    for m in set(spectrum):
        score += min(cyclospectrum.count(m), spectrum.count(m))
    return score

def linear_score(peptide, spectrum):
    ls = linear_spectrum(peptide)
    score = 0
    for m in set(spectrum):
        score += min(ls.count(m), spectrum.count(m))
    return score

def trim(leaderboard, scores, spectrum, n):
    n = n - 1
    linear_scores = [0]*len(leaderboard)
    for j in range(len(leaderboard)):
        peptide = leaderboard[j]
        linear_scores[j] = scores[peptide]
    
    leaderboard = [l for _,l in sorted(zip(linear_scores, leaderboard), reverse=True)]
    linear_scores.sort(reverse=True)

    for j in range(n + 1, len(leaderboard)):
        if linear_scores[j] < linear_scores[n]:
            del leaderboard[j:]
            return leaderboard

    return leaderboard

def expand(leaderboard, scores, masses, spectrum):
    new_leaderboard = []
    for leader in leaderboard:
        for p in MASS_TABLE.keys():
            new_leader = leader + p
            masses[new_leader] = masses[leader] + MASS_TABLE[p]
            new_leaderboard.append(new_leader)
            scores[new_leader] = linear_score(new_leader, spectrum)
    return new_leaderboard

def leaderboard_cyclopeptide(spectrum, n):
    leaderboard = ['']
    scores = {'':0}
    masses = {'':0}
    leader_peptide = ''
    pm = parent_mass(spectrum)
    while leaderboard:
        leaderboard = expand(leaderboard, scores, masses, spectrum)
        print(leaderboard)
        for peptide in leaderboard.copy():
            peptide_mass = masses[peptide]
            if peptide_mass == pm:
                if scores[peptide] > linear_score(leader_peptide, spectrum):
                    leader_peptide = peptide
            elif peptide_mass > pm:
                leaderboard = [l for l in leaderboard if l != peptide]
                del scores[peptide]
                del masses[peptide]
        leaderboard = trim(leaderboard, scores, spectrum, n)
    return leader_peptide

def convolution(m, spectrum):
    diffs = {}
    for n in spectrum:
        for l in spectrum:
            d = abs(n - l)
            if d in diffs:
                diffs[d] += 1
            else:
                diffs[d] = 1   
    del diffs[0]

    for d in diffs.copy().keys():
        if d < 57 or d > 200:
            del diffs[d]

    largest = sorted(diffs.items(), key=lambda item: item[1], reverse=True)[:m]
    for d in list(diffs.items())[m:]:
        if d[1] == largest[-1][1]:
            largest.append(d)

    final_diffs = {k:v for k,v in largest}

    return final_diffs

def convolution_cyclopeptide(m, n, spectrum):
    global MASS_TABLE
    conv = convolution(m, spectrum)
    print(conv)
    count = '1'
    MASS_TABLE = {}
    for c in conv.keys():
        MASS_TABLE[count] = c
        count = chr(ord(count) + 1)
    return leaderboard_cyclopeptide(spectrum, n)


with open('data/convolution.txt', 'r') as stream:
    m = int(stream.readline().strip())
    n = int(stream.readline().strip())
    spectrum = sorted([int(s) for s in stream.readline().strip().split(' ')])

print(spectrum)
peptide = convolution_cyclopeptide(m, n, spectrum)
print(MASS_TABLE)
print(peptide)
print('-'.join([str(MASS_TABLE[s]) for s in peptide]))