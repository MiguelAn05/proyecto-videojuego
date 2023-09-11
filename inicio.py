nombre = input ("escribe tu nombre:")
print ("bienvenido", nombre)



import readchar
from readchar import readkey, key

while True:
  
 try:
  key = readchar.readkey()
  print(f"tecla presionada:{key}")
  if key == 'w':
   print("la tecla ↑ fue presionada")
   break
 except KeyboardInterrupt:
  break
 print("programa terminado")

  
   
