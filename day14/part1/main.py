#file_name = "ex.txt"
file_name = "input.txt"

def cycle(p, rules):
    new_p = p[0]
    for i in range(len(p)-1):
        e = p[i:i+2]
        new_p += rules[e]
        new_p += p[i+1]
    return new_p

def build_count_dict(p):
    d = dict()
    for c in p:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

rules = dict()

with open(file_name) as file:
    pol = file.readline().strip()
    file.readline()

    r = file.readline().strip().split(" -> ")
    while len(r) > 1:
        rules[r[0]] = r[1]
        r = file.readline().strip().split(" -> ")

for i in range(10):
    pol = cycle(pol, rules)

count_d = build_count_dict(pol)

low_c = high_c = count_d[pol[0]]

for k in count_d:
    if count_d[k] < low_c:
        low_c = count_d[k]
    if count_d[k] > high_c:
        high_c = count_d[k]

print(high_c - low_c)