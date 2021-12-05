class Line:
    def __init__(self, input):
        self.origin = [int(i) for i in input[0]]
        self.dest = [int(i) for i in input[1]]

        if self.origin[0] == self.dest[0]:
            self.orientation = 'h'
        elif self.origin[1] == self.dest[1]:
            self.orientation = 'v'
        else:
            self.orientation = 'd'

    def is_hor_or_ver(self):
        return self.origin[0] == self.dest[0] or self.origin[1] == self.dest[1]

    def __str__(self):
        return str(self.origin[0]) + "," + str(self.origin[1]) + " -> " + str(self.dest[0]) + "," + str(self.dest[1])

    def is_point_in_line(self, point):
        if self.orientation == 'h':
            if point[0] != self.origin[0]:
                return False
            ma = max(self.origin[1], self.dest[1])
            mi = min(self.origin[1], self.dest[1])
            return mi <= point[1] <= ma
        if self.orientation == 'v':
            if point[1] != self.origin[1]:
                return False
            ma = max(self.origin[0], self.dest[0])
            mi = min(self.origin[0], self.dest[0])
            return mi <= point[0] <= ma
        return "maluquice"