from bits import BitsReader

#file_name = "ex.txt"
file_name = "input.txt"

input = ""
with open(file_name) as file:
    input = file.readline().strip()

reader = BitsReader(input)
version_total = reader.read()
print("bits read:", reader.bits_read)
print("ignored bits:", reader.s)

print("\n\nversion total:", version_total)