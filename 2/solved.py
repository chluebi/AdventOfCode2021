with open('in') as f:
    s = f.read().strip().split('\n')

depth = 0
horizontal = 0
aim = 0
for command in s:
    command, number = command.split(' ')
    number = int(number)
    if (command == 'forward'):
        horizontal += number
        depth += aim*number
    elif (command == 'down'):
        aim += number
    elif (command == 'up'):
        aim -= number

print(depth*horizontal)