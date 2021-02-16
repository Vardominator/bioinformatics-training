

def find_occurrence_index(col, index):
    occurence = 0
    i = 0
    while i < index:
        if col[i] == col[index]:
            occurence += 1
        i += 1
    return occurence

def find_nth_occurence_index(col, n, c):
    count = -1
    for i in range(len(col)):
        if col[i] == c:
            count += 1
            if n == count:
                return i 


def inverse(bwt):
    last_col = bwt
    first_col = sorted(bwt)
    first_col = ''.join([c for c in first_col])
    curr_index = 0
    curr_char = last_col[0]
    genome = ''
    while len(genome) < len(first_col):
        genome += curr_char
        occurrence = find_occurrence_index(last_col, curr_index)
        curr_index = find_nth_occurence_index(first_col, occurrence, curr_char)
        curr_char = last_col[curr_index]
    return genome[:-1][::-1] + '$'

with open('data/dataset_299_10.txt', 'r') as stream:
    bwt = stream.readline().strip()
    genome = inverse(bwt)
    with open('output/dataset_299_10.txt', 'w') as stream:
        stream.write(genome)