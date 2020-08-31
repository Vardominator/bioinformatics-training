from collections import OrderedDict
import re

with open('data/blosum62.txt', 'r') as stream:
    scores = OrderedDict({k:{} for k in re.split('\s+', stream.readline().strip())})
    for row in stream.readlines():
        vals = re.split('\s+', row.strip())
        i = 1
        for letter in scores.keys():
            scores[vals[0]][letter] = int(vals[i])
            i += 1

# indel penalty
SIGMA = 5

def lcs_backtrack(v, w):
    grid = [[0]*(len(w) + 1) for _ in range(len(v) + 1)]
    for i in range(0, len(v) + 1):
        grid[i][0] = -5 * i
    for j in range(0, len(w) + 1):
        grid[0][j] = -5 * j

    backtrack = [[0]*(len(w) + 1) for _ in range(len(v) + 1)]
    for i in range(0, len(v) + 1):
        backtrack[i][0] = '↓'
    for j in range(0, len(w) + 1):
        backtrack[0][j] = '→'

    max_score = -100000
    start_i = -1
    start_j = -1

    print(len(v) * len())
    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            mu = scores[v[i-1]][w[j-1]]
            grid[i][j] = max(grid[i-1][j] - SIGMA, grid[i][j-1] - SIGMA, grid[i-1][j-1] + mu)
            if grid[i][j] >= max_score:
                max_score = grid[i][j]
                start_i = i
                start_j = j
            if grid[i][j] == grid[i-1][j] - SIGMA:
                backtrack[i][j] = '↓'
            elif grid[i][j] == grid[i][j-1] - SIGMA:
                backtrack[i][j] = '→'
            elif grid[i][j] == grid[i-1][j-1] + mu:
                backtrack[i][j] = '↘'

    return backtrack, max_score, start_i, start_j

def alignment(backtrack, v, w, i, j):
    alignmentv = ''
    alignmentw = ''
    while i > 0 and j > -1:
        if backtrack[i][j] == 0:
            break
        if backtrack[i][j] == '↘':
            alignmentv += v[i - 1]
            alignmentw += w[j - 1]
            i -= 1
            j -= 1
        elif backtrack[i][j] == '↓':
            alignmentv += v[i - 1]
            alignmentw += '-'
            i -= 1
        else:
            alignmentw += w[j - 1]
            alignmentv += '-'
            j -= 1
             
    return ''.join([l for l in reversed(alignmentv)]), ''.join([l for l in reversed(alignmentw)])

with open('data/week2problem1.txt', 'r') as stream:
    v = stream.readline().strip()
    w = stream.readline().strip()

if len(w) > len(v):
    w, v = v, w


backtrack, max_score, start_i, start_j = lcs_backtrack(v, w)

alignedv, alignedw = alignment(backtrack, v, w, start_i, start_j)
final_score = 0
for i in range(len(alignedv)):
    if alignedv[i] == alignedw[i]:
        final_score += scores[alignedv[i]][alignedw[i]]
    elif alignedv[i] == '-' or alignedw[i] == '-':
        if alignedv[i] == alignedw[i]:
            final_score -= 2*SIGMA
        else:
            final_score -= SIGMA
    else:
        final_score += scores[alignedv[i]][alignedw[i]]
    
print(final_score)
print(alignedv)
print(alignedw)
