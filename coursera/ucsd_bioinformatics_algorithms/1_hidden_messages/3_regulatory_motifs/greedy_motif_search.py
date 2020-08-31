def Count(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {'A':[0] * k,'T':[0] * k,'C':[0] * k,'G':[0] * k}
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def Profile(Motifs):
    count = Count(Motifs)
    t = len(Motifs)
    k = len(Motifs[0])
    for i in count.keys():
        for j in range(k):
            count[i][j] /= t
    return count

def Consensus(Motifs):
    count = Count(Motifs)
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
    
def Pr(Text, Profile):
    p = 1
    for i,t in enumerate(Text):
        p *= Profile[t][i] 
    return p

def ProfileMostProbableKmer(text, k, profile):
    max_p = 0
    max_p_text = text[0:k]
    for i in range(len(text) - k + 1):
        if Pr(text[i:i+k], profile) > max_p:
            max_p = Pr(text[i:i+k], profile)
            max_p_text = text[i:i+k]
    return max_p_text

def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n - k + 1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs



profile = {
    'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
    'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
    'G': [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
    'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]
}

print(Pr('AAGAGA', profile))
print(Pr('ACGTTA', profile))
print(Pr('AAGCTA', profile))
print(Pr('TCGCGA', profile))
print(Pr('AGGTCA', profile))
print(Pr('ACGCGA', profile))

