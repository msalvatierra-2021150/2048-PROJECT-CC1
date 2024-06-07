from .use_cases.single_player import single_player
from .shared.scoreboard_formatter import single_scoreboard_formatter
from .use_cases.multi_player import multi_player
from .shared.move import movements_reseter
from .shared.movements import score_reseter
from src.helpers.print_2048_instructions import print_2048_instructions

# Loop para mostrar el menú al usuario.
def mainLoop():
    while True:
        print("\n***************************************")
        print("     Bienvenido a este juego 2048      ")
        print("         Modalidades de juego:         ")
        print("1. Un jugador")
        print("2. Dos jugadores")
        print("3. Jugador vs máquina ")
        print("4. Ayuda ")
        print("5. Salir")

        modality = input("Ingrese la opción de juego (1-5): ")


        if modality in ["1", "2", "3"]:
            menu(modality)
            break
        elif modality == "4" or modality.lower() == "ayuda":
            print_2048_instructions()
        elif modality == "5" or modality.lower() == "salir":
            print("¡Adiós, gracias por jugar!")
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
        input("Presione enter para continuar: ")
        mainLoop()

    if modality == "2":
        multi_player(base, modality)
        input("Presione enter para continuar: ")
        mainLoop()