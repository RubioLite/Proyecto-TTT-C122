from board import within_bounds, free_moves

DIRECTIONS = [(0,1), (1,0), (1,1), (1,-1)]

def line_from(board, pos, direction, symbol, k):
    '''True si a partir de pos hay k fichas seguidas de symbol en direction'''
    n = len(board)
    row, col = pos
    dr, dc = direction
    
    for _ in range(k):
        if not within_bounds(n, (row, col)):
            return False
        if board[row][col] != symbol:
            return False
        row += dr
        col += dc
    return True

def has_line(board, symbol, k):
    '''True si symbol tiene k fichas seguidas en cualquier dirección desde cualquier posición'''
    n = len(board)
    for i in range(n):
        for j in range(n):
            for direction in DIRECTIONS:
                if line_from(board, (i, j), direction, symbol, k):
                    return True
    return False

def full_board(board):
    '''True si ya no quedan casillas vacías'''
    return not free_moves(board)