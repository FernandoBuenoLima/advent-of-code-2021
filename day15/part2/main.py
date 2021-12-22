from astar import AStar

#file_name = "ex.txt"
file_name = "input.txt"

original_map = []

with open(file_name) as file:
    line = [int(c) for c in file.readline().strip()]
    while len(line) > 0:
        original_map.append(line)
        line = [int(c) for c in file.readline().strip()]

height = len(original_map)
width = len(original_map[0])

map = [[0 for i in range(width*5)] for j in range(height*5)]

for i1 in range(5):
    for j1 in range(5):
        for i2 in range(height):
            for j2 in range(width):
                n = original_map[i2][j2] + i1 + j1
                while n > 9:
                    n -= 9
                map[i1*height + i2][j1*width + j2]  = n

a = AStar(map)

print(a.run())