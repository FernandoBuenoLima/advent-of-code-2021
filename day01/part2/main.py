#file_name = "ex.txt"
file_name = "input.txt"

with open(file_name) as file:
    input = [int(n) for n in file.readlines()]


acc = 0
i = 0

while (len(input) - i) >= 4:
    a = sum(input[i:i+3])
    b = sum(input[i+1:i+4])
    if a < b:
        acc += 1
    i += 1

print(acc)
