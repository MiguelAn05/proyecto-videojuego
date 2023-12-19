import os
import sys
import keyboard  # Importamos el módulo keyboard
from functools import reduce

def cadena_a_matriz(mapa_cadena):
    return list(map(list, mapa_cadena.strip().split('\n')))

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

        key = keyboard.read_key()  # Usamos keyboard.read_key() en lugar de msvcrt.getch()

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
