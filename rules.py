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

def evaluate_state(board, k, user_s, ia_s):
    '''
        Devuelve el estado de la partida:
        - "victory" si el usuario tiene k en línea
        - "defeat" si la IA tiene k en línea
        - "draw" si el tablero está lleno sin línea
        - "running" en caso contrario
    '''
    if has_line(board, user_s, k):
        return "victory"
    if has_line(board, ia_s, k):
        return "defeat"
    if full_board(board):
        return "draw"
    return