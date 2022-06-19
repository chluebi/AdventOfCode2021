from collections import Counter


with open('input') as f:
    s = f.read().strip().split(',')

ages = []
for age in s:
    ages.append(int(age))

c = Counter(ages)
age_range = [c[i] for i in range(9)]

for t in range(256):
    print(t)
    new_age_range = [0 for i in range(9)]
    for i, n in enumerate(age_range):
        if i == 0:
            new_age_range[6] += n
            new_age_range[8] += n
        else:
            new_age_range[i-1] += n
    age_range = new_age_range
print(new_age_range)
print(sum(new_age_range))