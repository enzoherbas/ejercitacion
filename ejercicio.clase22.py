menu = []
mesas = []
opcion_a = 0
while opcion_a != 6:
    plato=[]
    mesa = []
    opcion = int(input("1)Cargar menu del restaurant.\n2)Listar los platos.\n3)Abrir nueva mesa.\n4)Mostrar mesas abiertas e importes.\n5)Agregar mas pedidos a mesas abiertas.\n6)Cerrar mesa(del ejercicio seria el punto c).\n7)Finalizar.\nIngresar la opcion a realizar: "))

    if opcion == 1:
        entrada_plato = input("\n-Si el plato es una ENTRADA, ingresar la tecla (e).\n-Si el plato es uno PRINCIPAL, ingresar la tecla (p).\n-Si el plato es un POSTRE, ingresar la tecla (o).\n: ")
        plato.append(entrada_plato)
        nombre_plato = input("Ingresar el nombre del plato: ")
        plato.append(nombre_plato)
        precio_plato = int(input("Ingrese el precio del plato: "))
        plato.append(precio_plato)
        menu.append(plato)
        print("Ingresaste el plato satisfactoriamente.\n")
        print(menu)

    elif opcion == 2:
        for contador_opcion_2 in range (3):
            contador = 0
            if contador_opcion_2 == 0: 
                print("\n==================================\nLos platos de ENTRADA que hay registrados son: ")
                for x in range (len(menu)):
                    if menu[x][0] == "e":
                        print(menu[x][1])
                        contador += 1
                if contador == 0:
                    print("No hay platos de entrada ingresados")
            elif contador_opcion_2 == 1: 
                print("==================================\nLos platos PRINCIPALES que hay registrados son: ")
                for x in range (len(menu)):
                    if menu[x][0] == "p":
                        print(menu[x][1])
                        contador +=1
                if contador == 0:
                        print("No hay platos principales ingresados")
            elif contador_opcion_2 == 2: 
                print("==================================\nLos platos de ENTRADA que hay registrado son: ")
                for x in range (len(menu)):
                    if menu[x][0] == "o":
                        print(menu[x][1])
                        contador +=1
                if contador == 0:
                        print("No hay platos de postre ingresados\n")

    elif opcion == 3:
        pedidos = "si"
        numero_mesa = int(input("\nIngresar el numero de mesa:"))
        mesa.append(numero_mesa)
        while pedidos == "si" :
            plato_pedido = input("Ingresar el plato a agregar a la mesa: ")
            plato_cantidad =int(input("Cuantos platos desea agregar: "))
            for contador_opcion_3_1 in range(len(menu)):
                if menu [contador_opcion_3_1][1] == plato_pedido:
                    for contador_opcion_3_2 in range (plato_cantidad):
                        mesa.append(menu[contador_opcion_3_1])
            print("Plato agregado a la mesa con exito")
            pedidos = input("Desea seguir agregando platos? (si/no)")
            if pedidos == "no":
                print("Mesa {0} abierta.".format (numero_mesa))
                mesas.append(mesa)
                print(mesas)

    elif opcion == 4:
        for contador_opcion_4_1 in range(0,len(mesas)):
            mesa_opcion4 = mesas[contador_opcion_4_1][0]
            total_mesa = 0
            for contador_opcion_4_2 in range (1,len(mesas[contador_opcion_4_1])):
                total_mesa += mesas[contador_opcion_4_1][contador_opcion_4_2][2]
            print("\nLa mesa {0} esta abierta, hasta ahora, con un importe total de {1} dolares.".format(mesa_opcion4,total_mesa))

    elif opcion == 5:
        mesa_opcion_5 = int(input("\nIngrese a que mesa desea seguir ingresando articulos: "))
        for contador_opcion_5_1 in range(len(mesas)):
            if mesas[contador_opcion_5_1][0] == mesa_opcion_5:
                pedidos = "si"
                while pedidos == "si" :
                    plato_pedido = input("\nIngresar el plato a agregar a la mesa: ")
                    plato_cantidad =int(input("Cuantos platos desea agregar: "))
                    for contador_opcion_5_2 in range(len(menu)):
                        if menu [contador_opcion_5_2][1] == plato_pedido:
                            for contador_opcion_5_3 in range (plato_cantidad):
                                mesas[contador_opcion_5_1].append(menu[contador_opcion_5_2])
                    print("Plato agregado a la mesa con exito")
                    pedidos = input("Desea seguir agregando platos? (si/no)")
                    if pedidos == "no":
                        print("Items agregados a la Mesa {0} exitosamente.".format (mesa_opcion_5))
    elif opcion == 6:
        opcion_6 = int(input("\n1-Indicar que volumen de $ se facturó de un determinado plato a elección del usuario.\n2-Indicar cual es el plato más pedido de cada tipo.\n3-Indicar los pedidos donde se hayan pedido 2 entradas o mas.\n4-Cerrar mesa."))
        if opcion_6 == 1:
            total_importe_6 = 0
            ingresar_mesa = int(input("Ingrese el numero de mesa: "))
            for contador_opcion_6_1 in range (len(mesas)):
                if mesas[contador_opcion_6_1][0] == ingresar_mesa:
                    importe_plato = input("Ingresar el plato que desea ver su monto total: ")
                    for contador_opcion_6_2 in range (1,len(mesas[contador_opcion_6_1])):
                        if mesas[contador_opcion_6_1][contador_opcion_6_2][2] == importe_plato:
                            total_importe_6 += mesas[contador_opcion_6_1][contador_opcion_6_2][3]
                    print("El importe total que se gasto en el plato {0} es de {1} dolares".format (importe_plato,total_importe_6))
        elif opcion_6 == 3:
            for x in range(len(mesas)):
                contador_opcion_6_5 = 0
                for y in range(1,(len(mesas[x]))):
                    if mesa [x][y][0] == "e":
                        contador_opcion_6_5 += 1
                if contador_opcion_6_5 >= 2:
                    print("La mesa {0} tiene mas de 2 entradas".format (mesa[x][0]))
