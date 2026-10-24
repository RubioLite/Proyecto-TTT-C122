def full_board(board):
    '''True si ya no quedan casillas vacías'''
    for row in board:
        if " " in row:
            return False
    return True