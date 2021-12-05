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

    def get_all_points(self):
        i = self.origin[0]
        j = self.origin[1]

        i_inc = 0
        j_inc = 0

        if i > self.dest[0]:
            i_inc = -1
        elif i < self.dest[0]:
            i_inc = 1

        if j > self.dest[1]:
            j_inc = -1
        elif j < self.dest[1]:
            j_inc = 1

        points = []

        while [i, j] != self.dest:
            points.append(str(i) + "," + str(j))
            i += i_inc
            j += j_inc

        points.append(str(i) + "," + str(j))

        return points