def get_numbers_with_length(numbers, l):
    arr =[]
    for n in numbers:
        if len(n) == l:
            arr.append(n)
    return arr

def get_letter_links(numbers):
    d = dict()

    #number 1
    c_or_f = get_numbers_with_length(numbers, 2)[0]
    d[c_or_f[0]] = "cf"
    d[c_or_f[1]] = "cf"

    #number 7
    n_seven = get_numbers_with_length(numbers, 3)[0]
    for l in n_seven:
        if l not in c_or_f:
            d[l] = 'a'
            break

    #number 4
    b_or_d = get_numbers_with_length(numbers, 4)[0]
    for l in b_or_d:
        if l not in c_or_f:
            d[l] = "bd"

    #numbers 0, 6 and 9
    n_len_6 = get_numbers_with_length(numbers, 6)

    n_9 = ""
    for num in n_len_6:
        found = 0
        for c in num:
            if c in d:
                if d[c] in "bdcf":
                    found += 1
        if found == 4:
            n_9 = num
            break

    for l in "abcdefg":
        if l not in n_9:
            d[l] = 'e'
            break

    n_6 = ""


