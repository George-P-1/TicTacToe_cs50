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
    # Iterate through the 3x3 board to check for winner
    for i in range(3):
        # Check vertically
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]
        # Check horizontally
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
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


def minimax(board):
    """
    Returns the optimal action for the current player on the board
    """
    optimal_action, _ = helper(board)
    return optimal_action

        
def helper(board):
    """
    Returns optimal action and utility score.
    Recursive function to find optimal action that corresponds to optimal utility score (-1, 0 or 1).
    """
    # if terminal state then return utility score
    if terminal(board):
        return None, utility(board)
    
    # X is maximizing player, O is minimizing player
    current_player = player(board)
    optimal_action = None
    
    # Initialize best value based on player type
    if current_player == X:
        best_value = -math.inf
        # Loop through all possible actions and choose the one with the max value
        for action in actions(board):
            _ , action_value = helper(result(board, action))
            if action_value > best_value:
                best_value = action_value
                optimal_action = action
            if best_value == 1:   # If we find an optimal (maximal) move, return it. Reduces computation.
                return optimal_action, best_value
        return optimal_action, best_value
    
    elif current_player == O:
        best_value = math.inf
        # Loop through all possible actions and choose the one with the min value
        for action in actions(board):
            _ , action_value = helper(result(board, action))
            if action_value < best_value:
                best_value = action_value
                optimal_action = action
            if best_value == -1:    # If we find an optimal (minimal) move, return it. Reduces computation.
                return optimal_action, best_value
        return optimal_action, best_value