with open('input') as f:
    s = f.read().strip().split('\n')

grid = [[int(num) for num in line] for line in s]

count = 0

def flash(x, y):
    global count
    count += 1
    flashed[x][y] = True
    for offset in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        x_offset, y_offset = offset
        if x+x_offset >= 0 and x+x_offset < len(grid) and y+y_offset >= 0 and y+y_offset < len(grid[0]):
            grid[x+x_offset][y+y_offset] += 1

    for offset in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        x_offset, y_offset = offset
        if x+x_offset >= 0 and x+x_offset < len(grid) and y+y_offset >= 0 and y+y_offset < len(grid[0]):
            if not flashed[x+x_offset][y+y_offset] and grid[x+x_offset][y+y_offset] > 9:
                flash(x+x_offset, y+y_offset)


for step in range(100000):
    flashed = [[False for num in line] for line in s]
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            grid[x][y] += 1

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if not flashed[x][y] and grid[x][y] > 9:
                flash(x, y)
    
    all_flash = True
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            all_flash = all_flash and flashed[x][y]
            if flashed[x][y]:
                grid[x][y] = 0

    if all_flash:
        print(step+1)
        break

print(grid)
print(count)