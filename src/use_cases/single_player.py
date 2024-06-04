from ..shared.initialize_grid import initialize_grid
from ..shared.move import move
from ..shared.board_formatter import board_formatter

# Modalidad para un jugador
def single_player(base, nameUser):
    # Se genera el tablero y se imprime
    player_board = initialize_grid(base)
    board_formatter(player_board)
    # Se inicia un ciclo para pedir el moviento e imprimir el tablero
    play = True
    while play == True:
        direction = input("\nIngrese su movimento a, w, s, d: ")
        if direction and play == True:
            player_board = move(player_board, direction, base, nameUser)
            board_formatter(player_board)
            for i in range(4):
                if (base * 1024) in player_board[i]:
                    print("\nllego a", base * 1024, "felicitaciones has ganado el juego. :D\n")
                    play = False