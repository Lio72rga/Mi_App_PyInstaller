tablero = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]
def inicializar_tablero():
    return [["" for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    for fila in tablero:
        print("|".join([elemento if elemento != "" else " " for elemento in fila]))
        print("-" * 5)

def hay_ganador(tablero, jugador):
    # Comprobar filas
    for fila in tablero:
        if all(elemento == jugador for elemento in fila):
            return True

    # Comprobar columnas
    for col in range(3):
        if all(tablero[fila][col] == jugador for fila in range(3)):
            return True

    # Comprobar diagonales
    if all(tablero[i][i] == jugador for i in range(3)):
        return True
    if all(tablero[i][2 - i] == jugador for i in range(3)):
        return True

    return False

def tablero_lleno(tablero):
    return all(elemento != "" for fila in tablero for elemento in fila)

def solicitar_entrada(jugador):
    while True:
        try:
            fila, col = map(int, input(f"Jugador {jugador}, ingrese fila y columna (0, 1 o 2) separadas por espacio: ").split())
            if fila in range(3) and col in range(3):
                return fila, col
            else:
                print("Entrada no válida, ingrese números entre 0 y 2.")
        except ValueError:
            print("Entrada no válida, ingrese dos números.")

def jugar_ta_te_ti():
    tablero = inicializar_tablero()
    jugadores = ["X", "O"]
    turno = 0

    while True:
        mostrar_tablero(tablero)
        jugador_actual = jugadores[turno]

        while True:
            fila, col = solicitar_entrada(jugador_actual)
            if tablero[fila][col] == "":
                tablero[fila][col] = jugador_actual
                break
            else:
                print("Posición ocupada, elija otra.")

        if hay_ganador(tablero, jugador_actual):
            mostrar_tablero(tablero)
            print(f"¡Jugador {jugador_actual} gana!")
            break

        if tablero_lleno(tablero):
            mostrar_tablero(tablero)
            print("¡Empate!")
            break

        turno = 1 - turno

    if input("¿Quieres jugar otra vez? (s/n): ").lower() == "s":
        jugar_ta_te_ti()

# Iniciar el juego
jugar_ta_te_ti()