from line import Line

#file_name = "ex.txt"
file_name = "input.txt"

input =[l.strip().split(" -> ") for l in open(file_name).readlines()]

lines = []

for inp in input:
    lines.append(Line([inp[0].split(','), inp[1].split(',')]))

new_lines = []

for l in lines:
    if l.orientation != 'd':
        new_lines.append(l)

lines = new_lines

overlaps = 0

for i in range(1000):
    for j in range(1000):
        print(str(i), str(j))
        acc = 0
        for l in lines:
            if l.is_point_in_line([i, j]):
                acc += 1
                if acc > 1:
                    overlaps += 1
                    break

print(overlaps)