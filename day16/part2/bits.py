#Type Id
SUM = 0
PRODUCT = 1
MINIMUM = 2
MAXIMUM = 3
LITERAL_NUMBER = 4
GREATER_THAN = 5
LESS_THAN = 6
EQUAL_TO = 7

#Size Type Id
FIFTEEN_BITS_FOR_BITS = '0'
ELEVEN_BITS_FOR_PACKETS = '1'

class BitsReader:
    def __init__(self, hex_input, pointer = 0, bits_limit = -1, s = ""):
        self.hex = hex_input
        self.hex_pointer = pointer

        self.s = s
        self.bits_read = 0
        self.bits_limit = bits_limit

    def peek_current_hex(self):
        h = self.hex[self.hex_pointer]
        s = bin(int(h, 16))[2:]
        while len(s) < 4:
            s = '0' + s
        return s

    def read_current_hex(self):
        self.s += self.peek_current_hex()
        self.hex_pointer += 1

    def read_bits(self, n):
        while len(self.s) < n:
            self.read_current_hex()

        s = self.s[:n]
        if len(self.s) > n:
            self.s = self.s[n:]
        else:
            self.s = ""

        self.bits_read += n
        return s

    def read_packet_header(self):
        version = self.read_bits(3)
        type_id = self.read_bits(3)

        return version, type_id

    def read_packet_number(self):
        total = ""
        while True:
            n = self.read_bits(5)
            total += n[1:]
            if n[0] == '0':
                break
        return total

    def read_packet(self):
        version, type_id = self.read_packet_header()
        version = int(version, 2)
        type_id = int(type_id, 2)
        print("version:", version)
        print("type id:", type_id)
        arr = []
        if type_id == LITERAL_NUMBER:
            arr.append(int(self.read_packet_number(), 2))
            print("number:", arr[0])
        else:
            print("operator")
            print("s:", self.s)
            length_type_id = self.read_bits(1)
            print("lengh type id:", length_type_id)
            if length_type_id == FIFTEEN_BITS_FOR_BITS:
                length = int(self.read_bits(15), 2)
                print("length:", length)
                sub_reader = BitsReader(self.hex, self.hex_pointer, length, self.s)
                arr.extend(sub_reader.read())
                self.hex_pointer = sub_reader.hex_pointer
                self.s = sub_reader.s
                self.bits_read += sub_reader.bits_read
            else:#ELEVEN_BITS_FOR_PACKETS
                packets = int(self.read_bits(11), 2)
                print("packets:", packets)
                for i in range(packets):
                    arr.append(self.read_packet())

        total = None

        print("type_id", type_id)
        print("arr", arr)

        if type_id == SUM:
            total = sum(arr)
        elif type_id == PRODUCT:
            total = 1
            for n in arr:
                total *= n
        elif type_id == MINIMUM:
            total = min(arr)
        elif type_id == MAXIMUM:
            total = max(arr)
        elif type_id == LITERAL_NUMBER:
            total = arr[0]
        elif type_id == GREATER_THAN:
            total = 1 if arr[0] > arr[1] else 0
        elif type_id == LESS_THAN:
            total = 1 if arr[0] < arr[1] else 0
        elif type_id == EQUAL_TO:
            total = 1 if arr[0] == arr[1] else 0

        return total


    def read(self):
        arr = []
        if self.bits_limit > 0:
            while self.bits_read < self.bits_limit:
                if len(self.s) > 0 and int(self.s, 2) == 0 and int(self.hex[self.hex_pointer:], 16) == 0:
                    break
                arr.append(self.read_packet())
        else:
            while self.hex_pointer < len(self.hex):
                if len(self.s) > 0 and int(self.s, 2) == 0 or len(self.s) == 0 and int(self.hex[self.hex_pointer:], 16) == 0:
                    break
                arr.append(self.read_packet())
        return arr