with open('.in') as f:
    s = f.read().split('\n')

count = 0
for i, _ in enumerate(s):
    if i < 3:
        continue
    if int(s[i]) > int(s[i-3]):
        count+=1
print(count)