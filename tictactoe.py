"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X    # NOTE - Always starts with X 
    elif sum(1 if element==EMPTY else 0 for row in board for element in row) % 2 == 0:
        return O    # O plays when there are even number of empty cells
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_cells = list()
    for i, row in enumerate(board):
        for j, element in enumerate(row):
            if element == EMPTY:
                empty_cells.append((i, j))
    return empty_cells



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")
    # NOTE - Make copy cuz minimax uses this function to simulate future moves. So won't change original board.
    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check horizontally
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]
    # Check vertically
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]
    # Check diagonally
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    # If no winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):         # NOTE - (End of recursion) If end state then return the final score
        return utility(board)
    if player(board) == X:      # NOTE - X is maximizing player
        value = -math.inf       # Initialize variable in order to find highest possible score
        for action in actions(board):
            value = max(value, minimax(result(board, action)))
        raise NotImplementedError
    elif player(board) == O:    # NOTE - O is minimizing player
        value = math.inf        # Initialize variable in order to find lowest possible score
        for action in actions(board):
            value = min(value, minimax(result(board, action)))
        raise NotImplementedError
