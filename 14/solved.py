from collections import Counter

with open('input') as f:
    s = f.read().split('\n\n')

polymer, steps = s

rules = []
for step in steps.split('\n'):
    i, o = step.split(' -> ')
    rules.append((i, o))

for count in range(40):
    insertions = []
    for rule in rules:
        i, o = rule
        if i in polymer:
            for ind in range(len(polymer)):
                if polymer.startswith(i, ind):
                    insertions.append((ind+1, o))
    
    more_index = 0
    for ind, letter in sorted(insertions, key=lambda x: x[0]):
        full_ind = ind + more_index
        polymer = polymer[:full_ind] + letter + polymer[full_ind:]
        more_index += 1
    
    #print(polymer)
    print(count)
    print(len(polymer))

counter = Counter(polymer)
print(len(polymer))
print(counter.most_common())
print(counter.most_common()[0][1] - counter.most_common()[-1][1])