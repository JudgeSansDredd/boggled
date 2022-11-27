from .board.board import Board
from .dice.dice import rollDice
from .dictionary.dictionary import Dictionary
from .screen.boggle_screen import Boggle_Screen


class Game:
    def __init__(self, board_dimensions):
        self.board = Board(rollDice(board_dimensions))
        self.screen = Boggle_Screen()
        self.dictionary = Dictionary()
        self.check_word = ''

    def tick(self):
        response = {}
        event_response = self.screen.do_events()
        self.check_word = self.screen.check_word
        path = self.board.find_word(self.check_word)
        self.screen.draw_screen(self.board, path)
        if 'quit' in event_response and event_response['quit']:
            response['quit'] = True
        elif 'lookup' in event_response and event_response['lookup']:
            dictionary_response = self.dictionary.get_definition(self.check_word)
            if dictionary_response['found']:
                self.screen.definition = " ".join(
                    [
                        f"{i + 1}) {d}"
                        for i, d
                        in enumerate(dictionary_response['definitions'])
                    ]
                )
            else:
                suggestions = ", ".join(dictionary_response['suggestions'])
                self.screen.definition = f"Did you mean?: {suggestions}"

        return response
