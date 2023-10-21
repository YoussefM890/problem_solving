

def func(grid):
    visited = set()
    ones = 0
    n = len(grid)
    m = len(grid[0])
    # l = [[1 if i == 0 or i == n - 1 or j == 0 or j == n - 1 else 0 for j in range(n)] for i in range(n)]
    def explore(i, j):
        if (i, j) in visited or i not in range(0, n) or j not in range(0, m) or grid[i][j] == 0:
            return
        else:
            visited.add((i, j))
        explore(i + 1, j)
        explore(i - 1, j)
        explore(i, j + 1)
        explore(i, j - 1)

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 :
                ones += 1
                if (i in [0,n-1] or  j in [0,m-1]):
                    explore(i , j)
    return ones - len(visited)
grid = [[0],[1],[1],[0],[0]]
print(func(grid))
