from .single_player import single_player
from ..shared.results.scoreboard_formatter import scoreboard_formatter
from ..shared.move.movements import score_reseter
from ..shared.move.move import movements_reseter
import time


def multi_player(base, modality):
    #nombres
    p1_name = input("\nIngresar nombre del jugador 1: ")
    p2_name = input("Ingresar nombre del jugador 2: ")

    #primer jugador
    score_reseter()
    print("\n\nTurno del jugador:", p1_name)
    data_p1 = single_player(base, p1_name, modality)
    print(f"{p1_name} ha terminado de jugar.")

    time.sleep(2)
    input("presione 'Enter' para siguiente jugador...")


    #segundo jugador
    movements_reseter()
    score_reseter()
    print("\n\nTurno del jugador: ", p2_name)
    data_p2 = single_player(base, p2_name, modality)
    print("¡El juego ha terminado!")
    
    
    time.sleep(2)

    scoreboard_formatter(p1_name, data_p1, p2_name, data_p2, base)
    time.sleep(2)
    movements_reseter()
