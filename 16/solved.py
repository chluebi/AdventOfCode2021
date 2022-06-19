with open('input') as f:
    s = f.read().strip()

to_bin = lambda hex: '{0:08b}'.format(int(hex, 16))[4:]

bin = ''
for i in s:
    bin += to_bin(i)

# bin = '0011100000000000011011110100010100101001000100100000000011010010111111100010100011101110000000001101010000001100100000100011000001100000'
print(bin)

version_sum = 0
i = 0

def parse_package():
    global i
    global version_sum
    version = bin[i:i+3]
    i += 3
    version_sum += int(version, 2)
    id = int(bin[i:i+3], 2)
    i += 3

    print(version, id)

    if (id == 4):
        num_bits = ''
        while (bin[i] == '1'):
            i += 1
            num_bits += bin[i:i+4]
            i += 4
        i += 1
        num_bits += bin[i:i+4]
        i += 4
        print('num bits', num_bits, int(num_bits, 2))
        return int(num_bits, 2)
    else:
        length_type_id = bin[i]
        i += 1
        values = []
        if (length_type_id == '0'):
            package_bits = int(bin[i:i+15], 2)
            print('package bits', package_bits)
            i += 15
            old_i = i
            while (i - old_i < package_bits):
                values.append(parse_package())
                print('compare', i - old_i, package_bits)
        else:
            num_packages = int(bin[i:i+11], 2)
            print('num packages', num_packages)
            i += 11
            for j in range(num_packages):
                values.append(parse_package())
        
        if (id == 0):
            return sum(values)
        elif (id == 1):
            prod = 1
            for v in values:
                prod *= v
            return prod
        elif (id == 2):
            return min(values)
        elif (id == 3):
            return max(values)
        elif (id == 5):
            return 1 if values[0] > values[1] else 0
        elif (id == 6): 
            return 1 if values[0] < values[1] else 0
        elif (id == 7): 
            return 1 if values[0] == values[1] else 0
        else:
            raise ValueError(id)

while (True):
    print(parse_package())

    if (i >= len(bin)):
        break

    while (bin[i] == '0'):
        i += 1
        if (i >= len(bin)):
            break

    if (i >= len(bin)):
        break
    
print(version_sum)
