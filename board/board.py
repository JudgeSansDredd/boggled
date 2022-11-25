class Board:
    def __init__(self, layout):
        self.layout = layout
        self.dimension = len(layout)

    def get_letter(self, pos):
        x, y = pos
        return self.layout[y][x]

    def print(self):
        for row in self.layout:
            print(''.join(row))
