import copy
import math

def str_to_list(s, ind):
    if s[ind] == '[':
        ind += 1
        left, ind = str_to_list(s, ind)
        if s[ind] != ',':
            raise Exception('no comma')
        ind += 1
        right, ind = str_to_list(s, ind)
        if s[ind] != ']':
            raise Exception('no closing')
        ind += 1
        return [left, right], ind
    else:
        num_string = ''
        while True:
            try:
                num_string += str(int(s[ind]))
            except ValueError:
                break
            ind += 1
        return int(num_string), ind

def get_number(x, path):
    if path == '':
        return x
    if path[0] == 'l':
        return get_number(x[0], path[1:])
    else:
        return get_number(x[1], path[1:])

def change_number(x, path, value):
    if path == 'l':
        x[0] = value
        return
    if path == 'r':
        x[1] = value
        return

    if path[0] == 'l':
        return change_number(x[0], path[1:], value)
    else:
        return change_number(x[1], path[1:], value)

def get_side(path, side):
    if len(path) == 0:
        return None
    if side == 'l':
        if path[-1] == 'r':
            return path[:-1] + 'l'
        else:
            return get_side(path[:-1], side)
    else:
        if path[-1] == 'l':
            return path[:-1] + 'r'
        else:
            return get_side(path[:-1], side)

def get_side_most(x, side, path):
    if type(x) is not list:
        return path
    if side == 'l':
        s = x[0]
    else:
        s = x[1]
    if type(s) is list:
        path = get_side_most(s, side, path + side)
        return path
    else:
        return path + side
    

def explode_pos(full_x, x, r, path):
    if type(x) is list:
        if r == 4:
            exploded = True
            return exploded, path
        else:
            r += 1
            exploded, explode_path = explode_pos(full_x, x[0], r, path + 'l')
            if exploded:
                return exploded, explode_path
            exploded, explode_path = explode_pos(full_x, x[1], r, path + 'r')
            if exploded:
                return exploded, explode_path
            return False, None
    else:
        return False, None

def explode(full_x):
    exploded, path = explode_pos(full_x, full_x, 0, '')
    if not exploded:
        return False
    x = get_number(full_x, path)
    left = get_side(path, 'l')
    if left is not None:
        left_side = get_number(full_x, left)
        left += get_side_most(left_side, 'r', '')
        change_number(full_x, left, get_number(full_x, left) + x[0])

    right = get_side(path, 'r')
    if right is not None:
        right_side = get_number(full_x, right)
        right += get_side_most(right_side, 'l', '')
        change_number(full_x, right, get_number(full_x, right)+x[1])

    change_number(full_x, path, 0)
    return True

def get_split_path(full_x, x, r, path):
    if type(x) is list:
        r += 1
        sp, split_path = get_split_path(full_x, x[0], r, path + 'l')
        if sp:
            return sp, split_path
        sp, split_path = get_split_path(full_x, x[1], r, path + 'r')
        if sp:
            return sp, split_path
        return False, None
    else:
        if x >= 10:
            return True, path
        return False, None

def split(full_x):
    sp, split_path = get_split_path(full_x, full_x, 0, '')
    if sp is False:
        return False
    num = get_number(full_x, split_path)
    left = math.floor(num / 2)
    right = math.ceil(num / 2)
    change_number(full_x, split_path, [left, right])
    return True

def add(x, y):
    z = [x, y]
    
    reduce(z)

    return z

def reduce(z):
    while True:
        repeat = True
        while repeat:
            repeat = explode(z)

        sp = split(z)
        if not sp:
            break

def magnitude(x):
    if type(x[0]) is list:
        left = magnitude(x[0])
    else:
        left = x[0]

    if type(x[1]) is list:
        right = magnitude(x[1])
    else:
        right = x[1]

    return left*3 + right*2

def main():
    with open('input') as f:
        s = f.read().strip().split('\n')

    m = -100000
    for line1 in s:
        for line2 in s:
            
            x, _ = str_to_list(line1, 0)
            y, _ = str_to_list(line2, 0)
            res = add(x, y)
            m = max(m, magnitude(res))

    print(m)

l = [[[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]],[1,[[[9,3],9],[[9,0],[0,7]]]]]
print(l)
print(reduce(l))
print(l)