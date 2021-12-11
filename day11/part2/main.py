#file_name = "ex.txt"
file_name = "input.txt"

def flash(m, height, width, i, j):
    m[i][j] = -1
    for i2 in range(i-1, i+2):
        for j2 in range(j-1, j+2):
            if i2 >= 0 and i2 < height and j2 >= 0 and j2 < width:
                if m[i2][j2] == -1:
                    continue
                m[i2][j2] += 1
                if m[i2][j2] > 9:
                    flash(m, height, width, i2, j2)

def step(m, height, width):
    acc = 0
    for i in range(height):
        for j in range(width):
            m[i][j] += 1
    for i in range(height):
        for j in range(width):
            if m[i][j] > 9:
                flash(m, height, width, i, j)
    for i in range(height):
        for j in range(width):
            if m[i][j] == -1:
                acc += 1
                m[i][j] = 0
    return acc

input = []
with open(file_name) as file:
    l = [int(n.strip()) for n in file.readline().strip()]
    while len(l) > 0:
        input.append(l)
        l = [int(n.strip()) for n in file.readline().strip()]

height = len(input)
width = len(input[0])

target = height * width
i = 1
while True:
    flashes = step(input, height, width)
    if flashes == target:
        break
    i += 1

print(i)