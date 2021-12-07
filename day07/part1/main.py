#file_name = "ex.txt"
file_name = "input.txt"

input = [int(n.strip()) for n in open(file_name).readline().split(',')]

def calculate_fuel(crabs, target):
    acc = 0
    for c in crabs:
        diff = c - target
        if diff < 0:
            diff *= -1
        acc += diff
    return acc

ma = max(input)
mi = min(input)

result = calculate_fuel(input, mi)

for i in range(mi+1, ma+1):
    f = calculate_fuel(input, i)
    if f < result:
        result = f

print(result)
