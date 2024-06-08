from ..shared.move import movements_reseter
from ..shared.movements import score_reseter
from .single_player import single_player
from ..shared.scoreboard_formatter import scoreboard_formatter
import time

def player_vs_computer(base, modality):
    
    m_player_name = input("Ingresar nombre del jugador 1: ")
    m_machine_name = 'Oskers'

    #Turno del primer jugador
    score_reseter()
    print("Turno del jugador: ", m_player_name)
    data_p1 = single_player(base, m_player_name, modality)

    time.sleep(2)
    input("Presione 'Enter' para el turno de", m_machine_name)

    #Turno de la máquina
    score_reseter()
    print("Turno de la máquina: ", m_machine_name)
    m_machine_data = [] #Agregar funcionalidad de máquina. 

    scoreboard_formatter(m_player_name, data_p1, m_machine_name, m_machine_data, base)
    movements_reseter()

    return