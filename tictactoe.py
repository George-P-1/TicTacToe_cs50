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
    if board == initial_state():    # REVIEW - Initial state is probably included in the else part below
        return X    # NOTE - Always starts with X 
    elif sum(1 if element==EMPTY else 0 for row in board for element in row) % 2 == 0:
        return O    # O plays when there are even number of empty cells
    else:
        return X    # X plays when there are odd number of empty cells


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
    # REVIEW - Checking for horizontal and vertical can be done in the same for loop maybe
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
    # game over if someone won
    if winner(board) != None:
        return True
    # if any cell is empty, game not over
    for row in board:
        for element in row:
            if element == EMPTY:
                return False
    # All cells filled
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winning_player = winner(board)
    if winning_player == X:
        return 1
    elif winning_player == O:
        return -1
    else:
        return 0


# REMOVE_LATER - I think the AI/algorithm is not smart cuz it only looks one move ahead since there is no recursion
# REMOVE_LATER - utility() only returns a valid value if board is in terminal state. Otherwise it returns a 0 
# which is not useful information for the algorithm.
# REMOVE_LATER - The algorithm at least works a little because sometimes the optimal move is the action that corresponds to
# when the utility() function returns the default 0 value. 
# REVIEW - Can also initialize the best_val variable with the least desirable value instead of infinites
def minimax(board):
    """
    Returns the optimal action for the current player on the board. and minimax score that was chosen (-1, 0 or 1).
    """

    # in the last state where only 2 empty cell is available
    optimal_action = None
    if player(board) == X:      # X is maximizing player
        best_val = -1
        for action in actions(board):
            new_board = result(board, action)
            if not terminal(new_board):
                return minimax(new_board)
            else:
                val = utility(new_board)
                if val > best_val:
                    best_val = val
                    optimal_action = action
    elif player(board) == O:        # O is minimizing player
        best_val = 1
        for action in actions(board):
            new_board = result(board, action)
            if not terminal(new_board):
                return minimax(new_board)
            else:
                val = utility(new_board)
                if val < best_val:
                    best_val = val
                    optimal_action = action
    else:
        # A terminal board shouldn't be given to minimax
        raise NotImplementedError
    return optimal_action
