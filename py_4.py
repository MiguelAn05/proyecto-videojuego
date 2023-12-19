import os
import sys
import msvcrt  

def cadena_a_matriz(mapa_cadena):
    filas = mapa_cadena.strip().split('\n')

    laberinto = []

    for fila in filas:
        caracteres_fila = list(fila)
        laberinto.append(caracteres_fila)
    return laberinto


def limpiar_pantalla():
        os.system('cls')


def mostrar_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=' ')
        print()


def main_loop(mapa, inicio, final):
    px, py = inicio 

    while (px, py) != final:
        limpiar_pantalla()
        mapa[px][py] = 'P'
        mostrar_matriz(mapa)
        mapa[px][py] = '.'  

        key = msvcrt.getch().decode('utf-8')

        nueva_px, nueva_py = px, py
        if key == 'w':
            nueva_px -= 1
        elif key == 's':
            nueva_px += 1
        elif key == 'a':
            nueva_py -= 1
        elif key == 'd':
            nueva_py += 1


        if (
            0 <= nueva_px < len(mapa) and
            0 <= nueva_py < len(mapa[0]) and
            mapa[nueva_px][nueva_py] != '#'
        ):
            px, py = nueva_px, nueva_py
mensaje = input("presiona las teclas w,s,a,d para moverte por el mapa, presiona ENTER para empezar")

if __name__ == "__main__":
    mapa_cadena =  """

#.#########
..........#
#.#####.#.#
#.#.....#.#
###.#####.#
#...#.....#
#######.#.#
#.....#.#.#
#.###.#.#.#
#.#.....#.#
#########.#

"""

    mapa = cadena_a_matriz(mapa_cadena)
    inicio = (0, 1) 
    final = (len(mapa) -1, len(mapa[0]) - 2) 

    main_loop(mapa, inicio, final)
   