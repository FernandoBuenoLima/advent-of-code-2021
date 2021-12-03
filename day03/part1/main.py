#file_name = "ex.txt"
file_name = "input.txt"

input = [n.strip() for n in open(file_name).readlines()]

zero_counter_arr = [0 ] * len(input[0])
one_counter_arr = [0 ] * len(input[0])

for n in input:
    for i in range(len(n)):
        d = n[i]
        if d == '0':
            zero_counter_arr[i] += 1
        else:
            one_counter_arr[i] += 1

gamma = ''
epsilon = ''

for i in range(len(zero_counter_arr)):
    if zero_counter_arr[i] > one_counter_arr[i]:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma * epsilon)


