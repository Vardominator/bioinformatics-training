from collections import OrderedDict
import re

with open('data/scoring_matrix.txt', 'r') as stream:
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
    for i in range(0, len(v)):
        grid[i][0] = -5 * i
    for j in range(0, len(w)):
        grid[0][j] = -5 * j

    max_score = -100000
    start_i = -1
    start_j = -1

    backtrack = [[0]*(len(w) + 1) for _ in range(len(v) + 1)]
    for i in range(0, len(v) + 1):
        backtrack[i][0] = '↓'
    for j in range(0, len(w) + 1):
        backtrack[0][j] = '→'

    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            mu = scores[v[i-1]][w[j-1]]
            grid[i][j] = max(0, grid[i-1][j] - SIGMA, grid[i][j-1] - SIGMA, grid[i-1][j-1] + mu)
            if grid[i][j] > max_score:
                max_score = grid[i][j]
                start_i = i
                start_j = j
            # if grid[i][j] == grid[i-1][j] - SIGMA:
            #     backtrack[i][j] = '↓'
            # elif grid[i][j] == grid[i][j-1] - SIGMA:
            #     backtrack[i][j] = '→'
            # elif grid[i][j] == grid[i-1][j-1] + mu:
            #     backtrack[i][j] = '↘'
    for g in grid:
        print(g)

    return grid, max_score, start_i, start_j

def construct(grid, v, w, i, j):
    alignmentv = v[i-1]
    alignmentw = w[j-1]
    while i > 0 and j > 0:
        if grid[i-1][j-1] == 0 and grid[i][j-1] == 0 and grid[i-1][j] == 0:
            break
        if grid[i-1][j-1] >= grid[i-1][j] and grid[i-1][j-1] >= grid[i][j-1]:
            i -= 1
            j -= 1
            alignmentv += v[i - 1]
            alignmentw += w[j - 1]            
        elif grid[i-1][j] >= grid[i-1][j-1] and grid[i-1][j] >= grid[i][j-1]:
            alignmentw += '-'           
            i -= 1
            alignmentv += v[i - 1]
        elif grid[i][j-1] >= grid[i-1][j-1] and grid[i][j-1] >= grid[i-1][j]:
            alignmentv += '-'    
            j -= 1
            alignmentw += w[j - 1]
            
    return ''.join([l for l in reversed(alignmentv)]), ''.join([l for l in reversed(alignmentw)])

with open('data/week2problem2.txt', 'r') as stream:
    v = stream.readline().strip()
    w = stream.readline().strip()

grid, score, start_i, start_j = lcs_backtrack(v, w)

alignedv, alignedw = construct(grid, v, w, start_i, start_j)
print(score)
print(alignedv)
print(alignedw)

