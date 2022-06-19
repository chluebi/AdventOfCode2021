s = None

def validate(num):
    num = str(num)
    input_num = 0
    var = {'w': 0, 'x': 0, 'y':0, 'z':0}

    for i, line in enumerate(s):
        ins = line.split()[0]
        val = line.split()[1:]

        if ins == 'inp':
            var[val[0]] = int(num[input_num])
            input_num += 1
        elif ins == 'add':
            b = None
            if val[1] in var:
                b = var[val[1]]
            else:
                b = int(val[1])

            var[val[0]] += b
        elif ins == 'mul':
            b = None
            if val[1] in var:
                b = var[val[1]]
            else:
                b = int(val[1])

            var[val[0]] *= b
        elif ins == 'div':
            b = None
            if val[1] in var:
                b = var[val[1]]
            else:
                b = int(val[1])

            var[val[0]] = int(var[val[0]]/b)
        elif ins == 'mod':
            b = None
            if val[1] in var:
                b = var[val[1]]
            else:
                b = int(val[1])

            var[val[0]] = var[val[0]] % b
        elif ins == 'eql':
            b = None
            if val[1] in var:
                b = var[val[1]]
            else:
                b = int(val[1])

            var[val[0]] = 1 if var[val[0]] == b else 0
        else:
            raise ValueError(ins)

        #print(i, var)
        if var['z'] <= 0 and i > 16:
            print(i, var)

    return var['z'] == 0

'''
z = 7 + 8 + 10 + in[0] + in[1] + in[2]
z % 26 - 2 == in[3]
z = z/26 # either 1 or 2

# you could add 4 + in[3] here but lets try not to

z % 26 - 10 == in[4] # never happens
z = z/26
z = 1 or 2 + 4 + in[4]

z += 6 + in[5]

z % 26 - 14 == in[6]
...



z is between 6 and 14
z % 26 - 5 == in[13] has to hold
'''

def alternate_validate(num):
    num = str(num)
    added_val = [7, 8, 10, 4, 4, 6, 11, 13, 1, 8, 4, 13, 4, 14]
    div = [0, 0, 0, -2, -10, 0, -14, -5, 0, 0, -14, 0, -14, -5]
    z = 0
    for i in range(14):
        if div[i] != 0:
            x = z % 26 + div[i]
            x = 1 if x == int(num[i]) else 0
            z = z/26
        else:
            x = 1
        z = z * 26 if x == 1 else z
        z += (int(num[i]) + added_val[i]) * x
    
    return z == 0

def test():
    global s
    with open('input') as f:
        s = f.read().strip().split('\n')

    for i in range(99999999999999, 11111111111111, -1):
        if '0' in str(i):
            continue
        valid = alternate_validate(i)
        if i % 999 == 0:
            print(i, valid)
        if valid:
            print(i, valid)
            break


def main():
    global s
    with open('input') as f:
        s = f.read().strip().split('\n')

    for i in range(10**15-1, 10**15-2, -1):
        if '0' in str(i):
            continue

        i = 12345678901234
        
        valid = validate(i)
        if i % 99 == 0:
            print(i, valid)
        if valid:
            break

test()