#file_name = "ex.txt"
file_name = "input.txt"

opening_chars = "([{<"
closing_chars = ")]}>"

points = { ')': 3, ']': 57, '}': 1197, '>': 25137 }

def get_corrupted_character(line):
    stack = []
    for c in line:
        if c in opening_chars:
            stack.append(c)
        elif c in closing_chars:
            if len(stack) == 0:
                return c
            current = stack.pop()
            if opening_chars.index(current) != closing_chars.index(c):
                return c
    return None

inputs = []

with open(file_name) as file:
    l = file.readline()
    while len(l) > 0:
        inputs.append(l.strip())
        l = file.readline()

d = dict()

for l in inputs:
    c = get_corrupted_character(l)
    if c is not None:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

acc = 0

for k in d:
    acc += d[k] * points[k]

print(acc)