from ..shared.operations.initialize_grid import initialize_grid
from ..shared.move.move import move
from ..shared.results.board_formatter import board_formatter
from ..shared.operations.check_for_moves import check_for_moves
from ..shared.operations.max_cell_searcher import max_cell_searcher
from ..shared.move.machine_algorithm import machine_algorithm
import time

# Modalidad para un jugador
def machine(base, nameUser, modality):

    #Mensaje de inicio
    print("\nSu partida comienza en 3...")
    time.sleep(1)
    print("Su partida comienza en 2...")
    time.sleep(1)
    print("Su partida comienza en 1...")
    time.sleep(1)
    print("\n¡A jugar!")


    # Se genera el tablero y se imprime
    machine_board = initialize_grid(base, modality)
    board_formatter(machine_board, sum=0, movements=0)
    old_direction = None
    # Se inicia un ciclo para pedir el movimiento e imprimir el tablero
    play = True
    while play:
        # Chequeo por posibles movimientos
        if not check_for_moves(machine_board):
            print("Ya no hay movimientos Posibles!\n")
            play = False
            max_cell = max_cell_searcher(machine_board)

            return [points, max_cell, movements]

        input("\nPresione ENTER para que la máquina se mueva: ")
        direction = machine_algorithm(machine_board, base, nameUser, old_direction)
        old_direction = direction
        print(direction)
        if direction and play:
            # Movimiento y posterior impresión
            machine_board, sum, points, movements = move(machine_board, direction, base, nameUser, modality, print_index=1)
            board_formatter(machine_board, sum=points)

            # Chequeo si gano el juego
            for i in range(4):
                if (base * 1024) in machine_board[i]:
                    print("\nLlegó a", base * 1024, "¡felicitaciones has ganado el juego! :D\n")
                    play = False
                    max_cell = max_cell_searcher(machine_board)

                    return [points, max_cell, movements]