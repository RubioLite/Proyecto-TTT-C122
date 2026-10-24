from board import create_board, print_board, free_space, random_play
from rules import full_board
import os

def get_name():
    '''Pide un nombre y rechaza cadenas vacías o de solo espacios'''
    while True:
        name = input("Como te llamas? ").strip()
        if name:
            return name
        print("El nombre no puede ser vacío ni de solo espacios")

def get_int(message, low, high):
    '''Pide un entero dentro del rango [min, max]. Repite hasta lograrlo'''
    while True:
        entry = input(message)
        try:
            value = int(entry)
        except ValueError:
            print("Debes escribir un número entero")
            continue
        
        if value < low or value > high:
            print(f"El número debe estar entre {low} y {high}")
            continue
        return value

def create_game(name, n, k):
    '''Crea y devuelve el diccionario que representa la partida'''
    return {
        "player": name,
        "n": n,
        "k": k,
        "board": create_board(n),
        "user_symbol": "X",
        "ia_symbol": "O",
        "state": "running",
    }

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
    ia_s = game["ia_symbol"]
    
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