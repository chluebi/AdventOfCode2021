
with open('input') as f:
    s = f.read().strip().split('\n')

close = {
    '(':')',
    '[':']',
    '{':'}',
    '<':'>'
}

cor_points = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
}

c_points = {
    ')':1,
    ']':2,
    '}':3,
    '>':4
}

scores = []

for line in s:
    stack = []
    count = 0
    corrupt = False
    for c in line:
        if c in close.keys():
            stack.append(c)
        else:
            if c == close[stack[-1]]:
                stack.pop()
            else:
                corrupt = True
                break
    if corrupt:
        #print(corrupt)
        continue
    while (len(stack) > 0):
        c = stack.pop()
        count *= 5
        count += c_points[close[c]]
    scores.append(count)

print(len(scores))
print(len(scores)//2)
print(sorted(scores)[len(scores)//2])