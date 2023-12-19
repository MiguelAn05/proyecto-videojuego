#proyecto integrador parte 1
nombre = input ("escribe tu nombre:")
print ("bienvenido", nombre)


#proyecto integrador parte 2
import readchar
from readchar import readkey, key
print("presiona cualquier tecla y w para salir del programa")
while True:
  
 try:
  key = readchar.readkey()
  print(f"tecla presionada:{key}")
  if key == 'w':
   print("la tecla w fue presionada")
   break
 except KeyboardInterrupt:
  break


#proyecto integrador parte 3
import os
import readchar
n=0
print("Presiona la tecla 'n' para aumentar el número")
while n < 50:
  try:
    key=readchar.readkey()
    if key == 'n':
     n+=1
     os.system('cls' if os.name=='nt' else 'clear')
     print(f"numero:{n}")
    else:
     break
  except KeyboardInterrupt:
   break






 
   



 
   
