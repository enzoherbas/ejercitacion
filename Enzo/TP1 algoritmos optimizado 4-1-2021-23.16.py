print("=================================================\nBIENVENIDO AL TP DE ENZO\n=================================================")
import string
import random

abecedario=list(string.ascii_uppercase)
tablero1  = []
tablero2 = []
tipos_barcos = ["Fuerte", "Campamento de defensa","Deposito de armas","Defensa norte","Defensa sur","Crucero pesado","Galeon","Cañonero","Galera","Barcaza"]
fila =[]
borde_superior= []
borde_lateral = []
posiciones_ocupadas = []
listanumerada_dimension = []
barcos_listados_sandokan = []
barcos_listados_armada_britanica = []
coordenadas_usadas_sandokan = []
coordenadas_usadas_armada_britanica = []
barcos_atacados_sandokan = []
barcos_atacados_armada_britanica = []
aciertos_sandokan = 0
aciertos_armada_britanica = 0
barcos_especiales = 0

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
    if personaje == "1":
        print("*********************************************************\nEl jugador 1, sera SANDOKAN Y SUS VALIENTES AMIGOS.\nEl jugador 2, sera LA ARMADA BRITANICA.\n*********************************************************")
        personaje_invalido = "no"
    elif personaje == "2":
        print("*********************************************************\nEl jugador 1, sera LA ARMADA BRITANICA.\nEl jugador 2, sera SANDOKAN Y SUS VALIENTES AMIGOS\n*********************************************************")
        personaje_invalido = "no"
    else:
        print("*************************\nDebe ingresar 1 o 2, para ser Sandokan o la Armada britanica. Ingrese nuevamente su opcion.\n*************************")
        
## TABLEROS EN BLANCO CON BORDES NUMERADOS
for x_bordesuperior in range(1,dimension+1):
    if x_bordesuperior < 11:
        borde_superior.append(str(x_bordesuperior))
    else:
        par = x_bordesuperior % 2
        if par == 0:
            borde_superior.append(str(x_bordesuperior))
        else:
            borde_superior.append(x_bordesuperior)
            
print(" ",borde_superior)
for y in range(dimension):
    listanumerada_dimension.append(y)
    
for x_tablero in range (dimension):
    fila =[]
    for y_tablero in range (dimension):
        fila.append("-")
    tablero1.append(fila)
    
for x_tablero in range (dimension):
    fila =[]
    for y_tablero in range (dimension):
        fila.append("-")
    tablero2.append(fila)
    
for x in range (dimension):
   print(abecedario[x],tablero1[x])
   borde_lateral.append(abecedario[x])

print("*********************************************************")
    
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
                if contador == 0 :
                    for x in range(celdas):
                            posiciones_ocupadas.append(posicion_parcial[x])
                            continuar = "no"
                    if barcos_especiales == 1:
                            if turno % 2 == 0:
                                if celdas == 6:
                                    posicion_parcial.append("Fuerte")
                                    barcos_listados_sandokan.append(posicion_parcial)
                                elif celdas == 2 and tipo_de_barco == "Deposito de armas":
                                    posicion_parcial.append("Deposito de armas")
                                    barcos_listados_sandokan.append(posicion_parcial)
                                elif celdas == 1:
                                    posicion_parcial.append("Defensa sur")
                                    barcos_listados_sandokan.append(posicion_parcial)
                                elif celdas == 3:
                                    posicion_parcial.append("Galeon")
                                    barcos_listados_sandokan.append(posicion_parcial)
                                elif celdas == 2 and tipo_de_barco == "Galera":
                                    posicion_parcial.append("Galera")
                                    barcos_listados_sandokan.append(posicion_parcial)
                            else:
                                if celdas == 6:
                                    posicion_parcial.append("Fuerte")
                                    barcos_listados_armada_britanica.append(posicion_parcial)
                                elif celdas == 2 and tipo_de_barco == "Deposito de armas":
                                    posicion_parcial.append("Deposito de armas")
                                    barcos_listados_armada_britanic.append(posicion_parcial)
                                elif celdas == 1:
                                    posicion_parcial.append("Defensa sur")
                                    barcos_listados_armada_britanic.append(posicion_parcial)
                                elif celdas == 3:
                                    posicion_parcial.append("Galeon")
                                    barcos_listados_armada_britanic.append(posicion_parcial)
                                elif celdas == 2 and tipo_de_barco == "Galera":
                                    posicion_parcial.append("Galera")
                                    barcos_listados_armada_britanic.append(posicion_parcial)
                    else:
                        if celdas_horizontales == [6,2,1]:
                            if celdas == 6:
                                posicion_parcial.append("Fuerte")
                                barcos_listados_sandokan.append(posicion_parcial)
                            elif celdas == 2:
                                posicion_parcial.append("Deposito de armas")
                                barcos_listados_sandokan.append(posicion_parcial)
                            elif celdas == 1:
                                posicion_parcial.append("Defensa sur")
                                barcos_listados_sandokan.append(posicion_parcial)
                        elif celdas_horizontales == [3,2]:
                            if celdas == 3:
                                posicion_parcial.append("Galeon")
                                barcos_listados_armada_britanica.append(posicion_parcial)
                            elif celdas == 2:
                                posicion_parcial.append("Galera")
                                barcos_listados_armada_britanica.append(posicion_parcial)
                        
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
                if contador == 0 :
                    for x in range(celdas):
                            posiciones_ocupadas.append(posicion_parcial[x])
                            continuar = "no"
                    if barcos_especiales == 1:
                            if turno % 2 == 0:
                                if celdas == 6:
                                    posicion_parcial.append("Crucero pesado")
                                    barcos_listados_sandokan.append(posicion_parcial)
                                elif celdas == 2 and tipo_de_barco == "Cañonero":
                                    posicion_parcial.append("Cañonero")
                                    barcos_listados_sandokan.append(posicion_parcial)
                                elif celdas == 1:
                                    posicion_parcial.append("Barcaza")
                                    barcos_listados_sandokan.append(posicion_parcial)
                                elif celdas == 3:
                                    posicion_parcial.append("Campamento de defensa")
                                    barcos_listados_sandokan.append(posicion_parcial)
                                elif celdas == 2 and tipo_de_barco == "Defensa norte":
                                    posicion_parcial.append("Defensa norte")
                                    barcos_listados_sandokan.append(posicion_parcial)
                            else:
                                if celdas == 6:
                                    posicion_parcial.append("Crucero pesado")
                                    barcos_listados_armada_britanica.append(posicion_parcial)
                                elif celdas == 2 and tipo_de_barco == "Cañonero":
                                    posicion_parcial.append("Cañonero")
                                    barcos_listados_armada_britanic.append(posicion_parcial)
                                elif celdas == 1:
                                    posicion_parcial.append("Barcaza")
                                    barcos_listados_armada_britanic.append(posicion_parcial)
                                elif celdas == 3:
                                    posicion_parcial.append("Campamento de defensa")
                                    barcos_listados_armada_britanic.append(posicion_parcial)
                                elif celdas == 2 and tipo_de_barco == "Defensa norte":
                                    posicion_parcial.append("Defensa norte")
                                    barcos_listados_armada_britanic.append(posicion_parcial)
                    if celdas_verticales == [3,2]:
                            if celdas == 3:
                                posicion_parcial.append("Campamento de defensa")
                                barcos_listados_sandokan.append(posicion_parcial)
                            elif celdas == 2:
                                posicion_parcial.append("Defensa norte")
                                barcos_listados_sandokan.append(posicion_parcial)
                    elif celdas_verticales == [6,2,1]:
                            if celdas == 6:
                                posicion_parcial.append("Crucero pesado")
                                barcos_listados_armada_britanica.append(posicion_parcial)
                            elif celdas == 2:
                                posicion_parcial.append("Cañonero")
                                barcos_listados_armada_britanica.append(posicion_parcial)
                            elif celdas == 1:
                                posicion_parcial.append("Barcaza")
                                barcos_listados_armada_britanica.append(posicion_parcial)
                    
        else:
                continuar = "si"

#GENERO, JUNTO CON LAS FUNCIONES PREVIAMENTE HECHAS, LAS POSICIONES DE LOS BARCOS DE SANDOKAN Y LA ARMADA BRITANICA
#PARA LA PARTIDA COMUN, 2 TABLEROS EN LA QUE LOS BARCOS ESTAN A LO LARGO DEL MISMO
continuar = "si"
while continuar == "si":
    #BARCOS DE SANDOKAN
    celdas_horizontales = [6,2,1]
    celdas_verticales = [3,2]
    for celdas in celdas_horizontales:
        barcohorizontal (celdas)
    for celdas in celdas_verticales:
        barcovertical (celdas)
        
    #print("SANDOKAN",barcos_listados_sandokan)#ESTA LINEA ES PARA VER LOS BARCOS ELEGIDOS ALEATORIAMENTE
    posiciones_ocupadas = []
    #BARCOS DE LA ARMADA BRITANICA
    celdas_horizontales = [3,2]
    celdas_verticales = [6,2,1]
    for celdas in celdas_horizontales:
        barcohorizontal (celdas)
    for celdas in celdas_verticales:
        barcovertical (celdas)
    #print("BRITANICOS",barcos_listados_armada_britanica)  ESTA LINEA ES PARA VER LOS BARCOS ELEGIDOS ALEATORIAMENTE
    continuar = "no"

#=============== GENERAR BARCOS PARTIDA ESPECIAL ===================
def generarbarco (tipo_de_barco):
    if tipo_de_barco == "Fuerte":
        barco_horizontal(6)
    elif tipo_de_barco == "Campamento de defensa":
        barco_vertical(3)
    elif tipo_de_barco == "Deposito de armas":
        barco_horizontal(2)
    elif tipo_de_barco == "Defensa norte":
        barco_vertical(2)
    elif tipo_de_barco == "Defensa sur":
        barco_horizontal(1)
    elif tipo_de_barco == "Crucero pesado":
        barco_vertical(6)
    elif tipo_de_barco == "Galeon":
        barco_horizontal(3)
    elif tipo_de_barco == "Cañonero":
        barco_vertical(2)
    elif tipo_de_barco == "Galera":
        barco_horizontal(2)
    elif tipo_de_barco == "Barcaza":
        barco_vertical(1)

#=============== SELECTOR DE PARTIDA===============================
comenzar_partida = "no"
while comenzar_partida == "no":

    tipo_de_partida = int(input("1)Partida NORMAL.\n2)Partida ESPECIAL.\nIngrese la opcion que desee jugar: "))
    if tipo_de_partida == 1 or tipo_de_partida == 2:
        comenzar_partida = "si"
    else:
        print("No elegiste una opcion valida, reingrese su opcion!.")

        
#================== PARTIDA NORMAL ===============================
if tipo_de_partida == 1:
    print("*********************************************************\nElegiste la partida NORMAL.")
    continuar = "si"

    if personaje == "1":
            turno = 0
    else:
            turno = 1
            
    while continuar == "si":
            
        if turno % 2 == 0:
            contador_acierto = 0
            ingresar_coordenada = "si"
            while ingresar_coordenada == "si":
                    coordenada_lateral_letra= input("*********************************************************\nSANDOKAN!\nIngrese la coordenada de ataque.\nLetra de la coordenada donde desea atacar(en mayuscula): ")
                    coordenada_superior = int(input("Ingrese el numero de la coordenada: "))
                    if coordenada_lateral_letra in borde_lateral and coordenada_superior <= dimension :
                            coordenada_superior -= 1
                            for contador in range (len(borde_lateral)):
                                if borde_lateral[contador] == coordenada_lateral_letra:
                                    coordenada_lateral = contador
                            coordenada_ataque = [coordenada_lateral,coordenada_superior]
                            #print(coordenada_ataque)
                            if coordenada_ataque in coordenadas_usadas_sandokan:
                                print("Ingresaste una coordenada previamente usada, reingrese una coordenada nuevamente.")
                            else:
                                coordenadas_usadas_sandokan.append(coordenada_ataque)
                                ingresar_coordenada = "no"
                    else:
                        print("Coordenada ingresada invalida. Reingresar la coordenada de ataque!.")
            for x in range (len(barcos_listados_armada_britanica)):
                if coordenada_ataque in barcos_listados_armada_britanica[x]:
                    contador_acierto += 1
                    print ("*********************************************************\nACERTAMOS SANDOKAN, El ataque dio en un objetivo!\n*********************************************************")
                    aciertos_sandokan += 1
                    barcos_listados_armada_britanica[x].remove(coordenada_ataque)
                    eliminado = len(barcos_listados_armada_britanica[x])
                    tablero1[coordenada_lateral][coordenada_superior] = "X"
                    if eliminado == 1:
                        print("*********************************************************\nVAMOS BIEN CAPITAN SANDOKAN!!! " + barcos_listados_armada_britanica[x][0] + " FUE DESTRUIDO!\n*********************************************************")
            if contador_acierto == 0:
                    print("*********************************************************\nNo logramos acertar a un objetivo CAPITAN SANDOKAN.\n*********************************************************")
                    tablero1[coordenada_lateral][coordenada_superior] = "0"
            print("S",borde_superior)
            for x in range (dimension):
                print(abecedario[x],tablero1[x])
            turno += 1
            if aciertos_sandokan == 14:
                continuar = "no"
            
        else:
            contador_acierto = 0
            ingresar_coordenada = "si"
            while ingresar_coordenada == "si":
                    coordenada_lateral_letra= input("*********************************************************\nARMADA BRITANICA!\nIngrese la coordenada de ataque.\nLetra de la coordenada donde desea atacar(en mayuscula): ")
                    coordenada_superior = int(input("Ingrese el numero de la coordenada: "))
                    if coordenada_lateral_letra in borde_lateral and coordenada_superior <= dimension:
                            coordenada_superior -= 1
                            for contador in range (len(borde_lateral)):
                                if borde_lateral[contador] == coordenada_lateral_letra:
                                    coordenada_lateral = contador
                            coordenada_ataque = [coordenada_lateral,coordenada_superior]
                            #print(coordenada_ataque)
                            if coordenada_ataque in coordenadas_usadas_sandokan:
                                print("Ingresaste una coordenada previamente usada, reingrese una coordenada nuevamente.")
                            else:
                                coordenadas_usadas_sandokan.append(coordenada_ataque)
                                ingresar_coordenada = "no"
                    else:
                        print("Coordenada ingresada invalida. Reingresar la coordenada de ataque!.")
            for x in range (len(barcos_listados_sandokan)):
                if coordenada_ataque in barcos_listados_sandokan[x]:
                    contador_acierto +=1
                    print ("*********************************************************\nACERTAMOS CAPITAN DE LA ARMADA BRITANICA, El ataque dio en un objetivo!\n*********************************************************")
                    aciertos_armada_britanica +=1
                    barcos_listados_sandokan[x].remove(coordenada_ataque)
                    eliminado = len(barcos_listados_sandokan[x])
                    tablero2[coordenada_lateral][coordenada_superior] = "X"
                    if eliminado == 1:
                        print("*********************************************************\nVAMOS BIEN CAPITAN DE LA ARMADA BRITANICA!!! " + barcos_listados_sandokan[x][0] + " FUE DESTRUIDO!\n*********************************************************")
            if contador_acierto == 0:
                    print("*********************************************************\nNo logramos acertar a un objetivo CAPITAN DE LA ARMADA BRITANICA\n*********************************************************")
                    tablero2[coordenada_lateral][coordenada_superior] = "0"            
            print("AB",borde_superior)
            for x in range (dimension):
                print(abecedario[x],tablero2[x])
            turno += 1
            if aciertos_armada_britanica == 14:
                continuar = "no"

    if aciertos_sandokan == 14:
        print("*********************************************************")
        print("*********************************************************")
        print("MUY BIEN SANDOKAN, LOGRASTE LA VICTORIAAAA!")
        print("*********************************************************")
        print("Las posiciones que faltaron de la ARMADA BRITANICA fueron," + barcos_listados_armada_britanica )
    elif aciertos_armada_britanica == 14:
        print("*********************************************************")
        print("*********************************************************")
        print("MUY BIEN CAPITAN DE LA ARMADA BRITANICA, LOGRASTE LA VICTORIAAAA!")
        print("Las posiciones que faltaron de SANDOKAN fueron," + barcos_listados_sandokan )

#=============== PARTIDA ESPECIAL =============================
#=============== AJUSTE DE ALEATORIEDAD ======================
elif tipo_de_partida == 2:
    barcos_especiales = 1
    aleatoriedad = "no"
    while aleatoriedad == "no":        
        eleccion_aleatoriedad = int(input("Elegiste la partida ESPECIAL, por defecto hay una aleatoriedad de robar barcos al enemigo de *30 %*.\nSi quiere cambiar el porcentaje de aleatoriedad por defecto, ingrese (1) o (2) para continuar sin cambios: "))
        if eleccion_aleatoriedad == 1:
            rango_aleatoriedad = int(input("Ingrese el valor, de 1 a 100, para dejar seteada la aleatoriedad: "))
            print("{0}% sera la nueva aleatoriedad para la partida!.".format(rango_aleatoriedad))
            aleatoriedad = "si"
        elif eleccion_aleatoriedad == 2:
                rango_aleatoriedad = 30
                print("La aleatoriedad por defecto sera 30%")
                aleatoriedad = "si"
        else:
                print("Elegiste una opcion incorrecta, reingrese la opcion de (1) o (2)")
                
#============ COMIENZO DE PARTIDA ESPECIAL ===========================               
    if personaje == "1":
                turno = 0
    else:
                turno = 1
                
    while continuar == "si":
                probabilidad = random.randrange(100)
                if probabilidad <= rango_aleatoriedad:
                    minimo = 10
                    for contador in range (len(barcos_listados_armada_britanica)):
                        for contador2 in lista[contador]:
                            if lista[contador] not in barcos_atacados_sandokan:
                                menor = len(barcos_listados_armada_britanica[contador])
                                if minimo >= menor:
                                    barco_minimo = barcos_listados_armada_britanica[contador]
                                    minimo = menor
                    barco_robado = barco_minimo
                    print(barco_minimo)
                    barcos_listados_armada_britanica.remove(barco_minimo)
                    tipo = len(barco_robado) - 1
                    tipo_de_barco = barco_robado[tipo]
                    generarbarco(tipo_de_barco)
                    
                    if turno % 2 == 0:
                        contador_acierto = 0
                        ingresar_coordenada = "si"
                    while ingresar_coordenada == "si":
                            coordenada_lateral_letra= input("*********************************************************\nSANDOKAN!\nIngrese la coordenada de ataque.\nLetra de la coordenada donde desea atacar(en mayuscula): ")
                            coordenada_superior = int(input("Ingrese el numero de la coordenada: "))
                            print(borde_lateral,borde_superior)
                            if coordenada_lateral_letra in borde_lateral and coordenada_superior <= dimension :
                                    coordenada_superior -= 1
                                    for contador in range (len(borde_lateral)):
                                        if borde_lateral[contador] == coordenada_lateral_letra:
                                            coordenada_lateral = contador
                                    coordenada_ataque = [coordenada_lateral,coordenada_superior]
                                    #print(coordenada_ataque)
                                    if coordenada_ataque in coordenadas_usadas_sandokan:
                                        print("Ingresaste una coordenada previamente usada, reingrese una coordenada nuevamente.")
                                    else:
                                        coordenadas_usadas_sandokan.append(coordenada_ataque)
                                        ingresar_coordenada = "no"
                            else:
                                print("Coordenada ingresada invalida. Reingresar la coordenada de ataque!.")
                            for x in range (len(barcos_listados_armada_britanica)):
                                if coordenada_ataque in barcos_listados_armada_britanica[x]:
                                    contador_acierto += 1
                                    print ("*********************************************************\nACERTAMOS SANDOKAN, El ataque dio en un objetivo!\n*********************************************************")
                                    aciertos_sandokan += 1
                                    barcos_listados_armada_britanica[x].remove(coordenada_ataque)
                                    eliminado = len(barcos_listados_armada_britanica[x])
                                    tablero1[coordenada_lateral][coordenada_superior] = "X"
                                    if eliminado == 1:
                                        print("*********************************************************\nVAMOS BIEN CAPITAN SANDOKAN!!! " + barcos_listados_armada_britanica[x][0] + " FUE DESTRUIDO!\n*********************************************************")
                            if contador_acierto == 0:
                                    print("*********************************************************\nNo logramos acertar a un objetivo CAPITAN SANDOKAN.\n*********************************************************")
                                    tablero1[coordenada_lateral][coordenada_superior] = "0"
                            print("S",borde_superior)
                            for x in range (dimension):
                                print(abecedario[x],tablero1[x])
                            turno += 1
                            if aciertos_sandokan == 14:
                                continuar = "no"
                        
                    else:
                        contador_acierto = 0
                        ingresar_coordenada = "si"
                        while ingresar_coordenada == "si":
                                coordenada_lateral_letra= input("*********************************************************\nARMADA BRITANICA!\nIngrese la coordenada de ataque.\nLetra de la coordenada donde desea atacar(en mayuscula): ")
                                coordenada_superior = int(input("Ingrese el numero de la coordenada: "))
                                if coordenada_lateral_letra in borde_lateral and coordenada_superior <= dimension:
                                        coordenada_superior -= 1
                                        for contador in range (len(borde_lateral)):
                                            if borde_lateral[contador] == coordenada_lateral_letra:
                                                coordenada_lateral = contador
                                        coordenada_ataque = [coordenada_lateral,coordenada_superior]
                                        #print(coordenada_ataque)
                                        if coordenada_ataque in coordenadas_usadas_sandokan:
                                            print("Ingresaste una coordenada previamente usada, reingrese una coordenada nuevamente.")
                                        else:
                                            coordenadas_usadas_sandokan.append(coordenada_ataque)
                                            ingresar_coordenada = "no"
                                else:
                                    print("Coordenada ingresada invalida. Reingresar la coordenada de ataque!.")
                        for x in range (len(barcos_listados_sandokan)):
                            if coordenada_ataque in barcos_listados_sandokan[x]:
                                contador_acierto +=1
                                print ("*********************************************************\nACERTAMOS CAPITAN DE LA ARMADA BRITANICA, El ataque dio en un objetivo!\n*********************************************************")
                                aciertos_armada_britanica +=1
                                barcos_listados_sandokan[x].remove(coordenada_ataque)
                                eliminado = len(barcos_listados_sandokan[x])
                                tablero2[coordenada_lateral][coordenada_superior] = "X"
                                if eliminado == 1:
                                    print("*********************************************************\nVAMOS BIEN CAPITAN DE LA ARMADA BRITANICA!!! " + barcos_listados_sandokan[x][0] + " FUE DESTRUIDO!\n*********************************************************")
                        if contador_acierto == 0:
                                print("*********************************************************\nNo logramos acertar a un objetivo CAPITAN DE LA ARMADA BRITANICA\n*********************************************************")
                                tablero2[coordenada_lateral][coordenada_superior] = "0"            
                        print("AB",borde_superior)
                        for x in range (dimension):
                            print(abecedario[x],tablero2[x])
                        turno += 1
                        if aciertos_armada_britanica == 14:
                            continuar = "no"
