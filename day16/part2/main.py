from bits import BitsReader

#file_name = "ex.txt"
file_name = "input.txt"

input = ""
with open(file_name) as file:
    input = file.readline().strip()

reader = BitsReader(input)
result = reader.read()
print("\n\nbits read:", reader.bits_read)
print("ignored bits:", reader.s)

print("\nresult:", result[0])