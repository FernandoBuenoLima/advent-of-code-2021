from math import floor, ceil

LEFT = 0
RIGHT = 1

class Node:
    def __init__(self, value, parent = None):
        self.value = value
        self.parent = parent

    def left(self):
        return self.value[LEFT]

    def set_left(self, n):
        self.value[LEFT] = n
        if type(n) is Node:
            n.parent = self

    def right(self):
        return self.value[RIGHT]

    def set_right(self, n):
        self.value[RIGHT] = n
        if type(n) is Node:
            n.parent = self

    def reduce(self):
        while True:
            nte = self.find_node_to_explode()
            if nte is not None:
                nte.explode()
            else:
                nts, dir = self.find_node_to_split()
                if nts is not None:
                    nts.split(dir)
                else:
                    break

    def sum(self, n):
        parent = Node([self, n])
        self.parent = parent

        if type(n) is Node:
            n.parent = parent

        parent.reduce()

        return parent

    def find_node_to_explode(self, level = 0):
        if level >= 4:
            return self
        l = self.left()
        if type(l) is Node:
            ret = l.find_node_to_explode(level+1)
            if ret is not None:
                return ret
        r = self.right()
        if type(r) is Node:
            ret = r.find_node_to_explode(level+1)
            return ret
        return None

    def explode(self):
        n, dir = self.find_left_value()
        if n is not None:
            n.value[dir] += self.value[0]

        n, dir = self.find_right_value()
        if n is not None:
            n.value[dir] += self.value[1]

        p = self.parent

        if p.left() == self:
            p.set_left(0)
        else:
            p.set_right(0)

    def find_left_value(self):
        p = self.parent

        if p.right() == self:
            if type(p.left()) == int:
                return p, LEFT
            elif p.left() is not None:
                r1, r2 = p.left().find_rightmost_leaf()
                if r1 is not None:
                    return r1, r2

        while True:
            previous = p
            p = p.parent

            while p is not None and p.left() == previous:
                previous = p
                p = p.parent

            if p is None:
                break

            if type(p.left()) == int:
                return p, LEFT
            elif p.left() is not None:
                r1, r2 = p.left().find_rightmost_leaf()
                if r1 is not None:
                    return r1, r2

        return None, None


    def find_rightmost_leaf(self):
        if type(self.right()) is int:
            return self, RIGHT
        if self.right() is not None:
            r1, r2 = self.right().find_rightmost_leaf()
            if r1 is not None:
                return r1, r2
        if self.left() is not None:
            r1, r2 = self.left().find_rightmost_leaf()
            if r1 is not None:
                return r1, r2
        if type(self.left()) is int:
            return self, LEFT
        return None, None





    def find_right_value(self):
        p = self.parent

        if p.left() == self:
            if type(p.right()) == int:
                return p, RIGHT
            elif p.right() is not None:
                r1, r2 = p.right().find_leftmost_leaf()
                if r1 is not None:
                    return r1, r2

        while True:
            previous = p
            p = p.parent

            while p is not None and p.right() == previous:
                previous = p
                p = p.parent

            if p is None:
                break

            if type(p.right()) == int:
                return p, RIGHT
            elif p.right() is not None:
                r1, r2 = p.right().find_leftmost_leaf()
                if r1 is not None:
                    return r1, r2

        return None, None

    def find_leftmost_leaf(self):
        if type(self.left()) is int:
            return self, LEFT
        if self.left() is not None:
            r1, r2 = self.left().find_leftmost_leaf()
            if r1 is not None:
                return r1, r2
        if self.right() is not None:
            r1, r2 = self.right().find_leftmost_leaf()
            if r1 is not None:
                return r1, r2
        if type(self.right()) is int:
            return self, RIGHT
        return None, None



    def split(self, dir):
        n = self.value[dir]
        half = n / 2
        h_l = floor(half)
        h_r = ceil(half)
        self.value[dir] = Node([h_l, h_r], self)

    def find_node_to_split(self):
        l = self.left()
        if type(l) is int:
            if l >= 10:
                return self, LEFT
        else:
            r1, r2 = l.find_node_to_split()
            if r1 is not None:
                return r1, r2

        r = self.right()
        if type(r) is int:
            if r >= 10:
                return self, RIGHT
        else:
            r1, r2 = r.find_node_to_split()
            if r1 is not None:
                return r1, r2

        return None, None

    def is_value_only(self):
        return type(self.left()) is int and type(self.right()) is int

    def magnitude(self):
        while not self.is_value_only():
            current = self
            visited = set()
            while current != None:
                visited.add(current)
                if current.is_value_only():
                    if current == self:
                        break
                    p = current.parent
                    dir = RIGHT
                    if current == p.left():
                        dir = LEFT
                    p.value[dir] = current.left() * 3 + current.right() * 2
                    current = p
                else:
                    if type(current.left()) is Node and current.left() not in visited:
                        current = current.left()
                        continue
                    if type(current.right()) is Node and current.right() not in visited:
                        current = current.right()
                        continue
                    current = current.parent
        return self.left() * 3 + self.right() * 2



    def __repr__(self):
        return str(self)

    def __str__(self):
        s = '[' + str(self.left()) + "," + str(self.right()) + "]"
        return s

def create_node_from_string(s):
    current = Node([None, None])
    dir = LEFT
    n = None
    for i in range(1, len(s)):
        c = s[i]
        if c == ',':
            continue
        if c == '[':
            if dir == LEFT:
                current.set_left(Node([None, None]))
                current = current.left()
            else:
                current.set_right(Node([None, None]))
                current = current.right()
            dir = LEFT
            continue
        if c == ']':
            if current.parent == None:
                break
            current = current.parent
            dir = RIGHT
            continue
        if c.isdigit():
            current.value[dir] = int(c)
            dir = RIGHT
    return current
