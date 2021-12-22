from lib import *

#file_name = "ex.txt"
file_name = "input.txt"

input = ""

with open(file_name) as file:
    input = file.readline().replace("target area: ", '').strip()

x, y = input.split(", ")

x = [int(n) for n in x.split('=')[1].split("..")]
y = [int(n) for n in y.split('=')[1].split("..")]

vx, vy = try_find_legal_v0(x, y)

total = 0
while vy > 0:
    total += vy
    vy -= 1

print(total)