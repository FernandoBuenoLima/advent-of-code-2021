from cave_system import CaveSystem

#file_name = "ex.txt"
file_name = "input.txt"

input = []



with open(file_name) as file:
    e = [v.strip() for v in file.readline().strip().split('-')]
    while len(e) > 1:
        input.append(e)
        e = [v.strip() for v in file.readline().strip().split('-')]

cave = CaveSystem(input)
cave.find_all_paths()

print(cave.paths)
