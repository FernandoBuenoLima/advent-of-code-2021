class CaveSystem:
    def __init__(self, edges):
        self.caves = dict()
        self.paths = 0
        for e in edges:
            if e[0] not in self.caves:
                self.caves[e[0]] = Cave(e[0])
            if e[1] not in self.caves:
                self.caves[e[1]] = Cave(e[1])
            a = self.caves[e[0]]
            b = self.caves[e[1]]
            a.adjacencies.append(b)
            b.adjacencies.append(a)


    def find_all_paths(self):
        s = self.caves["start"]
        return self.find_paths_from(s, set())

    def find_paths_from(self, v, visited):
        if v.is_end():
            self.paths += 1
            return

        visited.add(v.name)

        for a in v.adjacencies:
            if a.is_big or a.name not in visited:
                self.find_paths_from(a, visited.copy())

class Cave:
    def __init__(self, name):
        self.name = name
        self.is_big = name.isupper()
        self.adjacencies = []

    def is_start(self):
        return self.name == "start"

    def is_end(self):
        return self.name == "end"