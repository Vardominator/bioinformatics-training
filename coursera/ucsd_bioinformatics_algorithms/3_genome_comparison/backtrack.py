def lcs_backtrack(v, w):
    grid = [[0]*(len(w) + 1) for _ in range(len(v) + 1)]
    for i in range(0, len(v)):
        grid[i][0] = 0
    for j in range(0, len(w)):
        grid[0][j] = 0
    
    backtrack = [[0]*(len(w) + 1) for _ in range(len(v) + 1)]
    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            match = 0
            if v[i-1] == w[j-1]:
                match = 1
            grid[i][j] = max(grid[i-1][j], grid[i][j-1], grid[i-1][j-1] + match)
            if grid[i][j] == grid[i-1][j]:
                backtrack[i][j] = '↓'
            elif grid[i][j] == grid[i][j-1]:
                backtrack[i][j] = '→'
            elif grid[i][j] == grid[i-1][j-1] + match:
                backtrack[i][j] = '↘'

    return backtrack

def output_lcs(backtrack, v, i, j):
    lcs = []
    while i > 0 and j > 0:
        if backtrack[i][j] == '↘':
            lcs.append(v[i - 1])
            i -= 1
            j -= 1
        elif backtrack[i][j] == '↓':
            i -= 1
        else:
            j -= 1

    return ''.join([l for l in reversed(lcs)])

with open('data/week1problem3.txt', 'r') as stream:
    v = stream.readline().strip()
    w = stream.readline().strip()

v = "CCAATACGAC"
w = "GCCTTACGCT"
w2 = "CCCTAGCGGC"

res = output_lcs(lcs_backtrack(v, w), v, len(v), len(w))
print(output_lcs(lcs_backtrack(res, w2), res, len(res), len(w2)))
