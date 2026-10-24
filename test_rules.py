from rules import has_line, full_board

# ---------------------------------------------------------------------------
# 1. Fila completa de X en 3×3
# ---------------------------------------------------------------------------
board = [
    ["X", "X", "X"],
    [" ", " ", " "],
    [" ", " ", " "],
]
assert has_line(board, "X", 3) is True
assert has_line(board, "O", 3) is False


# ---------------------------------------------------------------------------
# 2. Columna completa de X en 3×3
# ---------------------------------------------------------------------------
board = [
    [" ", "X", " "],
    [" ", "X", " "],
    [" ", "X", " "],
]
assert has_line(board, "X", 3) is True


# ---------------------------------------------------------------------------
# 3. Diagonal principal \ de X en 3×3
# ---------------------------------------------------------------------------
board = [
    ["X", " ", " "],
    [" ", "X", " "],
    [" ", " ", "X"],
]
assert has_line(board, "X", 3) is True


# ---------------------------------------------------------------------------
# 4. Diagonal secundaria / de X en 3×3
# ---------------------------------------------------------------------------
board = [
    [" ", " ", "X"],
    [" ", "X", " "],
    ["X", " ", " "],
]
assert has_line(board, "X", 3) is True


# ---------------------------------------------------------------------------
# 5. K < N: tres X seguidas en un tablero 5×5 con k=3
#    (y k=4 debe dar False porque solo hay 3)
# ---------------------------------------------------------------------------
board = [
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    ["X", "X", "X", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
]
assert has_line(board, "X", 3) is True
assert has_line(board, "X", 4) is False


# ---------------------------------------------------------------------------
# 6. Tablero con fichas repartidas pero sin línea → False
# ---------------------------------------------------------------------------
board = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "X", "X"],
]
assert has_line(board, "X", 3) is False
assert has_line(board, "O", 3) is False


# ---------------------------------------------------------------------------
# 7. full_board: tablero vacío → False; tablero lleno → True
# ---------------------------------------------------------------------------
empty_3x3 = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]
assert full_board(empty_3x3) is False

full_2x2 = [
    ["X", "O"],
    ["O", "X"],
]
assert full_board(full_2x2) is True


# ---------------------------------------------------------------------------
# 8. Borde: celda en la esquina con dirección que sale del tablero
#    Debe devolver False, no lanzar IndexError.
# ---------------------------------------------------------------------------
corner = [
    ["X", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]
# Desde (0,0) hacia la izquierda (0,-1): sale del tablero en el paso 1
from rules import line_from
assert line_from(corner, (0, 0), (0, -1), "X", 3) is False
# Desde (0,0) hacia arriba (-1,0): sale del tablero en el paso 1
assert line_from(corner, (0, 0), (-1, 0), "X", 3) is False


print("Todo correcto — reglas.py verificado")