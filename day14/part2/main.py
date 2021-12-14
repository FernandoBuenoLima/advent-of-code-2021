#file_name = "ex.txt"
file_name = "input.txt"

def cycle(p, rules, count):
    new_p = dict()
    for k in p:
        a = k[0]
        b = k[1]
        m = rules[k]
        e1 = a + m
        e2 = m + b

        if m in count:
            count[m] += p[k]
        else:
            count[m] = p[k]


        if e1 in new_p:
            new_p[e1] += p[k]
        else:
            new_p[e1] = p[k]

        if e2 in new_p:
            new_p[e2] += p[k]
        else:
            new_p[e2] = p[k]

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
count_dict = dict()

with open(file_name) as file:
    pol = file.readline().strip()
    pol_dict = dict()

    for c in pol:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1

    for i in range(len(pol)-1):
        e = pol[i:i+2]
        if e in pol_dict:
            pol_dict[e] += 1
        else:
            pol_dict[e] = 1
    file.readline()

    r = file.readline().strip().split(" -> ")
    while len(r) > 1:
        rules[r[0]] = r[1]
        r = file.readline().strip().split(" -> ")

for i in range(40):
    pol_dict = cycle(pol_dict, rules, count_dict)

for k in count_dict:
    ex = count_dict[k]
    break

low_c = high_c = ex

for k in count_dict:
    if count_dict[k] < low_c:
        low_c = count_dict[k]
    if count_dict[k] > high_c:
        high_c = count_dict[k]

print(high_c - low_c)