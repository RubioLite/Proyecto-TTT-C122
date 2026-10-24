import random
import os

def get_name():
    '''Pide un nombre y rechaza cadenas vacías o de solo espacios'''
    while True:
        name = input("Como te llamas? ").strip()
        if name:
            return name
        print("El nombre no puede ser vacío ni de solo espacios")

def get_int(message, min, max):
    '''Pide un entero dentro del rango [min, max]. Repite hasta lograrlo'''
    while True:
        input = input(message)
        try:
            value = int(input)
        except ValueError:
            print("Debes escribir un número entero")
            continue
        
        if value < min or value > max:
            print(f"El número debe estar entre {min} y {max}")
            continue
        return value
        

def create_game(name, n, k):
    '''
        Devuelve una lista de n filas con n casillas " " cada una
        Cada lista se construye por separado con list comprehension
    '''
    return [[" " for _ in range(n)] for _ in range(n)]

def full_board(board):
    '''True si ya no quedan casillas vacías'''
    for row in board:
        if " " in row:
            return False
    return True

def print_board(board):
    '''Imprime el tablero con números por fila o columnas en base 1'''
    n = len(board)
    width = len(str(n)) # Ancho de la etiqueta de la fila (1 cuando n <= 9)
    cell = 3            # Ancho de cada casilla: " X "

    header = [" "] * (width + 2 + 4 * n)
    for i in range(n):
        header[width + 3 + 4 * i] = str(j + 1)
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

def free_space(board, row, col):
    '''True si la casilla (row, col) está vacía'''
    return board[row][col] == " "

def random_play(board):
    pass

def play():
    '''
        Función principal que gestiona el progreso del juego
    '''
    
    print("TicTacToe NxN")
    
    name = get_name()
    n = get_int("Tamaño del tablero (3-9):", 3, 9)
    k = get_int(f"Cantidad de fichas para ganar (3-{n})", 3, n)
    game = create_game(name, n, k)
    board = game["board"]
    user_s = game["user_symbol"]
    ia_s = game["user_symbol"]
    
    print(f"\nHola {name}")
    print(f"Bienvenido a TicTacToe {n}x{n}, conecta {k} fichas seguidas para ganar")
    
    while not full_board(board):
        print_board(board)
        
        # Turno del usuario
        while True:
            row = get_int(f"Fila (1-{n}): ", 1, n) - 1 # Para trabajar indexado desde 0
            col = get_int(f"Columna (1-{n}): ", 1, n) - 1
            if free_space(board, row, col):
                break
            print("Casilla ocupada, por favor selecciona otra")
        board[row][col] = user_s
        
        if full_board(board):
            break # Si ya el tablero está lleno, la IA no puede jugar
        
        # Turno de la IA
        r_ia, c_ia = random_play(board)
        board[r_ia][c_ia] = ia_s
        print(f"La ia juega en fila {r_ia+1}, columna {c_ia+1}\n")
    
    print_board(board)
    print("Fin de la partida. Gracias por jugar :3")

if __name__ == "__main__":
    play()