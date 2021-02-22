"Ejercicio de LISTADO DE EQUIPOS"
def definir_nombre_equipo ():
    nombre_equipo = input("Ingresar el nombre del equipo: ").capitalize()
    return nombre_equipo

def definir_titulos ():   
    titulos = []
    continuar = "si"
    while continuar != "no":
        titulo = []
        nombre_titulo = input("Ingrese el nombre del titulo: ").capitalize()
        dia_titulo = int(input("Ingresar el dia del año del titulo: "))
        mes_titulo = int(input("Ingresar el mes del año del titulo: "))
        año_titulo = int(input("Ingresar el año del titulo: "))
        fecha_titulo = (dia_titulo,mes_titulo,año_titulo)
        titulo.append(nombre_titulo)
        titulo.append(fecha_titulo)
        cantidad_jugadores = int(input("Ingresar la cantidad de jugadores: "))
        for jugador in range(cantidad_jugadores):
            nombre_jugador = input("Ingresar el nombre y apellido del jugador: ").capitalize()
            titulo.append(nombre_jugador)
        titulos.append(titulo)
        continuar = input("Ingrese NO para dejar de ingresar titulos o en caso contrario, ingrese cualquier tecla: ").lower()
    return titulos

def crear_dicc_equipos ():
    dicc_equipos = []
    continuar = "si"
    while continuar == "si":
        nombre_equipo, titulos = (definir_nombre_equipo(),definir_titulos())
        equipo = (nombre_equipo,titulos)
        dicc_equipos.append(equipo)
        continuar = input ("Si desea continuar ingrese SI, en caso contrario NO: ").lower()
    return dict(dicc_equipos)

def contador_titulos (equipos):
    mayor = 0
    for x in equipos.keys():
        if len(equipos[x]) > mayor:
            mayor = len(equipos[x])
            equipo_mas_ganador = x 
    print("El equipo mas ganador es {0} con {1} titulos.".format(equipo_mas_ganador,mayor))

def ultimo_titulo (equipos):
    mayor = [0,0,0]
    equipo_ultimo_titulo = input("Ingresar el equipo que desea saber su ultimo titulo: ").capitalize()
    titulos =  equipos[equipo_ultimo_titulo]
    for titulo in titulos:
        if titulo[1][2] > mayor[2]:
            mayor = titulo[1]
        elif titulo[1][2] == mayor [2]:
            if titulo[1][1] > mayor[1]:
                mayor = titulo[1]
            elif titulo[1][1] == mayor[1]:
                if titulo[1][0] > mayor[0]:
                    mayor = titulo[1]
    print("El ultimo titulo ganado por {0} fue en {1}.".format(equipo_ultimo_titulo,mayor))  
    
def jugador_titulos (equipos):
    equipo_ultimo_titulo = input("Ingresar el equipo que desea saber su jugador con mas titulos: ").capitalize()
    plantilla_titulos =  equipos[equipo_ultimo_titulo]
    mayor = 0
    jugadores = []
    for plantilla in plantilla_titulos:
        for jugador in range(2,len(plantilla)):
            jugadores.append(plantilla[jugador])
    for jugador_mas_ganador in jugadores:
        participaciones = jugadores.count(jugador_mas_ganador)
        if participaciones > mayor:
            mayor = participaciones
            nombre_jugador = jugador_mas_ganador
    print("El jugador mas ganador es", nombre_jugador)

def opciones (opcion,equipos):
    if opcion == 1:
        contador_titulos(equipos)
    elif opcion == 2:
        ultimo_titulo(equipos)
    elif opcion == 3:
        jugador_titulos(equipos)

def main ():
    LISTADO_EQUIPOS = crear_dicc_equipos()
    finalizar = False
    while finalizar == False:
        equipos = LISTADO_EQUIPOS
        print("1)Equipo con mas titulos.\n2)Ultimo titulo de un equipo.")
        print("3)Jugador con mas titulos de un equipo.\n4)Salir.")
        opcion = int(input("Ingrese la opcion que desea:"))
        if opcion == 4:
            finalizar = True
        else:
            opciones(opcion,equipos)

main()
            
            
            
    