import os
import sys
import msvcrt  # Importamos msvcrt para detectar las teclas presionadas en Windows

def cadena_a_matriz(mapa_cadena):
    # Dividir la cadena en líneas para obtener las filas
    filas = mapa_cadena.strip().split('\n')

    # Crear una matriz vacía para almacenar el laberinto
    laberinto = []

    for fila in filas:
        # Convertir cada fila en una lista de caracteres
        caracteres_fila = list(fila)
        laberinto.append(caracteres_fila)

    return laberinto

def limpiar_pantalla():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def mostrar_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=' ')
        print()

def main_loop(mapa, inicio, final):
    px, py = inicio  # Iniciar el jugador en la posición inicial

    while (px, py) != final:
        limpiar_pantalla()
        mapa[px][py] = 'P'
        mostrar_matriz(mapa)
        mapa[px][py] = '.'  # Restaurar el carácter anterior

        # Leer la tecla presionada
        key = msvcrt.getch().decode('utf-8')

        # Calcula la nueva posición tentativa
        nueva_px, nueva_py = px, py
        if key == 'w':
            nueva_px -= 1
        elif key == 's':
            nueva_px += 1
        elif key == 'a':
            nueva_py -= 1
        elif key == 'd':
            nueva_py += 1

        # Verificar si la nueva posición es válida
        if (
            0 <= nueva_px < len(mapa) and
            0 <= nueva_py < len(mapa[0]) and
            mapa[nueva_px][nueva_py] != '#'
        ):
            px, py = nueva_px, nueva_py

if __name__ == "__main__":
    mapa_cadena = """
    ######
    #S   #
    # ## #
    #   # #
    #   # #
    #   #E#
    ######
    """
    mapa = cadena_a_matriz(mapa_cadena)
    inicio = (1, 1)  # Coordenadas iniciales
    final = (len(mapa) - 2, len(mapa[0]) - 2)  # Coordenadas finales

    main_loop(mapa, inicio, final)