import copy

with open('input') as f:
    s = f.read().strip().split('\n')

l = len('111011001010')
print(l)

count = [[0,0] for i in range(l)]

possible1 = copy.copy(s)
value1 = None

for bit in range(l):
    for line in possible1:
        char = int(line[bit])
        count[bit][char] += 1
            
    zeroes = count[bit][0]
    ones = count[bit][1]

    if (zeroes > ones):
        bit_value = 0
    else:
        bit_value = 1

    for line in s:
        char = int(line[bit])
        if char != bit_value:
            if len(possible1) > 1:
                try:
                    possible1.remove(line)
                except:
                    pass
    if len(possible1) == 1:
        value1 = possible1[0]
        break

count = [[0,0] for i in range(l)]
possible2 = copy.copy(s)
value2 = None

for bit in range(l):
    for line in possible2:
        char = int(line[bit])
        count[bit][char] += 1
            
    zeroes = count[bit][0]
    ones = count[bit][1]

    if (zeroes > ones):
        bit_value = 0
    else:
        bit_value = 1

    for line in s:
        char = int(line[bit])
        if char == bit_value:
            if len(possible2) > 1:
                try:
                    possible2.remove(line)
                except:
                    pass
    if len(possible2) == 1:
        value2 = possible2[0]
        break

values_bit = [value1, value2]
values_dec = [0, 0]
print(values_bit)

for i, v in enumerate(values_bit):
    for j, bit in enumerate(v):
        bit = int(bit)
        if (bit == 1):
            values_dec[i] += 2**(l-j-i)

print(values_dec[0]*values_dec[1])