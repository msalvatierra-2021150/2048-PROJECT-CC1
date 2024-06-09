from .use_cases.single_player import single_player
from .shared.results.scoreboard_formatter import single_scoreboard_formatter
from .use_cases.multi_player import multi_player
from .shared.move.move import movements_reseter
from .shared.move.movements import score_reseter
from src.helpers.print_2048_instructions import print_2048_instructions
from .use_cases.player_vs_machine import player_vs_machine
import time

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

        modality = input("\nIngrese la opción de juego (1-5): ")


        if modality in ["1", "2", "3"]:
            menu(modality)
            break
        elif modality == "4" or modality.lower() == "ayuda":
            print_2048_instructions()
        elif modality == "5" or modality.lower() == "salir":
            print("¡Adiós! Gracias por jugar!\n")
            break
        else:
            print("\nPor favor ingrese una opción válida.")

# Procedimiento para el modo del juego

def menu(modality):
    try:
        base = int(input("Ingrese la base del juego, por ejemplo 2 o 3 para 2048 o 3072 respectivamente: "))
        print("Cargando...")
        time.sleep(2)

        if modality == "1":
            movements_reseter()
            score_reseter()
            nameUser = input("\nIngrese su nombre: ")
            single_data = single_player(base, nameUser, modality)
            
            print("¡El juego ha terminado!")
            time.sleep(2)
            single_scoreboard_formatter(single_data)
            time.sleep(2)
            input("Presione 'ENTER' para continuar...")
            mainLoop()


        if modality == "2":
            multi_player(base, modality)
            input("Presione 'ENTER' para continuar...")
            mainLoop()

        if modality == "3":
            player_vs_machine(base, modality)
            input("Presione 'ENTER' para continuar...")
            mainLoop()
        
    except ValueError:
        print("\nNúmero ingresado inválido, por favor ingresa un número válido.\n")
        return menu(modality)