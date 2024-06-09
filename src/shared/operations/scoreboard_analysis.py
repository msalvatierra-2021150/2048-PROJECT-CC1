def scoreboard_analysis(player1, player2, p1_boardmax_num, p2_boardmax_num, p1_score, p2_score, p1_max_moves, p2_max_moves, base):
    
    w1 = (f"{player1} es el ganador.")
    w2 = (f"{player2} es el ganador.")

    if p1_boardmax_num == int(base *1024) and not p2_boardmax_num == int(base *1024):
        print(w1)
    elif p2_boardmax_num == int(base *1024) and not p1_boardmax_num == int(base *1024):
        print(w2)
    else:
        if p1_boardmax_num > p2_boardmax_num:
            print (w1)
        elif p2_boardmax_num > p1_boardmax_num:
            print (w2)
        else:
            if p1_score > p2_score:
                print (w1)
            elif p2_score > p1_score:
                print (w2)
            else:
                if p1_max_moves < p2_max_moves:
                    print (w1)
                elif p2_max_moves < p1_max_moves:
                    print (w2)
                else:
                    print("Empate. ¡Bien jugado!")