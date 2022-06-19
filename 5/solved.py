import numpy as np

with open('input') as f:
    s = f.read().strip().split('\n')

lines = [[0 for i in range(1000)] for j in range(1000)]
for line in s:
    pos1, pos2 = line.strip().split('->')
    x1, y1 = pos1.split(',')
    x2, y2 = pos2.split(',')
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    x_dir = np.sign(x2-x1)
    y_dir = np.sign(y2-y1)

    x = x1
    y = y1
    while not (x == x2 and y == y2):
        lines[x][y] += 1
        x += x_dir
        y += y_dir
    
    lines[x][y] += 1

count = 0
for x in range(1000):
    for y in range(1000):
        if lines[x][y] >= 2:
            count+=1
print(count)