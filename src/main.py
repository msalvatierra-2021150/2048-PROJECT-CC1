from .use_cases.single_player import single_player

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
    if modality == "1":
        single_player()