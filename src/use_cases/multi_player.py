from .single_player import single_player
from ..shared.scoreboard_formatter import scoreboard_formatter
from ..shared.movements import score_reseter
from ..shared.move import movements_reseter


def multi_player(base, modality):
    #nombres
    p1_name = input("Ingresar nombre del jugador 1: ")
    p2_name = input("Ingresar nombre del jugador 2: ")

    #primer jugador
    score_reseter()
    print("Turno del jugador: ", p1_name)
    data_p1 = single_player(base, p1_name, modality)


    #segundo jugador
    score_reseter()
    print("Turno del jugador: ", p2_name)
    data_p2 = single_player(base, p2_name, modality)

    scoreboard_formatter(p1_name, data_p1, p2_name, data_p2, base)
    movements_reseter()
