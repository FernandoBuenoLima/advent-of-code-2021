from board import Board

#file_name = "ex.txt"
file_name = "input.txt"

def read_board(file):
    file.readline()

    b = []

    for i in range(5):
        arr = file.readline().split()
        b.append([int(n.strip()) for n in arr])

    return b

boards = []

with open(file_name) as file:
    numbers = [int(n.strip()) for n in file.readline().split(',')]

    while True:
        b_num = read_board(file)
        if len(b_num[0]) == 0:
            break
        boards.append(Board(b_num))

for n in numbers:
    for b in boards:
        if b.mark_number(n):
            if b.did_win():
                print(b.sum_all_unmarked()*n)
                exit()
