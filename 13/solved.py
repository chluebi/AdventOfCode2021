with open('input') as f:
    s = f.read().split('\n\n')

dots, folds = s

SIZE = 2000

grid = [[False for i in range(SIZE)] for i in range(SIZE)]
for dot in dots.split('\n'):
    x, y = dot.split(',')
    x = int(x)
    y = int(y)
    grid[x][y] = True

count = 0
for j in range(SIZE):
    for i in range(SIZE):
        # print(1 if grid[i][j] else 0, end='')
        if grid[i][j] == True:
            count += 1
    # print('\n', end='')

print('\n\n')

# 12
for i in range(12):
    print(i)
    fold = folds.split('\n')[i]
    text, fold = fold.split(' along ')
    coord, num = fold.split('=')
    num = int(num)
    
    for i in range(SIZE):
        for j in range(SIZE):
            if coord == 'x':
                if i > num:
                    if grid[i][j] == True:
                        grid[num-(i-num)][j] = True
                if i >= num:
                    grid[i][j] = False
            elif coord == 'y':
                if j > num:
                    if grid[i][j] == True:
                        grid[i][num-(j-num)] = True
                if j >= num:
                    grid[i][j] = False

with open('output', 'w+') as f:
    count = 0
    for j in range(SIZE):
        for i in range(SIZE):
            # print(str(1 if grid[i][j] else 0), end='')
            f.write(str(1 if grid[i][j] else 0))
            if grid[i][j] == True:
                count += 1
        # print('\n', end='')
        f.write('\n')

print(count)