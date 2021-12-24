from snailtree import *

#file_name = "ex.txt"
file_name = "input.txt"

inputs = []
with open(file_name) as file:
    line = file.readline().strip()
    while len(line) > 0:
        inputs.append(line)
        line = file.readline().strip()

max = 0

for i in range(len(inputs)):
    for j in range(len(inputs)):
        if i == j:
            continue

        a = create_node_from_string(inputs[i])
        b = create_node_from_string(inputs[j])

        c = a.sum(b)
        m = c.magnitude()
        if m > max:
            max = m

print(max)