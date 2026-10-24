# TicTacToe NxN

Juego de tres en raya (tic-tac-toe) para tableros de N×N (3 ≤ N ≤ 9), donde
el jugador se enfrenta a una IA que, por ahora, elige sus jugadas al azar.

> **Estado:** Semana 2 completada — código modular, coordenadas como tuplas y
> detección genérica de líneas (`has_line`). La conexión de `has_line` al flujo
> de juego (victoria/derrota) llega en la Semana 3.

## Características

- Tablero configurable de N×N (3 a 9).
- Cantidad de fichas a alinear (K) configurable entre 3 y N.
- Entrada validada: nombre no vacío, enteros dentro de rango, casillas ocupadas.
- La IA nunca elige una casilla ocupada.
- Sin dependencias externas: solo Python 3.

## Requisitos

- Python 3.6 o superior.

## Cómo ejecutar

```bash
python main.py
```

## Cómo jugar

1. Introduce tu nombre.
2. Elige el tamaño del tablero (3 a 9).
3. Elige cuántas fichas seguidas necesitas para ganar (3 a N).
4. En cada turno, escribe fila y columna (en base 1, de 1 a N).
5. La IA responde automáticamente con una jugada aleatoria.
6. El tablero se imprime en cada turno con índices en base 1.
7. La partida termina cuando el tablero se llena.

> **Nota:** En esta versión todavía no se detectan victorias en el flujo de
> juego; la partida continúa hasta llenar el tablero. La lógica de detección
> ya existe (`has_line`) y está cubierta por tests, pero se conecta al flujo
> en la Semana 3.

## Estructura del proyecto

```text
.
├── main.py          # Flujo: pedir datos, bucle de turnos
├── cli.py           # Entrada por consola: get_name, get_int, ask_move
├── board.py         # Tablero: crear, imprimir, mover, casillas libres
├── rules.py         # Reglas: line_from, has_line, full_board
└── test_reglas.py   # Tests con assert para rules.py
```

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Pide datos, orquesta turnos, imprime tablero. No sabe de reglas ni de casillas. |
| `cli.py` | Todo el I/O interactivo (`input`, validaciones, `ask_move`). |
| `board.py` | Pura manipulación de la matriz N×N. Sin `input`, sin `print` de mensajes de juego. |
| `rules.py` | Consultas sobre la matriz: ¿hay línea? ¿está lleno? Sin dibujar nada. |
| `test_reglas.py` | Congela el comportamiento de `has_line` y `full_board`. |

## Cómo probar

```bash
python test_reglas.py
```

Debe imprimir `Todo correcto — reglas.py verificado.` Si algún assert falla,
Python muestra la línea exacta del fallo.

## Roadmap

- [x] **Semana 1**: datos iniciales, tablero N×N y turnos con IA aleatoria.
- [x] **Semana 2**: código modular, coordenadas como tuplas y `has_line` genérica.
- [ ] **Semana 3**: conectar `has_line` al flujo, estados de partida y fin de juego por victoria/derrota.
- [ ] (Futuro) IA con minimax en un módulo `ia.py`.
- [ ] (Futuro) Perfiles de jugador (`perfiles.py`).