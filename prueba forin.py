import random
dimension = 10
posiciones_ocupadas = []
listanumerada_dimension = [0,1,2,3,4,5,6,7,8,9] 
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
    print(posiciones_ocupadas)
    for x in range (14):
        posiciones_ocupadas.pop(0)
    posiciones_britanicas = posiciones_ocupadas
    print(posiciones_britanicas)
    continuar = "no"

