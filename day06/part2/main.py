#file_name = 'ex.txt'
file_name = 'input.txt'

def do_cycle(fish):
    new_fish = dict()
    for f in fish:
        amount = fish[f]
        if amount == 0:
            continue
        if f == 0:
            add_to_dict(new_fish, 8, amount)
            add_to_dict(new_fish, 6, amount)
        else:
            add_to_dict(new_fish, f-1, amount)
    return new_fish

def add_to_dict(dict, fish, amount):
    if fish in dict:
        dict[fish] += amount
    else:
        dict[fish] = amount

input = [int(i.strip()) for i in open(file_name).readline().split(',')]

d = dict()

for f in input:
    add_to_dict(d, f, 1)

for i in range(256):
    d = do_cycle(d)

acc = 0

for f in d:
    acc += d[f]

print(acc)
