import random #importamos la librería random
import time   #para utilizar delay
#CODIGO DE COLORES
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
puntaje=random.randint(0,10) #variable para contabilizar el puntaje
#rango de 5-10 para preguntas correctas
#-rango de 1-5 por pregunta incorrecta
iniciar_trivia=True
intentos=0 #variable para almacenar el número de veces que se realiza la trivia
validacion_numero=True #variable para validación numérica de num_usuario de la P1
bandera=True #variable para validación numérica de num_usuario de P3

print (BLUE+"Bienvenido a mi trivia sobre robótica"+RESET)
print (BLUE+"Pondremos a prueba tus conocimientos"+RESET)
print (CYAN+"Comenzarás con ", puntaje, "puntos."+RESET)
time.sleep(1)
nombre=input(BLUE+"Ingrese su nombre: "+RESET)
nombre=nombre.upper()

# Es importante dar instrucciones sobre cómo jugar:
print (BLUE+"\n"+nombre, "Debes responder las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"+RESET)
time.sleep(1)

print("Comenzamos en:")
for numero_carga in range(5, 0, -1):
  print(numero_carga, "...")
  time.sleep(1)

#LISTA PARA ALMACENAR PUNTAJE:
lista_puntaje=[]
lista_puntaje.append(puntaje) #asignamos el valor de puntaje a la lista


#LISTAS DE ALTERNATIVAS DE PREGUNTAS:
lista1=[YELLOW+"a) Método Geométrico", "b) Método Algebráico", "c) Método Numérico", "d) Método Desacoplo cinemático"+RESET]
lista2=[YELLOW+"a) Matrices de rotación", "b) Cuaternios", "c) Par rotacional", "d) Matrices de transformación homogénea"+RESET]
lista3=[YELLOW+"a) Jacobiano de velocidades", "b) Métodos iterativos", "c) Singularidades", "d)Jacobiano de aceleraciones"+RESET]
lista4=[YELLOW+"a) Robot caminante", "b) Robot terrestre", "c) Robot paralelo", "d) Robot aéreo"+RESET]

  
#INICIAR TRIVIA
while iniciar_trivia==True:
  intentos+=1
  print(BLUE+"\nIntento número:", intentos, "."+RESET)
  # Pregunta 1
  print (MAGENTA+"\n1) ¿Qué método para calcular la cinemática inversa no es un método de Solución Cerrada?\n"+RESET)
  for i in lista1:  #imprimimos claves de la P1
    print(i)
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nIndique su respuesta: ")
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingrese nuevamente su respuesta: ")
  time.sleep(1)
  if respuesta_1=="a":
    print(RED+"\nTu respuesta es incorrecta ", nombre, ". ¡El método geométrico es un método de Solución Cerrada para hallar la cinemática inversa."+RESET)
    puntaje=-random.randint(1,5)
    lista_puntaje.append(puntaje)
    puntaje=sum(lista_puntaje)
    print("Puntaje actual:", puntaje, "puntos!\n")
  elif respuesta_1=="b":
    print(RED+"\nTu respuesta es incorrecta ", nombre, ". ¡El método algebráico es un método de Solución Cerrada para hallar la cinemática inversa."+RESET)
    puntaje=-random.randint(1,5)
    lista_puntaje.append(puntaje)
    puntaje=sum(lista_puntaje)
    print("Puntaje actual:", puntaje, "puntos!\n")
  elif respuesta_1=="d":
    print(RED+"\nTu respuesta es incorrecta ", nombre, ". ¡El método de desacoplo cinemático es un método de Solución Cerrada para hallar la cinemática inversa."+RESET)
    puntaje-=random.randint(1,5)
    print("Puntaje actual:", puntaje, "puntos!\n")
  else:
    print(GREEN+"\nTu respuesta es correcta ", nombre, "!"+RESET)
    num_usuario=input("Ingrese un número: ")
    validacion_numero=True #asignamos true nuevamente para cada vez que se realiza el bucle no haya errores
    while validacion_numero==True:
      if num_usuario.isnumeric():
        num_usuario=int(num_usuario)
        lista_puntaje.append(num_usuario)
        puntaje=sum(lista_puntaje)
        print("Puntaje actual:", puntaje, "puntos!\n")
        validacion_numero=False
      else:
        num_usuario=input("Por favor, ingrese un tipo de dato numérico: ")
  time.sleep(2)
  
  # Pregunta 2
  print (MAGENTA+"2) ¿Qué método se puede aplicar para definir la posición y orientación de un robot?\n"+RESET)
  for i in lista2:  #imprimimos claves de la P2
    print(i)  
  respuesta_2 = input("\nIndique su respuesta: ")
  while respuesta_2 not in ("a", "b", "c", "d", "x"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingrese nuevamente su respuesta: ")
  time.sleep(1)
  if respuesta_2=="a":
    print(RED+"\nTu respuesta es incorrecta ", nombre, ". ¡Las matrices de rotación se utilizan para hallar la orientación del robot."+RESET)
    puntaje=-random.randint(1,5)
    lista_puntaje.append(puntaje)
    puntaje=sum(lista_puntaje)
    print("Puntaje actual:", puntaje, "puntos!\n")
  elif respuesta_2=="b":
    print(RED+"\nTu respuesta es incorrecta ", nombre, ". ¡Los cuaternios se utilizan para hallar la orientación del robot."+RESET)
    puntaje=-random.randint(1,5)
    lista_puntaje.append(puntaje)
    puntaje=sum(lista_puntaje)
    print("Puntaje actual:", puntaje, "puntos!\n")
  elif respuesta_2=="c":
    print(RED+"\nTu respuesta es incorrecta ", nombre, ". ¡El par rotacional se utiliza para hallar la orientación del robot."+RESET)
    puntaje=-random.randint(1,5)
    lista_puntaje.append(puntaje)
    puntaje=sum(lista_puntaje)
    print("Puntaje actual:", puntaje, "puntos!\n")
  elif respuesta_2=="x":
    print("\nEste es un mensaje secreto ", nombre, "! Obtuviste 100 puntos por descubrirlo.")  
    lista_puntaje.append(100)
    puntaje=sum(lista_puntaje)
    print("Puntaje actual:", puntaje, "puntos!\n")
  else:
    print(GREEN+"\nTu respuesta es correcta ", nombre, "!"+RESET)
    puntaje=random.randint(1,5)
    lista_puntaje.append(puntaje)
    puntaje=sum(lista_puntaje)
    print("Puntaje actual:", puntaje, "puntos!\n")
  time.sleep(2)
  
  # Pregunta 3
  print (MAGENTA+"3) ¿Qué método no se aplica para la cinemática diferencial del robot?\n"+RESET)
  for i in lista3:  #imprimimos claves de la P3
    print(i)  
  respuesta_3 = input("\nIndique su respuesta: ")
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingrese nuevamente su respuesta: ")
  time.sleep(1)
  if respuesta_3=="a":
    print(RED+"\nTu respuesta es incorrecta ", nombre, ". ¡El jacobiano de velocidades se utiliza para la cinemática diferencial del robot."+RESET)
    num2_usuario=input("Ingrese un número: ")
    bandera=True
    while bandera==True:
      if num2_usuario.isnumeric():
        num2_usuario=-int(num2_usuario)
        lista_puntaje.append(num2_usuario)
        puntaje=sum(lista_puntaje)
        print("Puntaje actual:", puntaje, "puntos!\n")
        bandera=False
      else:
        num2_usuario=input("Por favor, ingrese un tipo de dato numérico: ")
  elif respuesta_3=="c":
    print(RED+"\nTu respuesta es incorrecta ", nombre, ". ¡Las singularidades se utilizan para la cinemática diferencial del robot."+RESET)
    num2_usuario=input("Ingrese un número: ")
    bandera=True
    while bandera==True:
      if num2_usuario.isnumeric():
        num2_usuario=-int(num2_usuario)
        lista_puntaje.append(num2_usuario)
        puntaje=sum(lista_puntaje)
        print("Puntaje actual:", puntaje, "puntos!\n")
        bandera=False
      else:
        num2_usuario=input("Por favor, ingrese un tipo de dato numérico: ")
  elif respuesta_3=="d":
    print(RED+"\nTu respuesta es incorrecta ", nombre, ". ¡El jacobiano de aceleraciones se utiliza para la cinemática diferencial del robot."+RESET)
    num2_usuario=input("Ingrese un número: ")
    bandera=True
    while bandera==True:
      if num2_usuario.isnumeric():
        num2_usuario=-int(num2_usuario)
        lista_puntaje.append(num2_usuario)
        puntaje=sum(lista_puntaje)
        print("Puntaje actual:", puntaje, "puntos!\n")
        bandera=False
      else:
        num2_usuario=input("Por favor, ingrese un tipo de dato numérico: ")
  else:
    print(GREEN+"\nTu respuesta es correcta ", nombre, "!"+RESET)
    puntaje=random.randint(1,5)
    lista_puntaje.append(puntaje)
    puntaje=sum(lista_puntaje)
    print("Puntaje actual:", puntaje, "puntos!\n")
  time.sleep(2)
  
  #PREGUNTA 4 - PREGUNTA CON EFECTOS ESPECIALES EN EL PUNTAJE
  # Pregunta 4
  print (MAGENTA+"4) ¿Qué tipo de robot es un ROBOT HEXAPODO según su aplicación?\n"+RESET)
  for i in lista4:  #imprimimos claves de la P4
    print(i)  
  respuesta_4 = input("\nIndique su respuesta: ")
  while respuesta_4 not in ("a", "b", "c", "d"):
    respuesta_4 = input("Debes responder a, b, c o d. Ingrese nuevamente su respuesta: ")
  time.sleep(1)
  if respuesta_4=="a":
    print(GREEN+"\nCorrecto...! ", nombre+RESET)
    puntaje*=2
    lista_puntaje.clear()
    lista_puntaje.append(puntaje)
    print(GREEN+"\nGracias", nombre, "por participar de la trivia, obtuviste", puntaje, "puntos"+RESET)
  elif respuesta_4=="b":
    print("\n... ")
    puntaje+=5
    lista_puntaje.clear()
    lista_puntaje.append(puntaje)
    print(GREEN+"\nGracias", nombre, "por participar de la trivia, obtuviste", puntaje, "puntos"+RESET)
  elif respuesta_4=="c":
    print(RED+"\nTu respuesta es incorrecta...", nombre+RESET)
    puntaje-=5
    lista_puntaje.clear()
    lista_puntaje.append(puntaje)
    print(GREEN+"\nGracias", nombre, "por participar de la trivia, obtuviste", puntaje, "puntos"+RESET)
  else:
    print(RED+"\nTotalmente incorrecto...!!", nombre, "!"+RESET)
    puntaje/=2
    lista_puntaje.clear()
    lista_puntaje.append(puntaje)
    print(GREEN+"\nGracias", nombre, "por participar de la trivia, obtuviste", puntaje, "puntos"+RESET)
  time.sleep(2)
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":  # != significa "diferente"
   print("\nEspero", nombre, "que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False  # Cambiamos el valor a False para terminar el bucle
  time.sleep(2)

