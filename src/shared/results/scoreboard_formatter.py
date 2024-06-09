from ..operations.scoreboard_analysis import scoreboard_analysis


def single_scoreboard_formatter(single_data):
    print("---------------------------------------")
    print("|          SCORE BOARD                 ")
    print("|----------------------------|")
    print(f"| Maximo puntaje en tabla    | {single_data[1]}")
    print(f"| Puntaje Acumulado          | {single_data[0]}")
    print(f"| Cantidad de movimiento     | {single_data[2]}")
    print("---------------------------------------")

    
        


def scoreboard_formatter (p1_name, data_p1, p2_name, data_p2, base):

    #Datos del primer jugador
    p1_max_board_num = int(data_p1[1])
    p1_max_score = int(data_p1[0])
    p1_max_moves = int(data_p1[2])

    #Datos del segundo jugador
    p2_max_board_num = int (data_p2[1])
    p2_max_score = int(data_p2[0])
    p2_max_moves = int(data_p2[2])


    print("---------------------------------------------------")
    print("|                   SCORE BOARD                   |")
    print("|-------------------------------------------------|")
    print(f"|                            | {p1_name} | {p2_name} ")
    print(f"| Maximo puntaje en tabla    | {p1_max_board_num} | {p2_max_board_num} ")
    print(f"| Puntaje Acumulado          | {p1_max_score} | {p2_max_score} ")
    print(f"| Cantidad de movimiento     | {p1_max_moves} | {p2_max_moves} ")
    print("---------------------------------------------------")

    scoreboard_analysis(p1_name, p2_name, p1_max_board_num, p2_max_board_num, p1_max_score, p2_max_score, p1_max_moves, p2_max_moves, base)

