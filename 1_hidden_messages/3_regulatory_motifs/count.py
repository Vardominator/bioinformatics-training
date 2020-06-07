def Count(Motifs):
    count = {}
    t = len(Motifs)
    k = len(Motifs[0])
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            if symbol not in count:
                count[symbol] = [0] * k
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