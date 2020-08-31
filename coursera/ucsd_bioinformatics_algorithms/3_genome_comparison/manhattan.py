n, m = 3, 3

grid = [[0]*m for _ in range(n)]

for i in range(n):
    grid[i][0] = 1

for j in range(m):
    grid[0][j] = 1

for i in range(1, n):
    for j in range(1, m):
        grid[i][j] = grid[i][j - 1] + grid[i - 1][j]


def manhattan_tourist(n, m, down, right):
    grid = [[0]*(m + 1) for _ in range(n + 1)]
    for i in range(1, n):
        grid[i][0] = grid[i - 1][0] + down[i - 1][0]
    for j in range(1, m):
        grid[0][j] = grid[0][j - 1] + right[0][j - 1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            grid[i][j] = max(grid[i - 1][j] + down[i - 1][j], grid[i][j - 1] + right[i][j - 1])
    print(grid)
    return grid[-1][-1]

down = []
right = []
with open('data/week1problem2.txt', 'r') as stream:
    n, m = stream.readline().strip().split(' ')
    line = stream.readline().strip()
    while line != '-':
        down.append([int(s) for s in line.split(' ')])
        line = stream.readline().strip()
    
    right_str = stream.readlines()
    for r in right_str:
        right.append([int(s) for s in r.split(' ')])

print(down)
print(right)
print(manhattan_tourist(int(n), int(m), down, right))