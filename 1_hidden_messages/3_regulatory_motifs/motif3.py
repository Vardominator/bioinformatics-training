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

def ProfileWithPseudocounts(Motifs):
    count = CountWithPseudocounts(Motifs)
    t = len(Motifs)
    k = len(Motifs[0])
    for i in count.keys():
        for j in range(k):
            count[i][j] /= t
    return count
    
def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {'A':[1] * k,'T':[1] * k,'C':[1] * k,'G':[1] * k}
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def RandomMotifs(Dna, k, t):
    rand_kmers = []
    for i in range(t):
        rand_k = random.randint(0, len(Dna[i]) - k)
        rand_kmers.append(Dna[i][rand_k:rand_k+k])
    return rand_kmers

def Pr(Text, Profile):
    p = 1
    for i,t in enumerate(Text):
        p *= Profile[t][i] 
    return p

def ProfileMostProbablePattern(text, k, profile):
    max_p = 0
    max_p_text = text[0:k]
    for i in range(len(text) - k + 1):
        if Pr(text[i:i+k], profile) > max_p:
            max_p = Pr(text[i:i+k], profile)
            max_p_text = text[i:i+k]
    return max_p_text

def Motifs(Profile, Dna):
    motifs = []
    for d in Dna:
        motifs.append(ProfileMostProbablePattern(d, len(Profile['A']), Profile))
    return motifs

def RandomizedMotifSearch(Dna, k, t):
    M = ['CCA', 'CCT', 'CTT', 'TTG']
    BestMotifs = M.copy()
    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        print(M)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs
        print(BestMotifs)
        
Dna = [
"AAGCCAAA",
"AATCCTGG",
"GCTACTTG",
"ATGTTTTG"
]

print(RandomizedMotifSearch(Dna,3,4))
