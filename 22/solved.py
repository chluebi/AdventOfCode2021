def part1():
    with open('input') as f:
        s = f.read().strip().split('\n')

    grid = [[[False for i in range(-50, 51)] for j in range(-50, 51)] for k in range(-50, 51)]

    for step in s:
        mode, coord = step.split(' ')
        coord = coord.split(',')

        x = coord[0][2:].split('..')
        x = [int(k) for k in x]

        y = coord[1][2:].split('..')
        y = [int(k) for k in y]

        z = coord[2][2:].split('..')
        z = [int(k) for k in z]

        print(mode, x, y, z)

        k = x[0]
        while k <= x[1]:
            if k < -50:
                k = -50
            if x[1] < -50:
                break
            if k > 50:
                break

            j = y[0]
            while j <= y[1]:
                if j < -50:
                    j = -50
                if y[1] < -50:
                    break
                if j > 50:
                    break

                i =  z[0]
                while i <= z[1]:
                    if i < -50:
                        i = -50
                    if z[1] < -50:
                        break
                    if i > 50:
                        break
                    
                    if mode == 'on':
                        grid[k][j][i] = True
                    elif mode == 'off':
                        grid[k][j][i] = False
                    else:
                        raise ValueError

                    i += 1
                j += 1
            k += 1

    count = 0
    for k in range(-50, 51):
        for j in range(-50, 51):
            for i in range(-50, 51):
                if(grid[k][j][i]):
                    count += 1
    
    print(count)


def part2():
    with open('input') as f:
        s = f.read().strip().split('\n')
    pass
    

part2()