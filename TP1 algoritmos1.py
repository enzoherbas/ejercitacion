print("=================================================\nBIENVENIDO AL TP DE ENZO\n=================================================")
import string
import random

abecedario=list(string.ascii_uppercase)
tablero  = []
fila =[]
borde_superior= []
posiciones_ocupadas = []
listanumerada_dimension = []

tablero_insuficiente = "si"
while tablero_insuficiente == "si" :
    dimension = int(input("Vamos a crear el tablero de juego. Ingrese el numero (debe estar entre 10 y 24) de dimension que desea para el tablero: "))
    if dimension < 10 or dimension > 24: 
        print("*************************\nEl tablero debe estar entre 10 y 24, vuelva a ingresar el valor.\n*************************")
    elif dimension >= 10 and dimension <= 24:
        tablero_insuficiente = "no"

personaje_invalido = "si"
while personaje_invalido == "si":
    personaje = input("Elija que personaje desea.\n1 ) Sandokan y sus valientes amigos.\n2 ) Armada britanica.\nIngrese el valor 1 o 2 para elegir a su personaje: ")
    if personaje == "1" or personaje ==  "2" :
       personaje_invalido = "no"
    else:
        print("*************************\nDebe ingresar 1 o 2, para ser Sandokan o la Armada britanica. Ingrese nuevamente su opcion.\n*************************")
#TABLERO EN BLANCO CON BORDES NUMERADOS
for x_bordesuperior in range(1,dimension+1):
    borde_superior.append(x_bordesuperior)
print(" ",borde_superior)
for y in range(dimension):
    listanumerada_dimension.append(y)


for x_tablero in range (dimension):
    fila =[]
    for y_tablero in range (dimension):
        fila.append(0)
    tablero.append(fila)
for x in range (dimension):
    print(abecedario[x],tablero[x])


#BARCO 6 SANDOKAN

continuar = "si"
while continuar == "si":
    barco6 = []
    filarandom = random.choice(listanumerada_dimension)
    columnarandom = random.choice(listanumerada_dimension)
    barco_sandokan_6_horizontal = []
    limite_columna_bs6 = dimension - 6
    if columnarandom <= limite_columna_bs6 :
        tope = columnarandom + 6
        for x in range (columnarandom, tope ):
            posicion_barco6 = [filarandom, x ]
            barco6.append(posicion_barco6)
            posicion_barco6 = []
        posiciones_ocupadas = barco6    
        continuar = "no"
    else:
        continuar = "si"

#BARCO 3 VERTICAL SANDOKAN

continuar = "si"
while continuar == "si":
    filarandom = random.choice(listanumerada_dimension)
    columnarandom = random.choice(listanumerada_dimension)
    limite_fila_bs6 = dimension - 3
    posicion_barco3v = []
    if filarandom <= limite_fila_bs6 :
        tope = filarandom + 3
        for x in range (filarandom, tope ):
            posicion_barco3 = [x, columnarandom ]
            posicion_barco3v.append(posicion_barco3)
        contador = 0
        for x in range(0,3):
                if posicion_barco3v[x] in posiciones_ocupadas:
                    contador += 1
        if contador == 0 :
                    for x in range(3):
                            continuar = "no"
                            posiciones_ocupadas.append(posicion_barco3v[x])
                    barco3_vertical = posicion_barco3v            
    else:
        continuar = "si"
#BARCO 2 HORIZONTAL SANDOKAN
        
continuar = "si"
while continuar == "si":
    filarandom = random.choice(listanumerada_dimension)
    columnarandom = random.choice(listanumerada_dimension)
    limite_columna_bs2h = dimension - 2
    posicion_barco2h = []
    if columnarandom <= limite_columna_bs2h :
        tope = columnarandom + 2
        for x in range (columnarandom, tope ):
            posicion_barco2hm = [filarandom, x ]
            posicion_barco2h.append(posicion_barco2hm)
        contador = 0
        for x in range(0,2):
                if posicion_barco2h[x] in posiciones_ocupadas:
                    contador += 1
        if contador == 0 :
                    for x in range(2):
                            continuar = "no"
                            posiciones_ocupadas.append(posicion_barco2h[x])
                    barco2h = posicion_barco2h         
    else:
        continuar = "si"
#BARCO 2 VERTICAL
        
continuar = "si"
while continuar == "si":
    filarandom = random.choice(listanumerada_dimension)
    columnarandom = random.choice(listanumerada_dimension)
    limite_fila_bs2v = dimension - 2
    posicion_barco2v = []
    if filarandom <= limite_fila_bs2v :
        tope = filarandom + 2
        for x in range (filarandom, tope ):
            posicion_barco2 = [x, columnarandom ]
            posicion_barco2v.append(posicion_barco2)
        contador = 0
        for x in range(0,2):
                if posicion_barco2v[x] in posiciones_ocupadas:
                    contador += 1
        if contador == 0 :
                    for x in range(2):
                            continuar = "no"
                            posiciones_ocupadas.append(posicion_barco2v[x])
                    barco2_vertical = posicion_barco2v            
    else:
        continuar = "si"

#BARCO 1 CASILLERO
continuar = "si"
while continuar == "si":
    filarandom = random.choice(listanumerada_dimension)
    columnarandom = random.choice(listanumerada_dimension)
    barco_1casillero = [filarandom,columnarandom]
    contador = 0
    if barco_1casillero not in posiciones_ocupadas:
        continuar = "no"
        posiciones_ocupadas.append(barco_1casillero)
        barco1 = barco_1casillero
        print(posiciones_ocupadas)
    else: 
        continuar = "si"
#ELIMINACION DE PUNTOS
coordenada_letra = input("Ingrese la coordenada de ataque.\nLetra de la coordenada donde desea atacar(en mayuscula): ")
coordenada_numero = int(input("Ingrese el numero de la coordenada: "))
for contador_objetivo in range (len(abecedario)):
    if abecedario[contador_objetivo] == coordenada_letra:
        coordenada_letra_numero = abecedario[contador_objetivo]
