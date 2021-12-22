#Type Id
LITERAL_NUMBER = 4

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
        total = version
        type_id = int(type_id, 2)
        print("version:", version)
        print("type id:", type_id)
        if type_id == LITERAL_NUMBER:
            number = self.read_packet_number()
            print("number:", int(number, 2))
        else:
            print("operator")
            print("s:", self.s)
            length_type_id = self.read_bits(1)
            print("lengh type id:", length_type_id)
            if length_type_id == FIFTEEN_BITS_FOR_BITS:
                length = int(self.read_bits(15), 2)
                print("length:", length)
                sub_reader = BitsReader(self.hex, self.hex_pointer, length, self.s)
                total += sub_reader.read()
                self.hex_pointer = sub_reader.hex_pointer
                self.s = sub_reader.s
                self.bits_read += sub_reader.bits_read
            else:#ELEVEN_BITS_FOR_PACKETS
                packets = int(self.read_bits(11), 2)
                print("packets:", packets)
                for i in range(packets):
                    total += self.read_packet()
        return total


    def read(self):
        total = 0
        if self.bits_limit > 0:
            while self.bits_read < self.bits_limit:
                if len(self.s) > 0 and int(self.s, 2) == 0 and int(self.hex[self.hex_pointer:], 16) == 0:
                    break
                total += self.read_packet()
        else:
            while self.hex_pointer < len(self.hex):
                if len(self.s) > 0 and int(self.s, 2) == 0 and int(self.hex[self.hex_pointer:], 16) == 0:
                    break
                total += self.read_packet()
        return total