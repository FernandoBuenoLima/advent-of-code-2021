from snailtree import *

#file_name = "ex.txt"
file_name = "input.txt"

inputs = []
with open(file_name) as file:
    line = file.readline().strip()
    while len(line) > 0:
        inputs.append(line)
        line = file.readline().strip()

nodes = []
for l in inputs:
    nodes.append(create_node_from_string(l))

s = nodes[0]

for i in range(1, len(nodes)):
    s = s.sum(nodes[i])

print(s.magnitude())
