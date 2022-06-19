import copy
import numpy as np

energy_dict = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

def correct_ordering(rooms):
    correct_order = True
    keys = list(energy_dict.keys())
    for i in range(1, 5):
        room = rooms[i]
        correct_order = correct_order and room[0] == keys[i-1]
        correct_order = correct_order and room[1] == keys[i-1]
    return correct_order

def correct_ordering2(rooms):
    correct_order = True
    keys = list(energy_dict.keys())
    for i in range(1, 3):
        room = rooms[i]
        correct_order = correct_order and room[0] == keys[i-1]
        correct_order = correct_order and room[1] == keys[i-1]
    return correct_order

best_configs = {}


def move(rooms_tuple, energy, recursion):
    if rooms_tuple in best_configs:
        if best_configs[rooms_tuple] <= energy:
            return
        else:
            best_configs[rooms_tuple] = energy
    else:
        best_configs[rooms_tuple] = energy

    rooms = list(list(r) for r in rooms_tuple)

    if recursion < 9:
        print(recursion, energy, rooms, len(best_configs))

    if energy > 1000000:
        return None
    if recursion > 18:
        return None

    if correct_ordering(rooms):
        return energy

    best_energy = []
    for i in range(1, 5):
        room = rooms[i]
        for j in range(0, 5):
            if rooms[0][j] is None:
                path = True
                if j == i:
                    path = True
                elif j < i:
                    for k in range(i-1, j, np.sign(j-i)):
                        path = path and rooms[0][k] is None
                else:
                    for k in range(i, j, np.sign(j-i)):
                        path = path and rooms[0][k] is None
                
                if path:
                    if room[0] is not None:
                        new_rooms = copy.deepcopy(rooms)
                        new_energy = 1 + abs(j*2 - i*2+1)
                        new_energy = new_energy * energy_dict[new_rooms[i][0]]
                        new_rooms[0][j] = new_rooms[i][0]
                        new_rooms[i][0] = None

                        new_rooms_tuple = tuple(tuple(r) for r in new_rooms)
                        best_energy.append(move(new_rooms_tuple, energy+new_energy, recursion+1))

                    elif room[1] is not None:
                        new_rooms = copy.deepcopy(rooms)
                        new_energy = 2 + abs(j*2 - i*2+1)
                        new_energy = new_energy * energy_dict[new_rooms[i][1]]
                        new_rooms[0][j] = new_rooms[i][1]
                        new_rooms[i][1] = None

                        new_rooms_tuple = tuple(tuple(r) for r in new_rooms)
                        best_energy.append(move(new_rooms_tuple, energy+new_energy, recursion+1))
            
            else:
                path = True
                if j == i:
                    path = True
                elif j < i:
                    for k in range(i-1, j, np.sign(j-i)):
                        path = path and rooms[0][k] is None
                else:
                    for k in range(i, j, np.sign(j-i)):
                        path = path and rooms[0][k] is None

                if path:
                    if room[1] is None:

                        new_rooms = copy.deepcopy(rooms)
                        new_energy = 2 + abs(j*2 - i*2+1)
                        new_energy = new_energy * energy_dict[new_rooms[0][j]]
                        new_rooms[i][1] = new_rooms[0][j]
                        new_rooms[0][j] = None

                        new_rooms_tuple = tuple(tuple(r) for r in new_rooms)
                        best_energy.append(move(new_rooms_tuple, energy+new_energy, recursion+1))

                    elif room[0] is None:
                        
                        new_rooms = copy.deepcopy(rooms)
                        new_energy = 1 + abs(j*2 - i*2+1)
                        new_energy = new_energy * energy_dict[new_rooms[0][j]]
                        new_rooms[i][0] = new_rooms[0][j]
                        new_rooms[0][j] = None

                        new_rooms_tuple = tuple(tuple(r) for r in new_rooms)
                        best_energy.append(move(new_rooms_tuple, energy+new_energy, recursion+1))
    
    min_energy = 10000000000
    for e in best_energy:
        if e is not None:
            min_energy = min(min_energy, e)

    return min_energy


def main():
    with open('input') as f:
        s = f.read().strip().split('\n')

    def p(k):
        if k == '.':
            return None
        else:
            return k

    rooms = [
        [s[1][2], s[1][4], s[1][6], s[1][8], s[1][10]],
        [s[2][3], s[3][3]],
        [s[2][5], s[3][5]],
        [s[2][7], s[3][7]],
        [s[2][9], s[3][9]]
    ]

    for i in range(len(rooms)):
        for j in range(len(rooms[i])):
            rooms[i][j] = p(rooms[i][j])

    print(rooms)
    rooms_tuple = tuple(tuple(r) for r in rooms)
    best = move(rooms_tuple, 0, 0)
    print('best', best)



main()