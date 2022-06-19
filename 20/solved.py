
def get_neighbors(x, y, grid):
    bits = ''
    for y_offset, x_offset in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]:
        if (x+x_offset < 0 or x+x_offset >= len(grid[0]) or y+y_offset < 0 or y+y_offset >= len(grid)):
            bits += '0'
        else:
            bits += '1' if grid[y+y_offset][x+x_offset] else '0'

    return int(bits, 2)

def print_grid(grid):
    for y, line in enumerate(grid):
        l = ''
        for x, char in enumerate(line):
            l += '#' if char else '.'
        print(l)

def main():
    with open('input') as f:
        s = f.read().strip().split('\n\n')
    algorithm = s[0].replace('\n', '')
    print(algorithm)
    image = s[1].split('\n')

    grid = [[True if char == '#' else False for char in line] for line in image]
    print_grid(grid)

    new_grid = [[False for i in range(len(grid[0]) + 500)] for j in range(len(grid) + 500)]
    for i in range(len(new_grid)):
        for j in range(len(new_grid[i])):
            y = i - 250
            x = j - 250
            if (x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid)):
                new_grid[i][j] = False
            else:
                new_grid[i][j] = grid[y][x]

    print_grid(new_grid)
    grid = new_grid

    for k in range(50):
        print(k)
        new_grid = [[False for i in range(1, len(new_grid[0])-1)] for j in range(1, len(new_grid)-1)]

        for y, line in enumerate(new_grid):
            for x, char in enumerate(line):
                num = get_neighbors(x, y, grid)
                new_grid[y][x] = True if algorithm[num] == '#' else False

        #print_grid(new_grid)

        grid = new_grid

    count = 0
    for y, line in enumerate(new_grid):
        for x, char in enumerate(line):
            if new_grid[y][x]:
                count += 1
    print(count)


main()