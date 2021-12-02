# Parse data file
data_path = 'input/d02_dive.txt'
commands = []
with open(data_path, 'r') as file:
    for line in file.readlines():
        direction, units = line.strip().split(' ')
        units = int(units)
        commands.append((direction, units))

# Part One
horizontal = 0
depth = 0
for direction, units in commands:
    if direction == 'forward':
        horizontal += units
    if direction == 'down':
        depth += units
    if direction == 'up':
        depth -= units
print('Part One', horizontal, depth, horizontal * depth)
