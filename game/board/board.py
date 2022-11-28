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

    def pos_in_board(self, pos):
        x, y = pos
        return x >= 0 and x < self.dimension and y >= 0 and y < self.dimension

    def _extend_path(self, path, newPos):
        newPath = []
        newPath.extend(path)
        newPath.append(newPos)
        return newPath

    def find_word(self, word, path=None):
        # Make sure a word was provided
        if len(word) == 0:
            return False

        if path is None:
            # Starting here
            for i in range(self.dimension):
                for j in range(self.dimension):
                    result = self.find_word(
                        word,
                        [(i, j)]
                    )
                    if result:
                        return result
            return False
        else:
            # We've already started, we have a word to check
            wordAttempt = ''.join([self.get_letter(pos) for pos in path])
            wordAbbrev = word[:len(wordAttempt)]
            if wordAttempt != wordAbbrev:
                return False

            # If we get here, all letters so far match
            if len(word) == len(path):
                # We have all the letters
                return path

            # We need more letters
            curr_pos = path[-1:][0]
            i, j = curr_pos
            left = (i - 1, j)
            right = (i + 1, j)
            up = (i, j - 1)
            down = (i, j + 1)
            if self.pos_in_board(right) and right not in path:
                result = self.find_word(
                    word,
                    self._extend_path(path, right)
                )
                if result:
                    return result
            if self.pos_in_board(down) and down not in path:
                result = self.find_word(
                    word,
                    self._extend_path(path, down)
                )
                if result:
                    return result
            if self.pos_in_board(left) and left not in path:
                result = self.find_word(
                    word,
                    self._extend_path(path, left)
                )
                if result:
                    return result
            if self.pos_in_board(up) and up not in path:
                result = self.find_word(
                    word,
                    self._extend_path(path, up)
                )
                if result:
                    return result

            # If we get here, nothing worked
            return False
