
with open('input') as f:
    s = f.read().strip().split(',')

positions = [int(i) for i in s]
best_diff = 1000000000000
best_pos = 0
for i in range(max(positions)):
    diff = 0
    for pos in positions:
        diff += abs(i-pos)*(abs(i-pos)+1)/2
    if diff < best_diff:
        best_diff = diff
        best_pos = i

print(best_pos, best_diff)