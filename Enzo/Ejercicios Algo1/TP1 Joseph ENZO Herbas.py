import random
def dimension_tablero():
    #PRE:
    #POST: CREARA LA DIMENSION DEL TABLERO, CON LA CUAL SERA LA VARIABLE MAS "FUERTE" DE MI CODIGO. CON EL CREARE CASI TODAS LAS DEMAS FUNCIONES 
    continuar_tablero = "Si"
    while continuar_tablero == "Si":
        dimension = int(input("Ingrese la dimension de los tableros de juego(Debe estar entre 10 y 24): "))
        if dimension > 24 or dimension < 10:
            print("Ingresaste una opcion no valida.")
        else:
            continuar_tablero = "No"
    return dimension
def borde_superior(dimension):
    #PRE:INGRESA LA DIMENSION INGRESADA AL COMIENZO
    #POST: DEVUELVE EL BORDE SUPERIOR A IMPRIMIR DEL TABLERO
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
def creacion_tableros(dimension):
    #PRE: INGRESA LA DIMENSION
    #POST: DEVUELVE LOS CASILLEROS DE LOS TABLEROS, AHI ESTARAN LOS BARCOS Y SE REALIZARAN LOS ATAQUES
    tablero = []
    for x_tablero in range (dimension):
        fila =[]
        for y_tablero in range (dimension):
            fila.append("-")
        tablero.append(fila)
    return tablero
def abecedario_tablero (dimension):
    #PRE:INGRESO LA DIMENSION
    #POST:DEVUELVE UN LISTADO CON LAS LETRAS QUE ESTARAN TANTO PARA IMPRIMIR EL TABLERO, COMO PARA POSTERIORMENTE INGRESAR LA COORDENADA DE LETRA
    abecedario = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    abecedario_tablero = []
    for x in range (dimension):
        abecedario_tablero.append(abecedario[x])
    return abecedario_tablero
def imprimir_tablero(dimension,tablero):
    #PRE:   INGRESO LA DIMENSION Y EL TABLERO CREADO PREVIAMENTE 
    #POST:  DEVUELVE LA IMPRESION DEL TABLERO 
    print(" ",borde_superior(dimension))
    borde_lateral = abecedario_tablero(dimension)
    for x in range (dimension):
       print(borde_lateral[x],tablero[x])
def ajustar_probabilidad():
    #PRE: 
    #POST: SE AJUSTA LA PROBABILIDAD DE LOS ROBOS DE BARCOS
    probabilidad_lista = "no"
    while probabilidad_lista == "no":
        ajuste_probablidad = int(input("Vamos a jugar un batalla naval de manera especial.\nLa probabilidad de robo de los barcos aleatorios por defecto sera de un 30%.\nPara elegir una probablidad distinta ingresa (1) o (2) si queres jugar con la probabilidad por defecto."))
        if ajuste_probablidad == 1:
            probabilidad_robo = int(input("Ingresar la nueva probabilidad:"))
            probabilidad_lista = "si"
        elif ajuste_probablidad == 2:
            print("La probabilidad sera la que esta por defecto (30%)")
            probabilidad_robo = 30
            probabilidad_lista = "si"
        else:
            print("Opcion ingresa incorrectamente")
    return probabilidad_robo 
def jugadores():
    #PRE:
    #POST:SE ELIGE QUE PERSONAJE SERA CADA JUGADOR
    jugadores_listo = "No"
    while jugadores_listo == "No":
        elegir_personaje = int(input("Jugador 1 que personaje desea.\n1 ) Sandokan y sus valientes amigos.\n2 ) Armada britanica.\nIngrese el valor 1 o 2 para elegir a su personaje:"))
        if elegir_personaje == 1:
            print("*********************************************************\nEl jugador 1, sera SANDOKAN Y SUS VALIENTES AMIGOS.\nEl jugador 2, sera LA ARMADA BRITANICA.\n*********************************************************")
            jugadores_listo = "Si"
            turno = 0
            #return elegir_personaje
        elif elegir_personaje == 2:
            print("*********************************************************\nEl jugador 1, sera LA ARMADA BRITANICA.\nEl jugador 2, sera SANDOKAN Y SUS VALIENTES AMIGOS\n*********************************************************")
            jugadores_listo= "Si"
            turno = 1
            #return elegir_personaje
        else:
            print("*************************\nDebe ingresar 1 o 2, para ser Sandokan o la Armada britanica. Ingrese nuevamente su opcion.\n*************************")
    return turno
def celdas_horizontales_sandokan():
    #PRE:
    #POST:SE DEVUELVE LAS CELDAS DE LOS BARCOS HORIZONTALES PARA SANDOKAN
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
def generador_barcos_horizontales(celdas, dimension):
    #PRE: SE INGRESA LA CANTIDAD DE CELDAS QUE OCUPARA EL BARCO A GENERAR JUNTO CON LA DIMENSION DEL TABLERO
    #POST: DEVUELVE UNA POSIBILIDAD DE POSICION DE BARCO HORIZONTAL
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
    #PRE: SE INGRESA LA CANTIDAD DE CELDAS QUE OCUPARA EL BARCO A GENERAR JUNTO CON LA DIMENSION DEL TABLERO
    #POST: DEVUELVE UNA POSIBILIDAD DE POSICION DE BARCO HORIZONTAL
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
def generar_barcos_sandokan (dimension):
    #PRE: INGRESA LA DIMENSION
    #POST: DEVUELVE TODOS LOS BARCOS "PREDETERMINADOS" PARA SANDOKAN
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
    #PRE:INGRESA UNA DIMENSION
    #POST: DEVUELVE TODOS LOS BARCOS "PREDETERMINADOS" PARA LA ARMADA BRITANICA
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
def ingreso_coordenada_ataque(dimension):
    #PRE: INGRESO LA DIMENSION PARA CORROBORAR LOS LIMITES 
    #POST:DEVUELVE UNA POSIBLE COORDENADA A USAR
    continuar_coordenada = "si"
    while continuar_coordenada == "si":
        coordenada_lateral_letra= input("*********************************************************\nIngrese la coordenada de ataque.\nLetra de la coordenada donde desea atacar(en mayuscula): ")
        coordenada_superior = int(input("Ingrese el numero de la coordenada: "))
        if coordenada_lateral_letra in abecedario_tablero(dimension) and coordenada_superior <= dimension :
            coordenada_superior -= 1
            abecedario = abecedario_tablero(dimension)
            for contador in range (len(abecedario)):
                if abecedario[contador] == coordenada_lateral_letra:
                    coordenada_lateral = contador
                    coordenada_ataque = [coordenada_lateral,coordenada_superior]
                    continuar_coordenada = "no"
                    print(coordenada_ataque)
        else:
            print("Coordenada ingresada incorrectamente")
    return coordenada_ataque
def eleccion_barco_menor (barcos_a_atacar,barcos_atinados):
    #PRE: INGRESO LOS BARCOS QUE OCUPA EL ADVERSARIO Y LOS BARCOS YA ATACADOS PARA EVITAR ROBARLOS
    #POST: DEVUELVE LOS BARCOS A ATACAR SIN EL BARCO QUE SE ROBARA, Y EL BARCO DE MENOR TAMAÑO
    menor = 10
    contador = 0
    for x in range (len(barcos_a_atacar)):
        if len(barcos_a_atacar[x]) < menor and barcos_a_atacar[x] not in barcos_atinados:
            menor = len(barcos_a_atacar [x])
            barco_menor = barcos_a_atacar[x]
            contador +=1
    if contador == 0:
            print("NO SE PUEDEN ROBAR BARCOS")
            barco_menor = 0
    else:
        barcos_a_atacar.remove(barco_menor)
    return barcos_a_atacar, barco_menor
def generar_barcos_robados(posiciones_ocupadas,barcos_jugador,barco_chico,dimension):
    #PRE: INGRESO LAS POSICIONES OCUPADAS POR LOS BARCOS, LOS BARCOS DEL JUGADOR EN ESE MOMENTO, DEL BARCO ROBADO Y DE LA DIMENSION
    #POST:DEVUELVO LAS POSICIONES OCUPADAS CON EL BARCO CREADO Y EL BARCO ROBADO YA ADHERIDO A LA LISTA DE BARCOS DEL PERSONAJE
    tipo_barco = barco_chico[-1]
    if tipo_barco == "Fuerte":
        continuar = "si"
        while continuar == "si":
            posicion_generada = generador_barcos_horizontales(6,dimension)
            contador = 0
            for x in range(6):
                if posicion_generada[x] in posiciones_ocupadas:
                           contador += 1
            if contador == 0:
                for x in posicion_generada:
                        posiciones_ocupadas.append(x)
            posicion_generada.append("Fuerte")
            barcos_jugador.append(posicion_generada)
            continuar = "no"  
    elif tipo_barco == "Campamento de defensa":
        continuar = "si"
        while continuar == "si":
            posicion_generada = generador_barcos_verticales(3,dimension)
            contador = 0
            for x in range(3):
                if posicion_generada[x] in posiciones_ocupadas:
                           contador += 1
            if contador == 0:
                for x in posicion_generada:
                        posiciones_ocupadas.append(x)
            posicion_generada.append("Campamento de defensa")
            barcos_jugador.append(posicion_generada)
            continuar = "no"
    elif tipo_barco == "Deposito de armas":
        continuar = "si"
        while continuar == "si":
            posicion_generada = generador_barcos_horizontales(2,dimension)
            contador = 0
            for x in range(2):
                if posicion_generada[x] in posiciones_ocupadas:
                           contador += 1
            if contador == 0:
                for x in posicion_generada:
                        posiciones_ocupadas.append(x)
            posicion_generada.append("Deposito de armas")
            barcos_jugador.append(posicion_generada)
            continuar = "no"
    elif tipo_barco == "Defensa norte":
        continuar = "si"
        while continuar == "si":
            posicion_generada = generador_barcos_verticales(2,dimension)
            contador = 0
            for x in range(2):
                if posicion_generada[x] in posiciones_ocupadas:
                           contador += 1
            if contador == 0:
                for x in posicion_generada:
                        posiciones_ocupadas.append(x)
            posicion_generada.append("Defensa norte")
            barcos_jugador.append(posicion_generada)
            continuar = "no"
    elif tipo_barco == "Defensa sur":
        continuar = "si"
        while continuar == "si":
            posicion_generada = generador_barcos_horizontales(1,dimension)
            contador = 0
            for x in range(1):
                if posicion_generada[x] in posiciones_ocupadas:
                           contador += 1
            if contador == 0:
                for x in posicion_generada:
                        posiciones_ocupadas.append(x)
            posicion_generada.append("Defensa sur")
            barcos_jugador.append(posicion_generada)
            continuar = "no"
    elif tipo_barco == "Crucero pesado":
        continuar = "si"
        while continuar == "si":
            posicion_generada = generador_barcos_verticales(6,dimension)
            contador = 0
            for x in range(6):
                if posicion_generada[x] in posiciones_ocupadas:
                           contador += 1
            if contador == 0:
                for x in posicion_generada:
                        posiciones_ocupadas.append(x)
            posicion_generada.append("Crucero pesado")
            barcos_jugador.append(posicion_generada)
            continuar = "no"
    elif tipo_barco == "Galeon":
        continuar = "si"
        while continuar == "si":
            posicion_generada = generador_barcos_horizontales(3,dimension)
            contador = 0
            for x in range(3):
                if posicion_generada[x] in posiciones_ocupadas:
                           contador += 1
            if contador == 0:
                for x in posicion_generada:
                        posiciones_ocupadas.append(x)
            posicion_generada.append("Galeon")
            barcos_jugador.append(posicion_generada)
            continuar = "no"
    elif tipo_barco == "Canonero":
        continuar = "si"
        while continuar == "si":
            posicion_generada = generador_barcos_verticales(2,dimension)
            contador = 0
            for x in range(2):
                if posicion_generada[x] in posiciones_ocupadas:
                           contador += 1
            if contador == 0:
                for x in posicion_generada:
                        posiciones_ocupadas.append(x)
            posicion_generada.append("Canonero")
            barcos_jugador.append(posicion_generada)
            continuar = "no"
    elif tipo_barco == "Galera":
        continuar = "si"
        while continuar == "si":
            posicion_generada = generador_barcos_horizontales(2,dimension)
            contador = 0
            for x in range(2):
                if posicion_generada[x] in posiciones_ocupadas:
                           contador += 1
            if contador == 0:
                for x in posicion_generada:
                        posiciones_ocupadas.append(x)
            posicion_generada.append("Galera")
            barcos_jugador.append(posicion_generada)
            continuar = "no"
    elif tipo_barco == "Barcaza":
        continuar = "si"
        while continuar == "si":
            posicion_generada = generador_barcos_verticales(1,dimension)
            contador = 0
            for x in range(1):
                if posicion_generada[x] in posiciones_ocupadas:
                           contador += 1
            if contador == 0:
                for x in posicion_generada:
                        posiciones_ocupadas.append(x)
            posicion_generada.append("Barcaza")
            barcos_jugador.append(posicion_generada)
            continuar = "no"
    return barcos_jugador,posiciones_ocupadas
def eliminar_celdas_ocupadas (barco_chico, posiciones_ocupadas):
    #PRE: INGRESO EL BARCO ROBADO Y LAS POSICIONES OCUPADAS, ESTO PARA QUE A FUTURO SI SE ROBA UN BARCO PUEDA ESTAR DONDE PREVIAMENTE ESTABA ESTE BARCO ROBADO
    #POST: DEVUELVO LAS POSICIONES OCUPADAS CON LAS CELDAS QUE OCUPADA EL BARCO YA ELIMINADAS
    for x in range(len(barco_chico)):
        if barco_chico[x] in posiciones_ocupadas:
            posiciones_ocupadas.remove(barco_chico[x])
    return posiciones_ocupadas
def eliminar_coordenadas_usadas (barco_menor,coordenadas_usadas):
    #PRE:INGRESO EL BARCO ROBADO Y LAS COORDENDAS USADAS, PARA QUE AL MOMENTO DE ATACAR EL RIVAL PUEDA VOLVER ATACAR DONDE YA ATACO
    #POST: DEVUELVO LAS COORDENADAS USADAS PERMITIENDO VOLVER A ATACAR DONDE YA ATACO, CON LA OPORTUNIDAD DE PEGAR AL BARCO ROBADO
    for x in range (len(barco_menor)):
        if barco_menor[x] in coordenadas_usadas:
            coordenadas_usadas.remove(barco_menor[x])
    return coordenadas_usadas  
def condicion_victoria (barcos_a_atacar):
    #PRE: INGRESO LOS BARCOS A ATACAR, PARA CORROBORAR LA CONDICION DE VICTORIA
    #POST: EN EL CASO QUE LOS BARCOS SOLO TENGAN 1 ESPACIO (en el que yo guarde unicamente el nombre del barco), SE OBTENDRA LA VICTORIA 
    contador = 0
    vacio = []
    respuesta_victoria = "no"
    for x in range (len(barcos_a_atacar)):
        if len(barcos_a_atacar[x]) >= 2:
            contador +=1
    if contador == 0:
        print("GANASTE !!!!")
        respuesta_victoria = "si"
    return respuesta_victoria
#=========FUNCIONES "FUERTES"
def ataque (coordenada_ataque,barcos_a_atacar,tablero_atacante,dimension):
    #PRE: INGRESO LA COORDENADA, BARCOS A ATACAR, TABLERO DEL ATACANTE Y DIMENSION
    #POST: DEVUELVE EL TABLERO CON LA SEÑAL QUE SI IMPACTO O NO EN UN OBJETIVO, LOS BARCOS A ATACAR CON LA MODIFICACION DE CELDA Y EN EL CASO QUE IMPACTE DEVUELVE EL BARCO ATACADO
    acierto = 0
    for x in range (len(barcos_a_atacar)):
        if coordenada_ataque in barcos_a_atacar[x]:
            acierto += 1
            print ("*********************************************************\nEl ataque dio en un objetivo!\n*********************************************************")
            barcos_a_atacar[x].remove(coordenada_ataque)
            barcos_atacados = barcos_a_atacar[x]
            eliminado = len(barcos_a_atacar[x])
            tablero_atacante[coordenada_ataque[0]][coordenada_ataque[1]] = "X"
            if eliminado == 1:
                        print("*********************************************************\nVAMOS BIEN!!! " + barcos_a_atacar[x][0] + " FUE DESTRUIDO!\n*********************************************************")
    if acierto == 0:
        print("*********************************************************\nNo logramos acertar a un objetivo.\n*********************************************************")
        tablero_atacante[coordenada_ataque[0]][coordenada_ataque[1]] = "0"
        barcos_atacados = []
    imprimir_tablero(dimension,tablero_atacante)
    return tablero_atacante, barcos_a_atacar,barcos_atacados
def turnos (dimension,barcos_listados_sandokan,barcos_listados_armada_britanica,celdas_ocupadas,celdas_ocupadas2):
    #PRE: INGRESO LA DIMENSION Y LA INFORMACION DE POSICION DE BARCOS DE AMBOS JUGADORES
    #POST: AL FINALIZAR, SE OBTIENE UN GANADOR. LOS TURNOS SE DESARROLLAN Y SE VAN GUARDANDO LOS DATOS A MEDIDA AVANZA
    contador_turnos = jugadores()
    celdas_ocupadas_sandokan = celdas_ocupadas
    celdas_ocupadas_armada_britanica = celdas_ocupadas2
    probabilidad = ajustar_probabilidad()
    finalizar = "no"
    tablero_sandokan = creacion_tableros(dimension)
    barcos_sandokan = barcos_listados_sandokan
    tablero_armada_britanica = creacion_tableros(dimension)
    barcos_armada_britanica = barcos_listados_armada_britanica
    coordenadas_usadas_sandokan = []
    coordenadas_usadas_armada_britanica = []
    barcos_atinados_sandokan = []
    barcos_atinados_armada_britanica = []
    while finalizar == "no": 
        if contador_turnos % 2 == 0:
            if random.randint(1,100) <= probabilidad:
                barcos_armada_britanica,barco_menor = eleccion_barco_menor(barcos_armada_britanica,barcos_atinados_sandokan)
                if barco_menor != 0: 
                    eliminar_celdas_ocupadas(barco_menor,celdas_ocupadas_armada_britanica)
                    eliminar_coordenadas_usadas(barco_menor,coordenadas_usadas_armada_britanica)
                    print("ROBASTE {0} AL ENEMIGO!".format(barco_menor[-1]))                
                    barcos_sandokan,celdas_ocupadas_sandokan = generar_barcos_robados(celdas_ocupadas_sandokan,barcos_sandokan,barco_menor,dimension)
            print("SANDOKAN!!")
            coordenada_correcta = "no"
            while coordenada_correcta == "no":
                coordenada_ataque = ingreso_coordenada_ataque(dimension)
                if coordenada_ataque in coordenadas_usadas_sandokan:
                    print("La coordenada que ingresaste fue previamente usada. Reingresa otra contraseña.")
                else:
                    coordenadas_usadas_sandokan.append(coordenada_ataque)
                    coordenada_correcta = "si"
            tablero_sandokan, barcos_armada_britanica, barco_acertado = ataque(coordenada_ataque,barcos_armada_britanica,tablero_sandokan,dimension)
            barcos_atinados_sandokan.append(barco_acertado)
            contador_turnos += 1
            print(barcos_armada_britanica)
            finalizar = condicion_victoria(barcos_armada_britanica)            
        else:
            if random.randint(1,100) <= probabilidad:
                barcos_sandokan,barco_menor = eleccion_barco_menor(barcos_sandokan,barcos_atinados_armada_britanica)
                if barco_menor != 0:
                    eliminar_celdas_ocupadas(barco_menor,celdas_ocupadas_armada_britanica)
                    eliminar_coordenadas_usadas(barco_menor,coordenadas_usadas_sandokan)
                    print("ROBASTE {0} AL ENEMIGO!".format(barco_menor[-1]))                
                    barcos_armada_britanica,celdas_ocupadas_armada_britanica = generar_barcos_robados(celdas_ocupadas_armada_britanica,barcos_armada_britanica,barco_menor,dimension)
            print("ARMADA BRITANICA!")
            coordenada_correcta = "no"
            while coordenada_correcta == "no":
                coordenada_ataque = ingreso_coordenada_ataque(dimension)
                if coordenada_ataque in coordenadas_usadas_armada_britanica:
                    print("La coordenada que ingresaste fue previamente usada. Reingresa otra contraseña.")
                else:
                    coordenadas_usadas_armada_britanica.append(coordenada_ataque)
                    coordenada_correcta = "si"
            tablero_armada_britanica, barcos_sandokan, barco_acertado = ataque(coordenada_ataque,barcos_sandokan,tablero_armada_britanica,dimension)
            barcos_atinados_armada_britanica.append(barco_acertado)
            contador_turnos += 1 
            print(barcos_sandokan)
            finalizar = condicion_victoria(barcos_sandokan)
def iniciar_partida(dimension):
    #PRE: INGRESO LA DIMENSION
    #POST: AL FINALIZAR LA FUNCION, SE TERMINA LA PARTIDA, POR LO CUAL FINALIZA EL JUEGO TAMBIEN.
    
    barcos_listados_sandokan, celdas_ocupadas_sandokan = generar_barcos_sandokan(dimension)
    barcos_listados_armada_britanica, celdas_ocupadas_armada_britanica = generar_barcos_armada_britanica(dimension)
    turnos (dimension,barcos_listados_sandokan,barcos_listados_armada_britanica,celdas_ocupadas_sandokan,celdas_ocupadas_armada_britanica)
def main():
    #PRE: INGRESE MI VARIABLE DE MAYOR IMPACTO EN MI CODIGO, EL CUAL ES LA DIMENSION PARA DESARROLLAR EL JUEGO
    #POST: EL JUEGO TERMINA
    dimension = dimension_tablero()
    imprimir_tablero(dimension,creacion_tableros(dimension))
    iniciar_partida(dimension)
main()