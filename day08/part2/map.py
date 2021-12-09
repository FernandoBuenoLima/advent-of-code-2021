
class NumMap:
    def __init__(self, numbers, output):
        self.d = dict()
        self.numbers = numbers
        self.output = output
        self.digits_mapping = { "abcefg": '0', "cf": '1', "acdeg": '2', "acdfg": '3', "bcdf": '4', "abdfg": '5', "abdefg": '6', "acf": '7', "abcdefg": '8', "abcdfg": '9' }

    def set_mapping(self, k, v):
        self.d[k] = v

    def get_numbers_with_length(self, l):
        arr = []
        for n in self.numbers:
            if len(n) == l:
                arr.append(n)
        return arr

    def get_keys_from_value(self, v):
        arr = []
        for k in self.d:
            if v in self.d[k]:
                arr.append(k)
        return arr

    def get_mising_key(self):
        for c in "abcdefg":
            if c not in self.d:
                return c

    def decode_output(self):
        arr = []
        for o in self.output:
            o_a = [self.d[c] for c in o]
            o_a.sort()
            s = ""
            for c in o_a:
                s += c
            arr.append(self.digits_mapping[s])
        return arr