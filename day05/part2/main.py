from line import Line

#file_name = "ex.txt"
file_name = "input.txt"

input =[l.strip().split(" -> ") for l in open(file_name).readlines()]

lines = []

for inp in input:
    lines.append(Line([inp[0].split(','), inp[1].split(',')]))

d = dict()

for l in lines:
    for p in l.get_all_points():
        if p in d:
            d[p] += 1
        else:
            d[p] = 1

acc = 0

for k in d:
    if d[k] > 1:
        acc += 1

print(acc)