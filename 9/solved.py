from collections import Counter

with open('input') as f:
    s = f.read().strip().split('\n')

grid = [[int(num) for num in line] for line in s]
where_flow = [[[] for num in line] for line in s]

count = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == 9:
            continue
        
        if grid[x][y] == 4:
            print(grid[x][y] == 4)

        for offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x_offset, y_offset = offset
            if not (x+x_offset < 0  or y+y_offset < 0 or x+x_offset > len(grid)-1 or y+y_offset > len(grid[0])-1):
                if grid[x][y] > grid[x+x_offset][y+y_offset]:
                    where_flow[x][y].append((x+x_offset, y+y_offset))

print(where_flow)

flow = [[0 for num in line] for line in s]

def dfs(x, y):
    if len(where_flow[x][y]) == 0:
        if not visited[x][y]:
            flow[x][y] += 1
    visited[x][y] = True
    for child in where_flow[x][y]:
        dfs(child[0], child[1])

for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == 9:
            continue
        visited = [[False for num in line] for line in s]
        dfs(x, y)

flat_flow = []
for x in range(len(grid)):
    for y in range(len(grid[0])):
        flat_flow.append(flow[x][y])

flat_flow.sort(reverse=True)
print(flat_flow[0]*flat_flow[1]*flat_flow[2])