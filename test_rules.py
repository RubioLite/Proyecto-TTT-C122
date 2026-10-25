from rules import has_line, full_board, line_from, evaluate_state

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
assert line_from(corner, (0, 0), (0, -1), "X", 3) is False
# Desde (0,0) hacia arriba (-1,0): sale del tablero en el paso 1
assert line_from(corner, (0, 0), (-1, 0), "X", 3) is False

# ---------------------------------------------------------------------------
# 9. evaluate_state: línea de X → "victory"
# ---------------------------------------------------------------------------
board = [
    ["X", "X", "X"],
    [" ", " ", " "],
    [" ", " ", " "],
]
assert evaluate_state(board, 3, "X", "O") == "victory"


# ---------------------------------------------------------------------------
# 10. evaluate_state: línea de O → "defeat"
# ---------------------------------------------------------------------------
board = [
    ["O", " ", " "],
    ["O", " ", " "],
    ["O", " ", " "],
]
assert evaluate_state(board, 3, "X", "O") == "defeat"


# ---------------------------------------------------------------------------
# 11. evaluate_state: tablero lleno sin línea → "draw"
#     Patrón específico para 3×3 que no tiene ninguna línea de 3.
# ---------------------------------------------------------------------------
board = [
    ["X", "O", "X"],
    ["O", "O", "X"],
    ["X", "X", "O"],
]
assert evaluate_state(board, 3, "X", "O") == "draw"


# ---------------------------------------------------------------------------
# 12. evaluate_state: tablero con espacios y sin línea → "running"
# ---------------------------------------------------------------------------
board = [
    ["X", " ", " "],
    [" ", "O", " "],
    [" ", " ", " "],
]
assert evaluate_state(board, 3, "X", "O") == "running"


# ---------------------------------------------------------------------------
# 13. evaluate_state: prioridad — X gana con tablero lleno → "victory"
#     (no "draw", no "defeat"; verifica que el orden de checks es correcto)
# ---------------------------------------------------------------------------
board = [
    ["X", "X", "X"],   # fila ganadora del usuario
    ["O", "O", "O"],   # fila ganadora de la IA (caso artificial)
    ["X", "O", "X"],   # relleno para que el tablero esté lleno
]
assert evaluate_state(board, 3, "X", "O") == "victory"


# ---------------------------------------------------------------------------
# 14. evaluate_state: K = 3 en tablero 5×5 → "victory"
#     (no solo en 3×3; verifica que k se pasa correctamente)
# ---------------------------------------------------------------------------
board = [
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    ["X", "X", "X", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
]
assert evaluate_state(board, 3, "X", "O") == "victory"
assert evaluate_state(board, 4, "X", "O") == "running"   # k=4 no se cumple

print("Todo correcto — reglas.py verificado")