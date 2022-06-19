from collections import Counter

with open('input') as f:
    s = f.read().split('\n\n')

polymer, steps = s

rules = {}
for step in steps.split('\n'):
    i, o = step.split(' -> ')
    rules[i] = o

p_dict = {}
for i in range(len(polymer)-1):
    d = polymer[i]+polymer[i+1]
    if d in p_dict:
        p_dict[d] += 1
    else:
        p_dict[d] = 1

def dict_increase(dic, d, am):
    if d in dic:
        dic[d] += am
    else:
        dic[d] = am

for count in range(40):
    new_p_dict = {}
    for key, value in p_dict.items():
        d = key
        if d in rules:
            o = rules[d]
            d1 = key[0] + o
            d2 = o + key[1]
            dict_increase(new_p_dict, d1, value)
            dict_increase(new_p_dict, d2, value)

    p_dict = new_p_dict

    print(p_dict)

letters = {}
for key, value in p_dict.items():
    l1, l2 = key
    dict_increase(letters, l1, value)
    dict_increase(letters, l2, value)

dict_increase(letters, polymer[0], 1)
dict_increase(letters, polymer[-1], 1)

s_letters = sorted(letters.items(), key=lambda x: x[1], reverse=True)
print(s_letters)

print(int(s_letters[0][1]/2 - s_letters[-1][1]/2))