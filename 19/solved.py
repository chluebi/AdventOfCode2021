import itertools
import numpy as np

rotations = [
    np.diag([1, 1, 1]),
    np.array([
        [1, 0, 0],
        [0, 0, 1],
        [0, 1, 0]]),
    np.array([
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 1]]),
    np.array([
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0]]),
    np.array([
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0]]),
    np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0]])
]

flips = [
    np.diag([1, 1, 1]),
    np.diag([1, 1, -1]),
    np.diag([1, -1, 1]),
    np.diag([1, -1, -1]),
    np.diag([-1, 1, 1]),
    np.diag([-1, 1, -1]),
    np.diag([-1, -1, 1]),
    np.diag([-1, -1, -1]),
]

def subtract(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]

def add(a, b):
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]

def minus(a):
    return (-a[0], -a[1], -a[2])

def main():
    with open('example') as f:
        s = f.read().strip().split('\n\n')

    scanners = [[[int(coord) for coord in line.split(',')] for line in passage.split('\n')[1:]] for passage in s]
    overlap = [[None for scanner in scanners] for scanner in scanners]

    for a_num, scanner_a in enumerate(scanners):
        for b_num, scanner_b in list(enumerate(scanners))[a_num:]:
            if scanner_a == scanner_b:
                continue
            for rot in rotations:
                for flip in flips:
                    perm = np.matmul(rot, flip)
                    dist = {}
                    for pos_a in scanner_a:
                        for pos_b in scanner_b:
                            perm_pos = np.matmul(perm, pos_a)
                            diff = subtract(pos_b, perm_pos)
                            if diff == [68, 1246, -43]:
                                print('HIIIIII', pos_b, perm_pos)
                            diff = tuple(diff)
                            if diff in dist:
                                dist[diff] += 1
                            else:
                                dist[diff] = 1
                    
                    match = False
                    for key, value in dist.items():
                        if value >= 12:
                            match = True
                            print('match', a_num, b_num, key, perm)
                            overlap[a_num][b_num] = (key, perm)
                            overlap[b_num][a_num] = (minus(key), np.linalg.inv(perm))
    
    print('overlap', overlap)
    print('overlap special', overlap[1][4])
    relative = [None for scanner in scanners]
    stack = [(0, (0, 0, 0), np.diag([1, 1, 1]))]
    while (len(stack) > 0):
        id, pos, perm = stack.pop()
        pos = tuple(pos)
        print(id, pos, perm)
        relative[id] = (pos, perm)
        for i, neighbor in enumerate(overlap[id]):
            if neighbor is not None:
                if relative[i] is None:
                    reverse_perm = np.linalg.inv(perm)
                    diff = np.matmul(perm, neighbor[0])
                    print('from', id, 'to', i)
                    print('neighbor',  i, neighbor[0], neighbor[1])
                    print('perm', perm)
                    new_dir = np.matmul(neighbor[1], perm)
                    stack.append((i, add(pos, diff), new_dir))

    print('relative', relative)
    beacons = set()
    for num, scanner in enumerate(scanners):
        dis = minus(relative[num][0])
        dir = np.linalg.inv(relative[num][1])
        for beacon in scanner:
            pos = tuple(beacon)
    

def test():
    pos = [1, 2, 3]
    for rot in rotations:
        for flip in flips:
            perm = np.matmul(rot, flip)
            perm_pos = np.matmul(pos, perm)
            print(perm_pos)

main()