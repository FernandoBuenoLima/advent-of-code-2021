#file_name = "ex.txt"
file_name = "input.txt"

with open(file_name) as file:
    input = [int(n) for n in file.readlines()]

current = input[0]
del input[0]
acc = 0

for n in input:
    if current < n:
        acc += 1
    current = n

print(acc)