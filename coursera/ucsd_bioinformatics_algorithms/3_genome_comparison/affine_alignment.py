from collections import OrderedDict
import re

SIGMA = 11
EPSILON = 1
SCORES = {}

with open('data/blosum62.txt', 'r') as stream:
    SCORES = OrderedDict({k:{} for k in re.split('\s+', stream.readline().strip())})
    for row in stream.readlines():
        vals = re.split('\s+', row.strip())
        i = 1
        for letter in SCORES.keys():
            SCORES[vals[0]][letter] = int(vals[i])
            i += 1

def backtrack(v, w):
    lower = [[0]*(len(w) + 1) for _ in range(len(v) + 1)]
    middle = [[0]*(len(w) + 1) for _ in range(len(v) + 1)]
    upper = [[0]*(len(w) + 1) for _ in range(len(v) + 1)]

    for i in range(1, len(v) + 1):
        lower[i][0] = -1*(SIGMA + EPSILON*(i - 1))
        middle[i][0] = -1*(SIGMA + EPSILON*(i - 1))
        upper[i][0] = -1*float("inf")

    for j in range(1, len(w) + 1):
        upper[0][j] = -1*(SIGMA + EPSILON*(j - 1))
        middle[0][j] = -1*(SIGMA + EPSILON*(j - 1))
        lower[0][j] = -1*float("inf")

    lower_backtrack = [[0]*(len(w) + 1) for _ in range(len(v) + 1)]
    middle_backtrack = [[0]*(len(w) + 1) for _ in range(len(v) + 1)]
    upper_backtrack = [[0]*(len(w) + 1) for _ in range(len(v) + 1)]
    for i in range(0, len(v) + 1):
        lower_backtrack[i][0] = ('↓','')
        middle_backtrack[i][0] = ('↘','')
        upper_backtrack[i][0] = ('→','')
    for j in range(0, len(w) + 1):
        lower_backtrack[0][j] = ('↓','')
        middle_backtrack[0][j] = ('↘','')
        upper_backtrack[0][j] = ('→','')

    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            # lower backtrack
            # lower[i][j] = max(lower[i-1][j] - EPSILON, middle[i-1][j] - SIGMA)
            if lower[i-1][j] - EPSILON >= middle[i-1][j] - SIGMA:
                lower[i][j] = lower[i-1][j] - EPSILON
                lower_backtrack[i][j] = ('↓','lower')
            else:
                lower[i][j] = middle[i-1][j] - SIGMA
                lower_backtrack[i][j] = ('↘','middle')

            # middle backtrack
            # upper[i][j] = max(upper[i][j-1] - EPSILON, middle[i][j-1] - SIGMA)
            if upper[i][j-1] - EPSILON >= middle[i][j-1] - SIGMA:
                upper[i][j] = upper[i][j-1] - EPSILON
                upper_backtrack[i][j] = ('→','upper')
            else:
                upper[i][j] = middle[i][j-1] - SIGMA
                upper_backtrack[i][j] = ('↘', 'middle')

            # higher backtrack
            # middle[i][j] = max(lower[i][j], middle[i-1][j-1] + SCORES[v[i-1]][w[j-1]], upper[i][j])
            if lower[i][j] >= middle[i-1][j-1] + SCORES[v[i-1]][w[j-1]] and lower[i][j] >= upper[i][j]:
                middle[i][j] = lower[i][j]
                middle_backtrack[i][j] = ('↓','lower')
            elif middle[i-1][j-1] + SCORES[v[i-1]][w[j-1]] >= lower[i][j] and middle[i-1][j-1] + SCORES[v[i-1]][w[j-1]] >= upper[i][j]:
                middle[i][j] = middle[i-1][j-1] + SCORES[v[i-1]][w[j-1]]
                middle_backtrack[i][j] = ('↘','middle')
            else:
                middle[i][j] = upper[i][j]
                middle_backtrack[i][j] = ('→','upper')

    return [lower, middle, upper], [lower_backtrack, middle_backtrack, upper_backtrack], middle[-1][-1]

def construct(btracks, v, w, i, j):
    alignmentv = ''
    alignmentw = ''

    lower_backtrack = btracks[0]
    middle_backtrack = btracks[1]
    upper_backtrack = btracks[2]

    curr_level = middle_backtrack[i][j][1]
    prev_level = curr_level

    while i > 0 and j > 0:
        if curr_level == 'lower':
            curr_level = lower_backtrack[i][j][1]
            alignmentw += '-'
            alignmentv += v[i - 1]
            i -= 1
        elif curr_level == 'middle':
            curr_level = middle_backtrack[i][j][1]
            if curr_level == 'lower':
                alignmentv += v[i - 1]
                alignmentw += '-'
                i -= 1
            elif curr_level == 'upper':
                alignmentw += w[j - 1]
                alignmentv += '-'
                j -= 1
            else:
                alignmentv += v[i - 1]
                alignmentw += w[j - 1]
                i -= 1
                j -= 1
        else:
            curr_level = upper_backtrack[i][j][1]
            alignmentv += '-'
            alignmentw += w[j - 1]
            j -= 1
            
    return ''.join([l for l in reversed(alignmentv)]), ''.join([l for l in reversed(alignmentw)])


with open('data/week3problem1.txt', 'r') as stream:
    v = stream.readline().strip()
    w = stream.readline().strip()

if len(w) > len(v):
    w, v = v, w

levels, btracks, max_score = backtrack(v, w)

alignedv, alignedw = construct(btracks, v, w, len(v), len(w))

print(max_score)
print(alignedv)
print(alignedw)
