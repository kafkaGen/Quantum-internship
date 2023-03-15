def dfs(grid, i, j):
    # base case: stop if we encounter water or out of bounds
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
        return
    # mark current cell as visited
    grid[i][j] = 0
    # explore neighboring cells recursively
    dfs(grid, i-1, j)
    dfs(grid, i+1, j)
    dfs(grid, i, j-1)
    dfs(grid, i, j+1)

def count_islands(grid):
    # count number of islands
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(grid, i, j)
                count += 1
    return count

# read input
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

# count number of islands
print(count_islands(grid))