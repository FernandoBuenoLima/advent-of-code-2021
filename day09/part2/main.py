#file_name = "ex.txt"
file_name = "input.txt"

def find_basin_size(map, height, width, i, j, visited):
    acc = 1
    v = map[i][j]
    if i > 0:
        c = (i-1, j)
        v2 = map[i-1][j]
        if c not in visited and v2 > v and v2 < 9:
            visited.append(c)
            acc += find_basin_size(map, height, width, i-1, j, visited)
    if j > 0:
        c = (i, j-1)
        v2 = map[i][j-1]
        if c not in visited and v2 > v and v2 < 9:
            visited.append(c)
            acc += find_basin_size(map, height, width, i, j-1, visited)
    if i < (height-1):
        c = (i+1, j)
        v2 = map[i+1][j]
        if c not in visited and v2 > v and v2 < 9:
            visited.append(c)
            acc += find_basin_size(map, height, width, i+1, j, visited)
    if j < (width-1):
        c = (i, j+1)
        v2 = map[i][j+1]
        if c not in visited and v2 > v and v2 < 9:
            visited.append(c)
            acc += find_basin_size(map, height, width, i, j+1, visited)
    return acc

with open(file_name) as file:
    map = []
    line = [int(c) for c in file.readline().strip()]
    while len(line) > 0:
        map.append(line)
        line = [int(c) for c in file.readline().strip()]

height = len(map)
width = len(map[0])

arr = []

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
        arr.append(find_basin_size(map, height, width, i, j, []))

arr.sort(reverse=True)

print(arr[0]*arr[1]*arr[2])
