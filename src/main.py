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
        nameUser = input("ingrese su nombre: ")
        base = int(input("ingrese la base del juego, por ejemplo 2 o 3 para 2048 o 3072 respectivamente: "))

        if modality in ["1", "2", "3"]:
            print("\nDe acuerdo.")
            menu(modality, base, nameUser)
            break
        else:
            print("\nPor favor ingrese una opción válida.")

# Procedimiento para el modo del juego
def menu(modality, base, nameUser):
    if modality == "1":
        single_player(base, nameUser)