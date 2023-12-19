import os
import random

class Juego:
    def __init__(self, mapa, inicio, fin):
        self.mapa = mapa
        self.inicio = inicio
        self.fin = fin

    # Aquí van tus métodos...

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        path_a_mapas = os.path.expanduser(path_a_mapas)  # Añade esta línea
        nombre_archivo = random.choice(os.listdir(path_a_mapas))
        path_completo = f"{path_a_mapas}/{nombre_archivo}"
        with open(path_completo, 'r') as archivo:
            lineas = archivo.readlines()
        mapa = ''.join(lineas[1:]).strip()  # Concatena todas las filas leídas del mapa
        try:
         mapa, inicio, fin = map(int, lineas[0].split())  # Extrae las dimensiones, inicio y fin
         super().__init__(mapa, inicio, fin)
        except ValueError:
            print("No se pudeo interpretar la linea")


    # Aquí van tus métodos...

def main():
    ruta = "~/Documents/pt-videojuego/"
    juego = JuegoArchivo(ruta)
    # Aquí ejecutas tu juego...

if __name__ == "__main__":
    main()
