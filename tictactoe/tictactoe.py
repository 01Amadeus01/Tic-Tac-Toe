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
    if terminal(board):
        return None
    x = o = 0
    for outer in board:
        for inner in outer:
            if inner == X:
                x += 1
            elif inner == O:
                o += 1
    if x == o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    i - row
    j - column
    """
    possible_moves = set()
    if terminal(board):
        return None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.add((i,j))
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_1 = copy.deepcopy(board)
    turn = player(board_1)
    if 0 <= action[0] <= 2 and 0 <= action[1] <= 2:
        board_1[action[0]][action[1]] = turn
    else:
        raise Exception("Action not valid")
    return board_1


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    dx, do, ddx, ddo = 0, 0, 0, 0
    for i in range(3):
        rx, ro, cx, co= 0, 0, 0, 0
        for j  in range(3):
            if board[i][j] == X:
                rx += 1
            elif board[i][j] == O:
                ro += 1
            if board[j][i] == X:
                cx += 1
            elif board[j][i] == O:
                co += 1
            if i == j:
                if board[i][j] == X:
                    dx += 1
                elif board[i][j] == O:
                    do += 1
            if i+j == 2:
                if board[i][j] == X:
                    ddx += 1
                elif board[i][j] == O:
                    ddo += 1
        if rx == 3 or cx == 3 or dx == 3 or ddx == 3:
            return X
        if ro == 3 or co == 3 or do == 3 or ddo == 3:
            return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    c = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                c += 1
    if winner(board) or c == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    uti = winner(board)
    if uti == X:
        return 1
    elif uti == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_val(board, alpha, beta, depth = 0):
        if terminal(board):
            return utility(board)
        print(depth)
        v = float('-inf')
        for move in actions(board):
            v1 = min_val(result(board, move), alpha, beta, depth+1)
            if v1 > v:
                v = v1
                if alpha < v:
                    alpha = v
                optimal_move = move
            if alpha >= beta:
                break
        if depth == 0:
            return v, optimal_move
        else:
            return v
    def min_val(board, alpha, beta, depth = 0):
        if terminal(board):
            return utility(board)
        print(depth)
        v = float('inf')
        for move in actions(board):
            v1 = max_val(result(board, move), alpha, beta, depth+1)
            if v1 < v:
                v = v1
                if beta > v:
                    beta = v
                optimal_move = move
            if alpha >= beta:
                break
        if depth == 0:
            return v, optimal_move
        else:
            return v
        
    alpha = float('-inf')
    beta = float('inf')
    if player(board) == X:
        return(max_val(board, alpha, beta)[1])
    elif player(board) == O:
        return(min_val(board, alpha, beta)[1])
    

    