from ..shared.initialize_grid import initialize_grid
from ..shared.move import move
from ..shared.board_formatter import board_formatter
from ..shared.check_for_moves import check_for_moves

# Modalidad para un jugador
def single_player(base, nameUser):
    # Se genera el tablero y se imprime
    player_board = initialize_grid(base)
    board_formatter(grid=player_board, sum=0)
    # Se inicia un ciclo para pedir el movimiento e imprimir el tablero
    play = True
    while play:
        # Chequeo por posibles movimientos
        if not check_for_moves(player_board):
            print("Ya no hay movimientos Posibles!\n")
            play = False
            _mainLoop()
            return

        direction = input("\nIngrese su movimiento a, w, s, d: ")
        if direction and play:
            # Movimiento y posterior impresión
            player_board, sum = move(player_board, direction, base, nameUser)
            board_formatter(player_board, sum=sum)

            # Chequeo si gano el juego
            for i in range(4):
                if (base * 1024) in player_board[i]:
                    print("\nLlegó a", base * 1024, "¡felicitaciones has ganado el juego! :D\n")
                    play = False
                    _mainLoop()
                    return


def _mainLoop():
    from src.main import mainLoop
    mainLoop()