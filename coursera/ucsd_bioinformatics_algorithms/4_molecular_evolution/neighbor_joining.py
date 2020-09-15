def d_star(matrix):
    n = len(matrix)
    totals = [0]*n
    d_star_mat = [[0]*n for _ in range(n)]
    for i in range(len(matrix)):
        totals[i] = sum(matrix[i])
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j:
                d_star_mat[i][j] = (n-2)*matrix[i][j] - totals[i] - totals[j]

    return d_star_mat

d = [
[0,11,11],
[11,0,15],
[11,15,0]
]

for row in d:
    print(sum(row))

print()

for row in d_star(d):
    print('\t'.join([str(r) for r in row]))