from lib import *

#file_name = "ex1.txt"
#file_name = "ex2.txt"
file_name = "input.txt"




arr_out = []

with open(file_name) as file:
    values = file.readline().split("|")
    while len(values) > 1:
        outs = [n.split() for n in values]
        arr_out.append(outs)
        values = file.readline().split("|")

acc = 0
for o in arr_out:
    s = ""
    for c in get_letter_links(o[0], o[1]):
        s += c
    acc += int(s)

print(acc)