import random
def dimension_tablero():
    continuar_tablero = "Si"
    while continuar_tablero == "Si":
        dimension = int(input("Ingrese la dimension de los tableros de juego(Debe estar entre 10 y 24): "))
        if dimension > 24 or dimension < 10:
            print("Ingresaste una opcion no valida.")
        else:
            continuar_tablero = "No"
    return dimension
def borde_superior(dimension):
    borde_superior = []
    for x_bordesuperior in range(1,dimension+1):
        if x_bordesuperior < 11:
            borde_superior.append(str(x_bordesuperior))
        else:
            par = x_bordesuperior % 2
            if par == 0:
                borde_superior.append(str(x_bordesuperior))
            else:
                borde_superior.append(x_bordesuperior)
    return borde_superior
def borde_lateral(dimension):
    borde_lateral = imprimir_tablero_comienzo(dimension)
def creacion_tableros(dimension):
    tablero = []
    for x_tablero in range (dimension):
        fila =[]
        for y_tablero in range (dimension):
            fila.append("-")
        tablero.append(fila)
    return tablero
def abecedario_tablero (dimension):
    abecedario = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    abecedario_tablero = []
    for x in range (dimension):
        abecedario_tablero.append(abecedario[x])
    return abecedario_tablero
def imprimir_tablero(dimension,tablero):
    print(" ",borde_superior(dimension))
    borde_lateral = abecedario_tablero(dimension)
    for x in range (dimension):
       print(borde_lateral[x],tablero[x])
def jugadores ():
    jugadores_listo = "No"
    while jugadores_listo == "No":
        elegir_personaje = int(input("Jugador 1 que personaje desea.\n1 ) Sandokan y sus valientes amigos.\n2 ) Armada britanica.\nIngrese el valor 1 o 2 para elegir a su personaje:"))
        if elegir_personaje == 1:
            print("*********************************************************\nEl jugador 1, sera SANDOKAN Y SUS VALIENTES AMIGOS.\nEl jugador 2, sera LA ARMADA BRITANICA.\n*********************************************************")
            jugadores_listo = "Si"
            return elegir_personaje
        elif elegir_personaje == 2:
            print("*********************************************************\nEl jugador 1, sera LA ARMADA BRITANICA.\nEl jugador 2, sera SANDOKAN Y SUS VALIENTES AMIGOS\n*********************************************************")
            jugadores_listo= "Si"
            return elegir_personaje
        else:
            print("*************************\nDebe ingresar 1 o 2, para ser Sandokan o la Armada britanica. Ingrese nuevamente su opcion.\n*************************")
    return elegir_personaje
def generar_barcos_sandokan (dimension):
    posiciones_ocupadas = []
    barcos_listados_sandokan = []
    for celdas in celdas_horizontales_sandokan():
        continuar = "si"
        while continuar == "si":
            posicion_generada = generador_barcos_horizontales(celdas,dimension)
            contador = 0
            for x in range(celdas):
                        if posicion_generada[x] in posiciones_ocupadas:
                           contador += 1
            if contador == 0 :
                    for x in posicion_generada:
                        posiciones_ocupadas.append(x)
                    if celdas == 6:
                        posicion_generada.append("Fuerte")
                        barcos_listados_sandokan.append(posicion_generada)
                        continuar = "no"
                    elif celdas == 2:
                        posicion_generada.append("Deposito de armas")
                        barcos_listados_sandokan.append(posicion_generada)
                        continuar = "no"
                    elif celdas == 1:
                        posicion_generada.append("Defensa sur")
                        barcos_listados_sandokan.append(posicion_generada)
                        continuar = "no"
    for celdas in celdas_verticales_sandokan():
        continuar = "si"
        while continuar == "si":
            posicion_generada = generador_barcos_verticales(celdas,dimension)
            contador = 0
            for x in range(celdas):
                        if posicion_generada[x] in posiciones_ocupadas:
                           contador += 1
            if contador == 0 :
                    for x in posicion_generada:
                        posiciones_ocupadas.append(x)
                    if celdas == 3:
                        posicion_generada.append("Campamento de defensa")
                        barcos_listados_sandokan.append(posicion_generada)
                        continuar = "no"
                    elif celdas == 2:
                        posicion_generada.append("Defensa norte")
                        barcos_listados_sandokan.append(posicion_generada)
                        continuar = "no"
    return barcos_listados_sandokan,posiciones_ocupadas             
def generar_barcos_armada_britanica (dimension):
    posiciones_ocupadas = []
    barcos_listados = []
    for celdas in celdas_horizontales_armada_britanica():
        continuar = "si"
        while continuar == "si":
            posicion_generada = generador_barcos_horizontales(celdas,dimension)
            contador = 0
            for x in range(celdas):
                        if posicion_generada[x] in posiciones_ocupadas:
                           contador += 1
            if contador == 0 :
                    for x in posicion_generada:
                        posiciones_ocupadas.append(x)
                    if celdas == 3:
                        posicion_generada.append("Galeon")
                        barcos_listados.append(posicion_generada)
                        continuar = "no"
                    elif celdas == 2:
                        posicion_generada.append("Galera")
                        barcos_listados.append(posicion_generada)
                        continuar = "no"
    for celdas in celdas_verticales_armada_britanica():
        continuar = "si"
        while continuar == "si":
            posicion_generada = generador_barcos_verticales(celdas,dimension)
            contador = 0
            for x in range(celdas):
                        if posicion_generada[x] in posiciones_ocupadas:
                           contador += 1
            if contador == 0 :
                    for x in posicion_generada:
                        posiciones_ocupadas.append(x)
                    if celdas == 6:
                        posicion_generada.append("Cruzero pesado")
                        barcos_listados.append(posicion_generada)
                        continuar = "no"
                    elif celdas == 2:
                        posicion_generada.append("Canonero")
                        barcos_listados.append(posicion_generada)
                        continuar = "no"
                    elif celdas == 1:
                        posicion_generada.append("Barcaza")
                        barcos_listados.append(posicion_generada)
                        continuar = "no"
    return barcos_listados,posiciones_ocupadas
def partida_normal (dimension):
    barcos_listados_sandokan, celdas_ocupadas_sandokan = generar_barcos_sandokan(dimension)
    barcos_listados_armada_britanica, celdas_ocupadas_armada_britanica = generar_barcos_armada_britanica(dimension)
    turnos (dimension,barcos_listados_sandokan,barcos_listados_armada_britanica)
    #print(barcos_listados_sandokan)
    #print(barcos_listados_armada_britanica)
def turnos (dimension,barcos_listados_sandokan,barcos_listados_armada_britanica):
    contador_turnos = 0
    if jugadores() == 1:
        contador_turnos = 2
        print("si")
    elif jugadores() == 2:
        contador_turnos = 1
        print("si2")
    finalizar = "no"
    tablero_sandokan = creacion_tableros(dimension)
    barcos_sandokan = barcos_listados_sandokan
    tablero_armada_britanica = creacion_tableros(dimension)
    barcos_armada_britanica = barcos_listados_armada_britanica
    coordenadas_usadas_sandokan = []
    coordenadas_usadas_armada_britanica = []
    aciertos_sandokan = 0
    aciertos_armada_britanica = 0
    while finalizar == "no": 
        if contador_turnos % 2 == 0:
            print("Sandokan!!")
            coordenada_correcta = "no"
            while coordenada_correcta == "no":
                coordenada_ataque = ingreso_coordenada_ataque(dimension)
                if coordenada_ataque in coordenadas_usadas_sandokan:
                    print("La coordenada que ingresaste fue previamente usada. Reingresa otra contraseña.")
                else:
                    coordenadas_usadas_sandokan.append(coordenada_ataque)
                    coordenada_correcta = "si"
            tablero_sandokan_nuevo , barcos_armada_britanica_nuevo,acierto = ataque_sandokan_normal(coordenada_ataque,barcos_armada_britanica,tablero_sandokan,dimension)
            tablero_sandokan = tablero_sandokan_nuevo
            barcos_armada_britanica =  barcos_armada_britanica_nuevo
            aciertos_sandokan += acierto
            contador_turnos += 1 
            if aciertos_sandokan == 14:
                print("SANDOKAN! OBTUVISTE LA VICTORIA.")
                print(barcos_armada_britanica)
                finalizar = "si"
        else:
            print("Armada Britanica!")
            coordenada_correcta = "no"
            while coordenada_correcta == "no":
                coordenada_ataque = ingreso_coordenada_ataque(dimension)
                if coordenada_ataque in coordenadas_usadas_armada_britanica:
                    print("La coordenada que ingresaste fue previamente usada. Reingresa otra contraseña.")
                else:
                    coordenadas_usadas_armada_britanica.append(coordenada_ataque)
                    coordenada_correcta = "si"
            tablero_armada_britanica_nuevo , barcos_sandokan_nuevo , acierto = ataque_armada_britanica_normal(coordenada_ataque,barcos_sandokan,tablero_armada_britanica,dimension)
            tablero_armada_britanica = tablero_armada_britanica_nuevo
            barcos_sandokan =  barcos_sandokan_nuevo
            aciertos_armada_britanica += acierto
            contador_turnos += 1 
            if aciertos_armada_britanica == 14:
                print("Armada Britanica! OBTUVISTE LA VICTORIA.")
                print(barcos_sandokan)
                finalizar = "si"        
def ataque_sandokan_normal (coordenada_ataque,barcos_armada_britanica,tablero_sandokan,dimension):
    acierto = 0
    print(barcos_armada_britanica)
    for x in range (len(barcos_armada_britanica)):
        if coordenada_ataque in barcos_armada_britanica[x]:
            acierto += 1
            print ("*********************************************************\nACERTAMOS SANDOKAN, El ataque dio en un objetivo!\n*********************************************************")
            barcos_armada_britanica[x].remove(coordenada_ataque)
            eliminado = len(barcos_armada_britanica[x])
            tablero_sandokan[coordenada_ataque[0]][coordenada_ataque[1]] = "X"
            if eliminado == 1:
                        print("*********************************************************\nVAMOS BIEN CAPITAN SANDOKAN!!! " + barcos_armada_britanica[x][0] + " FUE DESTRUIDO!\n*********************************************************")
    if acierto == 0:
        print("*********************************************************\nNo logramos acertar a un objetivo CAPITAN SANDOKAN.\n*********************************************************")
        tablero_sandokan[coordenada_ataque[0]][coordenada_ataque[1]] = "0"
    imprimir_tablero(dimension,tablero_sandokan)
    return tablero_sandokan, barcos_armada_britanica, acierto
def ataque_armada_britanica_normal (coordenada_ataque,barcos_sandokan,tablero_armada_britanica,dimension):
    acierto = 0
    print(barcos_sandokan)
    for x in range (len(barcos_sandokan)):
        if coordenada_ataque in barcos_sandokan[x]:
            print ("*********************************************************\nACERTAMOS ARMADA BRITANICA, El ataque dio en un objetivo!\n*********************************************************")
            barcos_sandokan[x].remove(coordenada_ataque)
            eliminado = len(barcos_sandokan[x])
            tablero_armada_britanica[coordenada_ataque[0]][coordenada_ataque[1]] = "X"
            acierto += 1
            if eliminado == 1:
                        print("*********************************************************\nVAMOS BIEN ARMADA BRITANICA!!! " + barcos_sandokan[x][0] + " FUE DESTRUIDO!\n*********************************************************")
    if acierto == 0:
        print("*********************************************************\nNo logramos acertar a un objetivo ARMADA BRITANICA.\n*********************************************************")
        tablero_armada_britanica[coordenada_ataque[0]][coordenada_ataque[1]] = "0"
    imprimir_tablero(dimension,tablero_armada_britanica)
    return tablero_armada_britanica, barcos_sandokan, acierto
def ingreso_coordenada_ataque(dimension):
    continuar_coordenada = "si"
    while continuar_coordenada == "si":
        coordenada_lateral_letra= input("*********************************************************\nIngrese la coordenada de ataque.\nLetra de la coordenada donde desea atacar(en mayuscula): ")
        coordenada_superior = int(input("Ingrese el numero de la coordenada: "))
        if coordenada_lateral_letra in abecedario_tablero(dimension) and coordenada_superior <= dimension :
            coordenada_superior -= 1
            abecedario = abecedario_tablero (dimension)
            for contador in range (len(abecedario)):
                if abecedario[contador] == coordenada_lateral_letra:
                    coordenada_lateral = contador
                    coordenada_ataque = [coordenada_lateral,coordenada_superior]
                    continuar_coordenada = "no"
                    print(coordenada_ataque)
                    return coordenada_ataque
        else:
            print("Coordenada ingresada incorrectamente")
def tipo_de_partida ():
    continuar = "no"
    while continuar == "no":
        selector_partida = int(input("1)Partida Normal.\n2)Partida Especial.\nIngrese que partida desea jugar: "))
        if selector_partida == 1 or selector_partida ==2:
            continuar = "si"
            return selector_partida 
        else:
            print("Opcion ingresada incorrectamente, reingresar su opcion.")
def generador_barcos_horizontales(celdas, dimension):
    continuar = "si"
    while continuar == "si":
        filarandom = random.randint(0,dimension-1)
        columnarandom = random.randint(0,dimension-1)
        posicion_parcial = []
        limite = dimension - celdas
        if columnarandom <= limite :
            tope = columnarandom + celdas
            for x in range (columnarandom, tope ):
                posicion_barco = [filarandom, x ]
                posicion_parcial.append(posicion_barco)
            continuar = "no"
    return posicion_parcial
def generador_barcos_verticales (celdas, dimension):
    continuar = "si"
    while continuar == "si":
        filarandom = random.randint(0,dimension-1)
        columnarandom = random.randint(0,dimension-1)
        posicion_parcial = []
        limite = dimension - celdas
        if filarandom <= limite :
            tope = filarandom + celdas
            for x in range (filarandom, tope ):
                posicion_barco = [x, columnarandom]
                posicion_parcial.append(posicion_barco)
            continuar = "no"
    return posicion_parcial
def celdas_horizontales_sandokan():
    celdas_barcos = [6,2,1]
    return celdas_barcos
def celdas_verticales_sandokan():
    celdas_barcos = [3,2]
    return celdas_barcos
def celdas_horizontales_armada_britanica():
    celdas_barcos = [3,2]
    return celdas_barcos
def celdas_verticales_armada_britanica():
    celdas_barcos = [6,2,1]
    return celdas_barcos
def main():
    dimension = dimension_tablero()
    imprimir_tablero(dimension,creacion_tableros(dimension))
    if tipo_de_partida() == 1:
            partida_normal(dimension)
    '''elif selector_partida == 2:
            partida_especial()'''
main()