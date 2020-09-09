def d_star(matrix):
    n = len(matrix)
    totals = [0]*n
    d_star_mat = [[0]*n for _ in range(n)]
    for i in range(len(matrix)):
        totals[i] = sum(matrix[i])
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            d_star_mat[i][j] = (n-2)*matrix[i][j] - totals[i] - totals[j]

    return d_star_mat

print(d_star(test_mat)[2][3])