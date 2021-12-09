#file_name = "ex.txt"
file_name = "input.txt"



with open(file_name) as file:
    map = []
    line = [int(c) for c in file.readline().strip()]
    while len(line) > 0:
        map.append(line)
        line = [int(c) for c in file.readline().strip()]

height = len(map)
width = len(map[0])

acc = 0

for i in range(height):
    for j in range(width):
        v = map[i][j]
        if i > 0:
            if map[i-1][j] <= v:
                continue
        if i < height-1:
            if map[i+1][j] <= v:
                continue
        if j > 0:
            if map[i][j-1] <= v:
                continue
        if j < width-1:
            if map[i][j+1] <= v:
                continue
        acc += (v+1)

print(acc)
