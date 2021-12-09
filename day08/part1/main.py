#file_name = "ex.txt"
file_name = "input.txt"

arr_out = []


with open(file_name) as file:
    values = file.readline().split("|")
    while len(values) > 1:
        outs = [n.strip() for n in values[1].split()]
        arr_out.append(outs)
        values = file.readline().split("|")


acc = 0


for o in arr_out:
    for n in o:
        if len(n) == 2:
            acc += 1
        if len(n) == 4:
            acc += 1
        if len(n) == 3:
            acc += 1
        if len(n) == 7:
            acc += 1

print(acc)