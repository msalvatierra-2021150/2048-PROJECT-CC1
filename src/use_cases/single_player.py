from ..shared.initialize_grid import initialize_grid
from ..shared.move import move
from ..shared.board_formatter import board_formatter

# Modalidad para un jugador
def single_player():
    # Se genera el tablero y se imprime
    player_board = initialize_grid()
    board_formatter(player_board)

    # Se inicia un ciclo para pedir el moviento e imprimir el tablero
    while True:
        direction = input("\nIngrese su movimento a, w, s, d: ")
        if direction:
            player_board = move(player_board, direction)
            board_formatter(player_board)