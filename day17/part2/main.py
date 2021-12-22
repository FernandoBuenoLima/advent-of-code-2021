from lib import *

#file_name = "ex.txt"
file_name = "input.txt"

input = ""

with open(file_name) as file:
    input = file.readline().replace("target area: ", '').strip()

x, y = input.split(", ")

x = [int(n) for n in x.split('=')[1].split("..")]
y = [int(n) for n in y.split('=')[1].split("..")]

max_v0y = find_max_v0y(x, y)

total = find_all_solutions(x, y, max_v0y)

print(total)