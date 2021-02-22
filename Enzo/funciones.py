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
## DEFINO LA FUNCION PARA GENERAR POSICIONES DE LOS BARCOS HORIZONTALES
def barcohorizontal (celdas):
        continuar = "si"
        while continuar == "si":
            filarandom = random.choice(listanumerada_dimension)
            columnarandom = random.choice(listanumerada_dimension)
            posicion_parcial = []
            limite = dimension - celdas
            if columnarandom <= limite :
                tope = columnarandom + celdas
                for x in range (columnarandom, tope ):
                    posicion_barco = [filarandom, x ]
                    posicion_parcial.append(posicion_barco)
                    contador = 0
                for x in range(celdas):
                            if posicion_parcial[x] in posiciones_ocupadas:
                                contador += 1
                                print("caca1")
                if contador == 0 :
                    for x in range(celdas):
                            posiciones_ocupadas.append(posicion_parcial[x])
                            continuar = "no"
        else:
                continuar = "si"
                
## DEFINO LA FUNCION PARA GENERAR POSICIONES DE LOS BARCOS VERTICALES
def barcovertical (celdas):
        continuar = "si"
        while continuar == "si":
            filarandom = random.choice(listanumerada_dimension)
            columnarandom = random.choice(listanumerada_dimension)
            posicion_parcial = []
            limite = dimension - celdas
            if filarandom <= limite :
                tope = filarandom + celdas
                for x in range (filarandom, tope ):
                    posicion_barco = [x, columnarandom]
                    posicion_parcial.append(posicion_barco)
                    contador = 0
                for x in range(celdas):
                            if posicion_parcial[x] in posiciones_ocupadas:
                                contador += 1
                                print("caca2")
                if contador == 0 :
                    for x in range(celdas):
                            posiciones_ocupadas.append(posicion_parcial[x])
                            continuar = "no"
        else:
                continuar = "si"

#GENERO, JUNTO CON LAS FUNCIONES PREVIAMENTE HECHAS, LAS POSICIONES DE LOS BARCOS DE SANDOKAN Y LA ARMADA BRITANICA
continuar = "si"
while continuar == "si":
    #BARCOS DE SANDOKAN
    celdas_horizontales = [6,2,1]
    celdas_verticales = [3,2]
    for celdas in celdas_horizontales:
        barcohorizontal (celdas)
    for celdas in celdas_verticales:
        barcovertical (celdas)
    posiciones_sandokan = posiciones_ocupadas
    print(posiciones_sandokan)
    #BARCOS DE LA ARMADA BRITANICA
    celdas_verticales = [6,2,1]
    celdas_horizontales = [3,2]
    for celdas in celdas_horizontales:
        barcohorizontal (celdas)
    for celdas in celdas_verticales:
        barcovertical (celdas)
    posiciones_ocupadas_totales = posiciones_ocupadas
    for x in range (14):
        posiciones_ocupadas.pop(0)
    posiciones_britanicas = posiciones_ocupadas
    print(posiciones_britanicas)
    continuar = "no"


#ELIMINACION DE PUNTOS
coordenada_letra = input("Ingrese la coordenada de ataque.\nLetra de la coordenada donde desea atacar(en mayuscula): ")
coordenada_numero = int(input("Ingrese el numero de la coordenada: "))
for contador_objetivo in range (len(abecedario)):
    if abecedario[contador_objetivo] == coordenada_letra:
        coordenada_letra_numero = abecedario[contador_objetivo]