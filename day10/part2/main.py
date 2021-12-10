#file_name = "ex.txt"
file_name = "input.txt"

opening_chars = "([{<"
closing_chars = ")]}>"

points = { ')': 3, ']': 57, '}': 1197, '>': 25137 }

def get_incomplete_line_chars(line):
    stack = []
    for c in line:
        if c in opening_chars:
            stack.append(c)
        elif c in closing_chars:
            current = stack.pop()
            if opening_chars.index(current) != closing_chars.index(c):
                return None
    return stack

inputs = []

with open(file_name) as file:
    l = file.readline()
    while len(l) > 0:
        inputs.append(l.strip())
        l = file.readline()

arr = []

for l in inputs:
    chars = get_incomplete_line_chars(l)
    if chars is not None:
        arr.append(chars)

accs = []

for chars in arr:
    acc = 0
    while len(chars) > 0:
        acc *= 5
        acc += (opening_chars.index(chars.pop())+1)
    accs.append(acc)

accs.sort()

i = len(accs)//2
print(accs[i])