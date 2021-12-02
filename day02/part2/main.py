file_name = 'ex.txt'
#file_name = 'input.txt'

input = [c.split() for c in open(file_name).readlines()]

for c in input:
    c[1] = int(c[1])

hor = 0
dep = 0
aim = 0

for c in input:
    if c[0] == 'forward':
        hor += c[1]
        dep += aim*c[1]
    elif c[0] == 'down':
        aim += c[1]
    elif c[0] == 'up':
        aim -= c[1]
    else:
        print("unrecognized command:", c[0])

print(hor*dep)