import itertools

with open('input') as f:
    s = f.read().strip().split('\n')

digits = [
    ['a', 'b', 'c', 'e', 'f', 'g'],
    ['c', 'f'],
    ['a', 'c', 'd', 'e', 'g'],
    ['a', 'c', 'd', 'f', 'g'],
    ['b', 'c', 'd', 'f'],
    ['a', 'b', 'd', 'f', 'g'],
    ['a', 'b', 'd', 'e', 'f', 'g'],
    ['a','c', 'f'],
    ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    ['a', 'b', 'c', 'd', 'f', 'g']
]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

count = 0
for line in s:
    i, out = line.split('|')
    
    good_perm = []
    for perm in itertools.permutations(letters):
        good = True
        for num in i.split():
            #print('num before', num)
            letter_list = []
            for letter in num:
                new_letter = letters[perm.index(letter)]
                letter_list.append(new_letter)
            #print('num after', letter_list)

            in_digits = False
            for d in digits:
                if (len(d) != len(letter_list)):
                    continue
                is_this_digit = True
                for letter in letter_list:
                    if not letter in d:
                        is_this_digit = False
                        break
                if is_this_digit:
                    in_digits = True
                    break
            
            if not in_digits:
                good = False
                break
            
        if good:
            good_perm = perm
            break

    print(good_perm)
    digit_string = ''
    
    for num in out.split():
        print('before', num)
        num_string = ''
        for letter in num:
            num_string += letters[good_perm.index(letter)]
        print('after', num_string)

        in_digits = False
        for d in digits:
            if (len(d) != len(num_string)):
                continue
            is_this_digit = True
            for letter in num_string:
                if not letter in d:
                    is_this_digit = False
                    break
            if is_this_digit:
                digit_string += str(digits.index(d))
                in_digits = True
                break

    print(digit_string)
    count += int(digit_string)

print(count)

'''
possible  =  {
        'a':set(),
        'b':set(),
        'c':set(),
        'd':set(),
        'e':set(),
        'f':set(),
        'g':set()
    }

while True:
        for num in i.split():
            for letters in digits:
                if len(letters) == len(num):
                    for l2 in letters:
                        if possible[l2] == set():
                            for l in num:
                                possible[l2].add(l)
                        else:
                            new_possible  = set()
                            for l in num:
                                new_possible.add(l)
                            possible[l2] = new_possible.intersection(possible[l2])
        
        all_one = True
        for letter, values in possible.items():
            print(letter, values)
            if len(values) == 1:
                v = None
                for l in values:
                    v = l
                all_one = False
                for letter2, values2 in possible.items():
                    try:
                        values2.remove(l)
                    except KeyError:
                        pass
'''
