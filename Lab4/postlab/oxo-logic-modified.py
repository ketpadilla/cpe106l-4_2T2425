"""
  LAB 04
  PROGRAMMING PROBLEM 01

  Convert the oxo-logic.py module to reflect OOP design by creating a Game class.
"""
import os
import random
import oxo_data

class Game:
    def __init__(self):
        self.board = list(" " * 9)

    def save(self, game):
        ' store the current game state to disk '
        oxo_data.saveGame(self.board)

    def restore(self):
        ''' restore previously saved game.
            If game not restored successfully return new game '''
        try:
            self.board = oxo_data.restoreGame()
            if len(self.board) != 9:
                self.board = list(" " * 9)
            return self.board
        except IOError:
            self.board = list(" " * 9)
            return self.board

    def _generateMove(self):
        ''' generate a random cell from those available.
            If all cells are used return -1'''
        options = [i for i in range(len(self.board)) if self.board[i] == " "]
        if options:
            return random.choice(options)
        else:
            return -1

    def _isWinningMove(self):
        wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6))
        game = self.board
        for a, b, c in wins:
            chars = game[a] + game[b] + game[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False

    def userMove(self, cell):
        if self.board[cell] != ' ':
            raise ValueError('Invalid cell')
        else:
            self.board[cell] = 'X'
            if self._isWinningMove():
                return 'X'
            else:
                return ""

    def computerMove(self):
        cell = self._generateMove()
        if cell == -1:
            return 'D'
        self.board[cell] = 'O'
        if self._isWinningMove():
            return 'O'
        else:
            return ""

    def printBoard(self):
        print("-------------")
        for i in range(0, 9, 3):
            print("| " + self.board[i] + " | " + self.board[i+1] + " | " + self.board[i+2] + " |")
            print("-------------")

def test():
    result = ""
    game = Game()
    while not result:
        print("Current board:")
        game.printBoard()
        try:
            result = game.userMove(game._generateMove())
        except ValueError:
            print("Oops, that shouldn't happen")
        if not result:
            result = game.computerMove()
        if not result:
            continue
        elif result == 'D':
            print("It's a draw")
        else:
            print("Final board:")
            game.printBoard()
            if result == 'X':
                print("Winner is: User (X)")
            elif result == 'O':
                print("Winner is: Computer (O)")

if __name__ == "__main__":
    test()
"""
  This is a copy of the file ./inlab/OXO/oxo-logic.py for easier reference of requirements
"""

#TODO
