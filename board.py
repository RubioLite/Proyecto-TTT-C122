import random

def create_board(n):
    '''
        Devuelve una lista de n filas con n casillas " " cada una
        Cada lista se construye por separado con list comprehension
    '''
    return [[" " for _ in range(n)] for _ in range(n)]

def print_board(board):
    '''Imprime el tablero con números por fila o columnas en base 1'''
    n = len(board)
    width = len(str(n)) # Ancho de la etiqueta de la fila (1 cuando n <= 9)
    cell = 3            # Ancho de cada casilla: " X "

    header = [" "] * (width + 2 + 4 * n)
    for i in range(n):
        header[width + 3 + 4 * i] = str(i + 1)
    print("".join(header))
    separator = " " * (width + 1) + ("+" + "-" * cell) * n + "+"
    print(separator) # Fue duro escribir esto, el prueba y error fue grande xDDD
        
    # FILAS
    for i in range(n):
        line = f"{i+1:>{width}} |"
        for j in range(n):
            line += f" {board[i][j]} |"
        print(line)
        print(separator)

def free_space(board, pos):
    '''True si la casilla pos = (row, col) está vacía'''
    row, col = pos
    return board[row][col] == " "

def place_piece(board, pos, symbol):
    '''Coloca symbol en la casilla pos = (row, col)'''
    row, col = pos
    board[row][col] = symbol
    
def free_moves(board):
    '''Devuelve una lista de tuplas (row, col) con todas las casillas libres'''
    n = len(board)
    return [(i, j) for i in range(n) for j in range(n) if free_space(board, (i, j))]

def random_play(board):
    '''
        Devuelve (fila, columna) de una casilla libre elegida al azar
        (Más adelante esto será cambiado por un algoritmo mini-max simple)
    '''
    free = free_moves(board)
    if not free:
        raise ValueError("No quedan casillas libres")
    return random.choice(free)