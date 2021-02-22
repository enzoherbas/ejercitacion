import random

continuar = "si"
while continuar == "si":
    celdas_barcos = [6,3,2,1]
    filarandom = random.choice(listanumerada_dimension)
    columnarandom = random.choice(listanumerada_dimension)
    for celdas in celdas_barcos:
        barco_sandokan_6_horizontal = []
        limite_columna_bs6 = dimension - 6
        if columnarandom <= limite_columna_bs6 :
            tope = columnarandom + 6
            for x in range (columnarandom, tope ):
                posicion_barco6 = [filarandom, x ]
                barco6.append(posicion_barco6)
                posicion_barco6 = []
            posiciones_ocupadas = barco6
            for x in range(0,3):
                    if posicion_barco3v[x] in posiciones_ocupadas:
                        contador += 1
            if contador == 0 :
                        for x in range(3):
                                continuar = "no"
                                posiciones_ocupadas.append(posicion_barco3v[x])
                        barco3_vertical = posicion_barco3v 
            continuar = "no"
    else:
            continuar = "si"
