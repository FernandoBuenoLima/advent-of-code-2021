EMPTY = ' '
DOT = '#'

class Transparency:
    def __init__(self, dots):
        width = 1
        height = 1

        for dot in dots:
            if dot[0] > width:
                width = dot[0]
            if dot[1] > height:
                height = dot[1]

        self.width = width+1
        self.height = height+1

        self.arr = [[EMPTY for i in range(self.width)] for j in range(self.height)]

        for dot in dots:
            self.add_dot(dot)

    def add_dot(self, dot):
        self.arr[dot[1]][dot[0]] = DOT

    def print(self):
        for l in self.arr:
            s = ""
            for c in l:
                s += c
            print(s)

    def fold_at_x(self, x):
        new_arr = []

        for j in range(self.height):
            line = []
            for i in range(x):
                if self.arr[j][i] == DOT or self.arr[j][self.width-i-1] == DOT:
                    line.append(DOT)
                else:
                    line.append(EMPTY)
            new_arr.append(line)
        self.arr = new_arr
        self.width = len(self.arr[0])
        self.height = len(self.arr)

    def fold_at_y(self, y):
        a1 = self.arr[:y]
        a2 = self.arr[y+1:]

        for i in range(len(a1)):
            for j in range(len(a1[0])):
                if a2[-(i+1)][j] == DOT:
                    a1[i][j] = DOT
        self.arr = a1
        self.width = len(self.arr[0])
        self.height = len(self.arr)

    def count_dots(self):
        acc = 0
        for line in self.arr:
            for c in line:
                if c == DOT:
                    acc += 1
        return acc