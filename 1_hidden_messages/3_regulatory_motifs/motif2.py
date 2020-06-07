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
    t = len(Motifs) + 4
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

def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n - k + 1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))

        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs

    return BestMotifs