from queue import PriorityQueue

with open('input') as f:
    s = f.read().strip().split('\n')

grid = [[int(x) for x in line] for line in s]
new_grid = [[0 for i in range((len(grid)*5))] for j in range((len(grid[0])*5))]
for i in range(len(grid)*5):
    for j in range(len(grid[0])*5):
        x_tile = i // (len(grid))
        y_tile = j // (len(grid[0]))
        old_x = i % (len(grid))
        old_y = j % (len(grid[0]))
        extra_danger = x_tile + y_tile
        new_grid[i][j] = grid[old_x][old_y] + extra_danger
        while new_grid[i][j] > 9:
            new_grid[i][j] -= 9
grid = new_grid
print(grid)

d = [[1000000000000 for y in range(len(grid[0]))] for x in range(len(grid))]
v = [[False for y in range(len(grid[0]))] for x in range(len(grid))]

d[0][0] = 0
v[0][0] = True

q = PriorityQueue()
q.put((0, (0, 0)))

def adjacent(coords):
    adj = []
    x, y = coords
    for offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x_offset, y_offset = offset
        if (x+x_offset >= 0) and (y+y_offset >= 0) and (x+x_offset < len(grid)) and (y+y_offset < len(grid[0])):
            adj.append((x+x_offset, y+y_offset))
    return adj


while not q.empty():
    node = q.get()
    print(node)
    n_x, n_y = node[1]
    for adj in adjacent(node[1]):
        x, y= adj
        if not v[x][y]:
            d[x][y] = d[n_x][n_y] + grid[x][y]
            v[x][y] = True
            q.put((d[x][y], (x, y)))
        else:
            if (d[x][y] > d[n_x][n_y] + grid[x][y]):
                d[x][y] = d[n_x][n_y] + grid[x][y]
                q.put((d[x][y], (x, y)))

print(len(grid), len(grid[0]))
print(d[len(grid)-1][len(grid[0])-1])