from board import (
    create_board,
    print_board,
    place_piece,
    random_play,
)
from cli import get_name, get_int, ask_move, ask_yes_no, clear_screen
from rules import evaluate_state

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

def play_match(game):
    '''
        Juega una sola partida sobre game["board"]
        Termina cuando evaluate_state deja de devolver "running"
    '''
    board = game["board"]
    user_s = game["user_symbol"]
    ia_s = game["ia_symbol"]
    k = game["k"]
    
    while game["state"] == "running":
        print_board(board)
        
        # Turno del usuario
        pos = ask_move(board)
        place_piece(board, pos, user_s)
        game["state"] = evaluate_state(board, k, user_s, ia_s)
        
        if game["state"] != "running":
            break # La IA no juega si el juego ya terminó
        
        # Turno de la IA
        ia_pos = random_play(board)
        place_piece(board, ia_pos, ia_s)
        print(f"La IA juega en fila {ia_pos[0]+1}, columna {ia_pos[1]+1}\n")
        game["state"] = evaluate_state(board, k, user_s, ia_s)
    
    return game["state"]

def show_result(game):
    '''Muestra el tablero final y el mensaje correspondiente al estado'''
    print_board(game["board"])
    if game["state"] == "victory":
        print("Ganaste!")
    elif game["state"] == "defeat":
        print("Perdiste, mejor suerte la próxima")
    elif game["state"] == "draw":
        print("Empate")
    else:
        print(f"Estado desconocido... {game['state']}") # Esto no debería ocurrir

def configure_match(name):
    '''Pide n y k y devuelve una partida nueva, con tablero limpio'''
    n = get_int("Tamaño del tablero (3-9): ", 3, 9)
    k = get_int(f"Cantidad de fichas para ganar (3-{n}): ", 3, n)
    return create_game(name, n, k)

def main():
    '''Función principal que gestiona el progreso del juego'''
    clear_screen()
    
    print("TicTacToe NxN")
    name = get_name()
    game = configure_match(name)
    
    while True:
        n = game["n"]
        k = game["k"]
        print(f"\nHola {name}")
        print(f"Bienvenido a TicTacToe {n}x{n}, conecta {k} fichas seguidas para ganar")
        play_match(game)
        show_result(game)
        
        if not ask_yes_no("\nOtra partida? (s/n): "):
            break
        if not ask_yes_no("\nMismo usuario? (s/n): "):
            name = get_name()
        
        clear_screen()
        game = configure_match(name)
    print("\nGracias por jugar :3")

if __name__ == "__main__":
    main()