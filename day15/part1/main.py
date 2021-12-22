from astar import AStar

#file_name = "ex.txt"
file_name = "input.txt"

map = []

with open(file_name) as file:
    line = [int(c) for c in file.readline().strip()]
    while len(line) > 0:
        map.append(line)
        line = [int(c) for c in file.readline().strip()]

a = AStar(map)

print(a.run())