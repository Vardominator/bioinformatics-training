def HammingDistance(p, q):
    return len([i for i in range(len(p)) if p[i] != q[i]])

# Generate the reverse complements of "possible kmers"
nucs = { 'A' : 'T', 'C' : 'G', 'G' : 'C', 'T' : 'A'}
RCDict = {}
RCList = []
def RevComplement(kmerList):
    for kmer in kmerList:
        c = ''
        for letter in kmer:
            c += nucs[letter]
        rc = c[::-1]
        RCList.append(rc)
        RCDict[kmer] = rc
    return(RCDict)


# Count how many times each possible kmer and its reverse complement appear within Text
import itertools   # to be used for generating possible kmers
def Count_pattern(text, k, d):
    # Generate the "possible kmers"
    kmers = list(itertools.product('ACTG', repeat=k))
    kmers = [''.join(kmer) for kmer in kmers]

    countDict = {}  # initiate dictionary to count kmers and reverse complements (rc) found, as well as their mismatches
    RCDict = RevComplement(kmers) # dictionary with kmer and rc pairs
    kmerList = list(RCDict.keys())  # list of kmers in order
    rcList = list(RCDict.values())  # list of rc's in corresponding order

    for kmer in kmerList:
        countDict[kmer] = 0
    for i in range(len(kmerList)):
        for j in range(len(text)-k+1):
            word = text[j:j+k]
            
            # kmer and kmer mismatches
            hamming1 = HammingDistance(word, kmerList[i])
            if hamming1 <= d:
                forCount1 = (kmerList[i]).strip("'")
                countDict[forCount1] += 1

            # rc and rc mismatches
            hamming2 = HammingDistance(word, rcList[i])
            if hamming2 <= d:
                forCount2 = (kmerList[i]).strip("'")
                countDict[forCount2] += 1
            
    # most frequent kmer and rc
    #print(countDict)
    maxCount = max(countDict.values())
    returnPair = []
    for key in countDict.keys():
        if maxCount == 0:
            return('no frequent kmer or reverse complement!')
        else:
            if countDict[key] == maxCount:
                returnKmer = key
                returnRC = RCDict[key]

    returnPair.append(returnKmer)
    returnPair.append(returnRC)
    returnPair = ' '.join(item for item in returnPair)

    return(returnPair)


with open("data/dataset_9_8.txt", 'r') as f:
    data = f.read().splitlines()

genome = data[0]
k, d = data[1].split(' ')

print(Count_pattern(genome, int(k), int(d)))