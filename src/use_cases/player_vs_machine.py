from ..shared.move.move import movements_reseter
from ..shared.move.movements import score_reseter
from .single_player import single_player
from ..shared.results.scoreboard_formatter import scoreboard_formatter
from .machine import machine
import time

def player_vs_machine(base, modality):
    m_player_name = input("Ingresar nombre del jugador: ")

    #Turno del primer jugador
    score_reseter()
    print("Turno del jugador: ", m_player_name)
    data_p1 = single_player(base, m_player_name, modality)

    time.sleep(2)
    input(f"Presione 'Enter' para el turno de la máquina")

    #Turno de la máquina
    score_reseter()
    print("Turno de la máquina")
    m_machine_data = machine(base, nameUser="Máquina", modality= modality) #Agregar funcionalidad de máquina. 

    scoreboard_formatter(m_player_name, data_p1, "Máquina", m_machine_data, base)
    movements_reseter()

    return