from ..shared.initialize_grid import initialize_grid
from ..shared.move import move
from ..shared.board_formatter import board_formatter
from ..shared.check_for_moves import check_for_moves
from ..shared.max_cell_searcher import max_cell_searcher
import time

# Modalidad para un jugador
def single_player(base, nameUser, modality):

    #Mensaje de inicio
    print("\nSu partida comienza en 3...")
    time.sleep(1)
    print("Su partida comienza en 2...")
    time.sleep(1)
    print("Su partida comienza en 1...")
    time.sleep(1)
    print("\n¡A jugar!")


    # Se genera el tablero y se imprime
    player_board = initialize_grid(base, modality)
    board_formatter(grid=player_board, sum=0)
    # Se inicia un ciclo para pedir el movimiento e imprimir el tablero
    play = True
    while play:
        # Chequeo por posibles movimientos
        if not check_for_moves(player_board):
            print("Ya no hay movimientos Posibles!\n")
            play = False
            max_cell = max_cell_searcher(player_board)

            return [sum, max_cell, movements]

        direction = input("\nIngrese su movimiento a, w, s, d: ")
        if direction and play:
            # Movimiento y posterior impresión
            player_board, sum, movements = move(player_board, direction, base, nameUser, modality)
            board_formatter(player_board, sum=sum)

            # Chequeo si gano el juego
            for i in range(4):
                if (base * 1024) in player_board[i]:
                    print("\nLlegó a", base * 1024, "¡felicitaciones has ganado el juego! :D\n")
                    play = False
                    max_cell = max_cell_searcher(player_board)

                    return [sum, max_cell, movements]