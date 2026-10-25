from board import (
    create_board,
    print_board,
    place_piece,
    random_play,
)
from cli import get_name, get_int, ask_move
from rules import full_board

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
    '''Función principal que gestiona el progreso del juego'''
    
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
        pos = ask_move(board)
        place_piece(board, pos, user_s)
        
        if full_board(board):
            break # Si ya el tablero está lleno, la IA no puede jugar
        
        # Turno de la IA
        ia_pos = random_play(board)
        place_piece(board, ia_pos, ia_s)
        print(f"La ia juega en fila {ia_pos[0]+1}, columna {ia_pos[1]+1}\n")
    
    print_board(board)
    print("Fin de la partida. Gracias por jugar :3")

if __name__ == "__main__":
    play()