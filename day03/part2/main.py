#file_name = "ex.txt"
file_name = "input.txt"

def count_digits(s):
    e = next(iter(s))
    zero_arr = [0 ] * len(e)
    one_arr = [0 ] * len(e)
    for n in s:
        for i in range(len(n)):
            d = n[i]
            if d == '0':
                zero_arr[i] += 1
            else:
                one_arr[i] += 1
    return zero_arr, one_arr




input = [n.strip() for n in open(file_name).readlines()]

oxygen = {n for n in input}
i = 0

while len(oxygen) > 1:
    zero_counter_arr, one_counter_arr = count_digits(oxygen)
    new_oxygen = set()
    for n in oxygen:
        if one_counter_arr[i] >= zero_counter_arr[i]:
            if n[i] == '1':
                new_oxygen.add(n)
        else:
            if n[i] == '0':
                new_oxygen.add(n)
    oxygen = new_oxygen.copy()
    i += 1


co2 = {n for n in input}
i = 0

while len(co2) > 1:
    zero_counter_arr, one_counter_arr = count_digits(co2)
    new_co2 = set()
    for n in co2:
        if one_counter_arr[i] >= zero_counter_arr[i]:
            if n[i] == '0':
                new_co2.add(n)
        else:
            if n[i] == '1':
                new_co2.add(n)
    co2 = new_co2.copy()
    i += 1




oxygen = int(oxygen.pop(), 2)
co2 = int(co2.pop(), 2)

print(oxygen * co2)


