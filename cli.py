from board import free_space

def get_name():
    '''Pide un nombre y rechaza cadenas vacías o de solo espacios'''
    while True:
        name = input("Como te llamas? ").strip()
        if name:
            return name
        print("El nombre no puede ser vacío ni de solo espacios")

def get_int(message, low, high):
    '''Pide un entero dentro del rango [low, high]. Repite hasta lograrlo'''
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
    
def ask_move(board):
    '''Pide fila y columna en base 1 hasta obtener una casilla vacía'''
    n = len(board)
    while True:
        row = get_int(f"Fila (1-{n}): ", 1, n) - 1
        col = get_int(f"Columna (1-{n}): ", 1, n) - 1
        pos = (row, col)
        if free_space(board, pos):
            return pos
        print("Casilla ocupada, por favor selecciona otra")