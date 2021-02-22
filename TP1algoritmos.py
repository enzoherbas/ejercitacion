print("=================================================\nBIENVENIDO AL TP DE ENZO\n=================================================")
tablero_insuficiente = "si"
while tablero_insuficiente == "si" :
    dimension = int(input("Vamos a crear el tablero de juego. Ingrese el numero (debe estar entre 10 y 24) de dimension que desea para el tablero: "))
    if dimension < 10 or dimension > 24: 
        print("*************************\nEl tablero debe estar entre 10 y 24, vuelva a ingresar el valor.\n*************************")
    elif dimension >= 10 and dimension <= 24:
        tablero_insuficiente = "no"
personaje_invalido = "si"
while personaje_invalido == "si":
    personaje = input("Elija que personaje desea.\n1 ) Sandokan y sus valientes amigos.\n2 ) Armada britanica\nIngrese el valor 1 o 2 para elegir a su personaje: ")
    if personaje == "1" or personaje ==  "2" :
        personaje_invalido = "no"
    else:
        print("*************************\nDebe ingresar 1 o 2, para ser Sandokan o la Armada britanica. Ingrese nuevamente su opcion.\n*************************")
tablero  = []
fila =[]
#TABLERO EN BLANCO
for x_tablero in range (0,dimension):
    fila =[]
    for y_tablero in range (0,dimension):
        fila.append(0)
    tablero.append(fila)
for x in range (dimension):
    print(tablero[x])
    #import string
#abecedario=list(string.ascii_lowercase)
#print(abecedario)

lista = [[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]]
import random
continuar = "no"
while continuar != "si":
    numerorandom = random.choice(lista)
    filarandom = random.choice(numerorandom)
    columnarandom = random.choice(numerorandom)
    barco6 = []
    continuar = "si"
    if filarandom <= 4 :
        continuar = "si"
        tope = filarandom + 6
        
        for x in range (filarandom, tope ):
            posicion_barco6 = [columnarandom, x]
            barco6.append(posicion_barco6)
            posicion_barco6 = []
        print(barco6)
    else:
        continuar = "no"
        