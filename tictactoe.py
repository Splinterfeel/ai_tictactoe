"""
Tic Tac Toe Player
"""

import math
import copy
from langcodes import best_match

from regex import I

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
    ВОЗВРАЩАЕТ Х ИЛИ О - ЧЬЯ ОЧЕРЕДЬ СЕЙЧАС ХОДИТЬ
    """
    sum_O = 0
    sum_X = 0
    for line in board:
        sum_X += len([x for x in line if x == X])
        sum_O += len([o for o in line if o == O])
    if (sum_X == 0): return X
    if (sum_X <= sum_O): return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i,line in enumerate(board):
        for j,cell in enumerate(line): 
            if cell is EMPTY: actions.add( (i, j) )
    return actions


def result(board, action):
    """
    РЕЗУЛЬТАТ ДЕЙСТВИЯ НАД ДОСКОЙ
    """
    _board = copy.deepcopy(board)
    current_player = player(_board)
    _board[action[0]][action[1]] = current_player
    return _board


def winner(board):
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]):
            if (board[i][0] == X): return X
            if (board[i][0] == O): return O
        if (board[0][i] == board[1][i] == board[2][i]):
            if (board[0][i] == X): return X
            if (board[0][i] == O): return O
    if (board[0][0] == board[1][1] == board[2][2]):
        if (board[0][0] == X): return X
        if (board[0][0] == O): return O
    if (board[0][2] == board[1][1] == board[2][0]):
        if (board[0][2] == X): return X
        if (board[0][2] == O): return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board): return True
    for line in board:
        if EMPTY in line: return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    _winner = winner(board)
    if (_winner == X): return 1
    if (_winner == O): return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if (player(board) == X):
        best_value, best_action = max_value(board)
    elif (player(board) == O):
        best_value, best_action = min_value(board)
    return best_action

def min_value(board):
    best_value = 10
    best_action = None
    if (terminal(board)):
        return utility(board), None
    available_actions = actions(board)
    for action in available_actions:
        next_board = result(board, action)
        enemy_max_velue, move = max_value(next_board)
        if (enemy_max_velue < best_value):
            best_value = enemy_max_velue
            best_action = action
    return best_value, best_action
    

def max_value(board):
    best_value = -10
    best_action = None
    if (terminal(board)):
        return utility(board), None
    available_actions = actions(board)
    for action in available_actions:
        next_board = result(board, action)
        enemy_max_velue, move = min_value(next_board)
        if (enemy_max_velue > best_value):
            best_value = enemy_max_velue
            best_action = action
    return best_value, best_action