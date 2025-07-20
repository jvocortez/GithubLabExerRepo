#PE1

import os, random
import oxo_data

try:
    import oxo_data
except ImportError:
    print("Warning: oxo_data module not found. Using a mock implementation.")
    class MockOxoData:
        def __init__(self):
            self._saved_game = None

        def saveGame(self, game):
            print(f"Mock Save: Saving game {game}")
            self._saved_game = game[:]

        def restoreGame(self):
            if self._saved_game:
                print(f"Mock Restore: Restoring game {self._saved_game}")
                return self._saved_game[:]
                print("Mock Restore: No game saved, simulating IOError.")
                raise IOError("No saved game found (mock error)")
    oxo_data = MockOxoData()


class TicTacToeGame:
    def __init__(self):
        self.game_board = self.newGame()

    def newGame(self):
        ' Return new empty game '
        self.game_board = list(" " * 9)
        return self.game_board

    def saveGame(self):
        ' Save game to disk '
        oxo_data.saveGame(self.game_board)

    def restoreGame(self):
        ''' Restore previously saved game.
        If game not restored successfully return new game'''
        try:
            game = oxo_data.restoreGame()
            if len(game) == 9:
                self.game_board = game
                return self.game_board
            else:
                return self.newGame()
        except IOError:
            return self.newGame()

    def _generateMove(self):
        ''' Generate a random cell from those available.
            If all cells are used return -1'''
        options = [i for i in range(len(self.game_board)) if self.game_board[i] == " "]
        if options:
            return random.choice(options)
        else:
            return -1

    def _isWinningMove(self):
        wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6))

        for a, b, c in wins:
            chars = self.game_board[a] + self.game_board[b] + self.game_board[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False

    def userMove(self, cell):
        """
        Handles a user's move.
        Returns 'X' if user wins, '' otherwise.
        Raises ValueError if the cell is already taken.
        """
        if self.game_board[cell] != ' ':
            raise ValueError('Invalid cell')
        else:
            self.game_board[cell] = 'X'
        if self._isWinningMove():
            return 'X'
        else:
            return ""

    def computerMove(self):
        """
        Handles the computer's move.
        Returns 'O' if computer wins, 'D' if draw, '' otherwise.
        """
        cell = self._generateMove()
        if cell == -1:
            return 'D'
        self.game_board[cell] = 'O'
        if self._isWinningMove():
            return 'O'
        else:
            return ""

    def get_board(self):
        ' Returns the current state of the game board '
        return self.game_board

def test():
    game_instance = TicTacToeGame()
    result = ""
    while not result:
        print(game_instance.get_board())
        try:
            user_cell = game_instance._generateMove()
            if user_cell != -1:
                result = game_instance.userMove(user_cell)
            else:
                pass
        except ValueError:
            print("Oops, that shouldn't happen (invalid cell in test)")

        if not result:
            result = game_instance.computerMove()

        if not result:
            continue
        elif result == 'D':
            print("It's a draw")
        else:
            print("Winner is:", result)
        print(game_instance.get_board())

if __name__ == "__main__":
    test()

-----------------------------------------------------------------------------------

#PE2

import tkinter as tk
from tkinter.filedialog import askopenfilename

filename = None
def UploadAction(event=None):
    filename = askopenfilename()
    filename = filename.split('/')[len(filename.split('/'))-1]
    print('Selected:', filename)
    label1['text'] = filename
    
root= tk.Tk()

button1 = tk.Button(text='Click Me', command=UploadAction, bg='brown', fg='white')
button1.pack(padx=2, pady=5)
label1 = tk.Label(text='Please choose a file')
label1.pack(padx=2, pady=2)

root.mainloop()

-----------------------------------------------------------------------------------

#PE3

import unittest
from unittest.mock import patch
from tic_tac_toe import tic_tac_toe

class TestTicTacToe(unittest.TestCase):

    @patch('builtins.input', side_effect=['0', '0', '1', '1', '0', '2', '1', '0', '2', '2'])
    def test_game_play(self, mock_input):
        with self.assertLogs(level='INFO') as cm:
            tic_tac_toe()

        log_messages = cm.output
        self.assertTrue(any("wins" in message for message in log_messages) or "draw" in log_messages)

    @patch('builtins.input', side_effect=['0', '0', '0', '1', '1', '1', '2', '2', '2', '0'])
    def test_invalid_moves(self, mock_input):
        with self.assertRaises(SystemExit):
            tic_tac_toe()

    @patch('builtins.input', side_effect=['0', '0', '0', '1', '1', '1', '2', '2', '2', '2', '2', '0', '0', '0', '1', '1', '1', '2', '2', '2'])
    def test_full_board_draw(self, mock_input):
        with self.assertLogs(level='INFO') as cm:
            tic_tac_toe()

        log_messages = cm.output
        self.assertTrue("draw" in log_messages)

if __name__ == '__main__':
    unittest.main()
