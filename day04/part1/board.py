MARKED = -1

class Board:
    def __init__(self, input):
        self.numbers = input.copy()

    def mark_number(self, number):
        for i in range(5):
            for j in range(5):
                if self.numbers[i][j] == number:
                    self.numbers[i][j] = MARKED
                    return True
        return False

    def row_win(self, row):
        for n in row:
            if n != MARKED:
                return False
        return True

    def col_win(self, i):
        for row in self.numbers:
            if row[i] != MARKED:
                return False
        return True

    def did_win(self):
        for row in self.numbers:
            if self.row_win(row):
                return True
        for i in range(5):
            if self.col_win(i):
                return True
        return False

    def sum_all_unmarked(self):
        acc = 0
        for row in self.numbers:
            for n in row:
                if n != MARKED:
                    acc += n
        return acc