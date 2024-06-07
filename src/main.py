from .use_cases.single_player import single_player
from .shared.scoreboard_formatter import single_scoreboard_formatter
from .use_cases.multi_player import multi_player
from .shared.move import movements_reseter
from .shared.movements import score_reseter

# Loop para mostrar el menú al usuario.
def mainLoop():
    while True:
        print("\n***************************************")
        print("     Bienvenido a este juego 2048      ")
        print("         Modalidades de juego:         ")
        print("1. Un jugador")
        print("2. Dos jugadores")
        print("3. Jugador vs máquina ")

        modality = input("Ingrese la opción de juego (1-3): ")


        if modality in ["1", "2", "3"]:
            print("\nDe acuerdo.")
            menu(modality)
            break
        else:
            print("\nPor favor ingrese una opción válida.")

# Procedimiento para el modo del juego

def menu(modality):
    base = int(input("ingrese la base del juego, por ejemplo 2 o 3 para 2048 o 3072 respectivamente: "))
    if modality == "1":

        movements_reseter()
        score_reseter()
        nameUser = input("Ingrese su nombre: ")
        single_data = single_player(base, nameUser, modality)
        single_scoreboard_formatter(single_data)
        enter = input("Presione enter para continuar: ")
        mainLoop()

    if modality == "2":
        multi_player(base, modality)
        enter = input("Presione enter para continuar: ")
        mainLoop()