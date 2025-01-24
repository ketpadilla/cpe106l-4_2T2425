"""
  LAB 04
  PROGRAMMING PROBLEM 03

  Create a unit test program for testing  the Tic Tac Toe Console App.
"""

import unittest
import oxo_logic

class TestOxoLogic(unittest.TestCase):
    
    def test_new_game(self):
        game = oxo_logic.newGame()
        self.assertEqual(game, [" "] * 9, "New game board should be empty")
    
    def test_user_move_valid(self):
        game = oxo_logic.newGame()
        result = oxo_logic.userMove(game, 0)
        self.assertEqual(result, "continue", "Valid move should return 'continue'")
        self.assertEqual(game[0], "X", "Cell should be marked with 'X'")
    
    def test_user_move_invalid(self):
        game = oxo_logic.newGame()
        oxo_logic.userMove(game, 0)  
        result = oxo_logic.userMove(game, 0)  
        self.assertEqual(result, "invalid", "Move on occupied cell should return 'invalid'")
    
    def test_computer_move(self):
        game = oxo_logic.newGame()
        oxo_logic.computerMove(game)
        self.assertIn("O", game, "Computer should place an 'O' somewhere on the board")
    
    def test_win_condition(self):
        game = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
        result = oxo_logic.userMove(game, 3)
        self.assertEqual(result, "win", "Winning move should return 'win'")
    
if __name__ == "__main__":
    unittest.main()

#TODO
