from transparency import Transparency

#file_name = "ex.txt"
file_name = "input.txt"

dots = []
folds = []
with open(file_name) as file:
    l = file.readline().strip().split(',')
    while len(l) > 1:
        dots.append([int(n) for n in l])
        l = file.readline().strip().split(',')

    l = file.readline().strip().replace("fold along ", '').split('=')
    while len(l) > 1:
        folds.append([l[0], int(l[1])])
        l = file.readline().strip().replace("fold along ", '').split('=')

t = Transparency(dots)

f = folds[0]

if f[0] == 'x':
    t.fold_at_x(f[1])
else:
    t.fold_at_y(f[1])

print(t.count_dots())
