file_name = 'ex.txt'
#file_name = 'input.txt'

fish = [int(i.strip()) for i in open(file_name).readline().split(',')]

def do_cycle(fish):
    new_fish = []
    for i in range(len(fish)):
        f = fish[i]
        if f == 0:
            new_fish.append(8)
            fish[i] = 6
        else:
            fish[i] -= 1

    fish.extend(new_fish)


for i in range(256):
    do_cycle(fish)

print(len(fish))
