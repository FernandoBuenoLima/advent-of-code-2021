from map import NumMap

def get_letter_links(numbers, outputs):
    m = NumMap(numbers, outputs)

    #number 1
    n_one = m.get_numbers_with_length(2)[0]
    m.set_mapping(n_one[0], "cf")
    m.set_mapping(n_one[1], "cf")

    #number 7
    n_seven = m.get_numbers_with_length(3)[0]
    for l in n_seven:
        if l not in n_one:
            m.set_mapping(l, 'a')
            break

    #number 4
    n_four = m.get_numbers_with_length(4)[0]
    for l in n_four:
        if l not in n_one:
            m.set_mapping(l, "bd")

    #numbers 0, 6 and 9
    cf = m.get_keys_from_value("cf")
    bd = m.get_keys_from_value("bd")
    n_len_6 = m.get_numbers_with_length(6)


    #number nine
    cfbd = []
    cfbd.extend(cf)
    cfbd.extend(bd)
    for num in n_len_6:
        found = True
        for l in cfbd:
            if l not in num:
                found = False
                break
        if found:
            n_nine = num
            break

    for l in "abcdefg":
        if l not in n_nine:
            m.set_mapping(l, 'e')
            break

    #number six
    for num in n_len_6:
        for l in cf:
            if not l in num:
                m.set_mapping(l, 'c')

    n = m.get_keys_from_value("cf")[0]
    m.set_mapping(n, 'f')

    #number zero
    for num in n_len_6:
        for l in bd:
            if l not in num:
                m.set_mapping(l, 'd')

    n = m.get_keys_from_value("bd")[0]
    m.set_mapping(n, 'b')

    last_key = m.get_mising_key()
    m.set_mapping(last_key, 'g')

    return m.decode_output()
