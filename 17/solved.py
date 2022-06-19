with open('input') as f:
    s = f.read().strip().split('\n')

target_x = (85, 145)
target_y = (-163, -108)

def simulation(vx, vy):
    c_vx = vx
    c_vy = vy
    x = 0
    y = 0
    max_y = -10000000000
    for i in range(2000):
        x += c_vx
        y += c_vy
        if c_vx > 0:
            c_vx -= 1
        elif c_vx < 0:
            c_vx += 1
        c_vy -= 1
        max_y = max(max_y, y)
        #print(x, y)
        if (x > target_x[1]):
            return None
        if (x >= target_x[0]) and (y >= target_y[0]) and (x <= target_x[1]) and (y <= target_y[1]):
            return max_y
    return None


count = 0
total_max_y = -1000000000000
for vy in range(-164, 169):
    print(vy)
    for vx in range(-10, 600):
        result = simulation(vx, vy)
        if result is not None:
            print(vx, vy)
            count += 1
            total_max_y = max(total_max_y, result)
print('total max', total_max_y)
print('count', count)
