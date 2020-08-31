import random 

def Consensus(Motifs):
    count = CountWithPseudocounts(Motifs)
    consensus = ['']*len(Motifs[0])
    maxes = [-1]*len(Motifs[0])
    for j in range(len(Motifs[0])):
        for i in count.keys():
            if count[i][j] > maxes[j]:
                maxes[j] = count[i][j]
                consensus[j] = i     
    return ''.join([c for c in consensus])

def Score(Motifs):
    consensus = Consensus(Motifs)
    score = 0
    for j in range(len(Motifs[0])):
        curr_score = 0
        for i in range(len(Motifs)):
            if Motifs[i][j] != consensus[j]:
                curr_score += 1
        score += curr_score
    return score

def Normalize(Probabilities):
    sum_vals = sum(Probabilities.values())
    for k in Probabilities.keys():
        Probabilities[k] /= sum_vals
    return Probabilities

def WeightedDie(Probabilities):
    kmer = ''
    u = random.uniform(0, 1)
    for p in Probabilities:
        u -= Probabilities[p]
        if u <= 0:
            return p

def Pr(Text, Profile):
    p = 1
    for i,t in enumerate(Text):
        p *= Profile[t][i] 
    return p

def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {}
    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)


def ProfileMostProbablePattern(text, k, profile):
    max_p = 0
    max_p_text = text[0:k]
    for i in range(len(text) - k + 1):
        if Pr(text[i:i+k], profile) > max_p:
            max_p = Pr(text[i:i+k], profile)
            max_p_text = text[i:i+k]
    return max_p_text

def RandomMotifs(Dna, k, t):
    rand_kmers = []
    for i in range(t):
        rand_k = random.randint(0, len(Dna[i]) - k)
        rand_kmers.append(Dna[i][rand_k:rand_k+k])
    return rand_kmers

def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {'A':[1] * k,'T':[1] * k,'C':[1] * k,'G':[1] * k}
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def ProfileWithPseudocounts(Motifs):
    count = CountWithPseudocounts(Motifs)
    t = len(Motifs)
    k = len(Motifs[0])
    for i in count.keys():
        for j in range(k):
            count[i][j] /= t
    return count

def Motifs(Profile, Dna):
    motifs = []
    for d in Dna:
        motifs.append(ProfileMostProbablePattern(d, len(Profile['A']), Profile))
    return motifs

def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M.copy()
    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs
    return BestMotifs

def GibbsSampler(Dna, k, t, N):
    BestMotifs = RandomMotifs(Dna, k, t)
    Motifs = BestMotifs.copy()
    for j in range(N):
        i = random.randint(0, t - 1)
        del Motifs[i]
        Profile = ProfileWithPseudocounts(Motifs)
        Motif_i = ProfileGeneratedString(Dna[i], Profile, k)
        Motifs.insert(i, Motif_i)      
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

with open('data/dataset_163_4.txt', 'r') as stream:
    params = stream.readline().strip().split(' ')
    dna = stream.read().splitlines()

k, t, N = int(params[0]), int(params[1]), int(params[2])


# min_score = 100000000
last_motifs = RandomizedMotifSearch(dna, int(k), int(t))
for i in range(500):
    print(i)
    bms = RandomizedMotifSearch(dna, int(k), int(t))
    if Score(bms) < Score(last_motifs):
        last_motifs = bms

# last_motifs = GibbsSampler(dna, k, t, N)
for i in range(20):
    print(i)
    bms = GibbsSampler(dna, k, t, N) 
    if Score(bms) < Score(last_motifs):
        last_motifs = bms

with open('data/dataset_163_4_result.txt', 'w') as stream:
    for lm in last_motifs:
        stream.write(lm + '\n')