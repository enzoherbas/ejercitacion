opcion = 0
alumno = []
padron = []
notas = []
while opcion !=5:
    opcion = int(input("1)Agregar alumno.\n2)Consultar aprobados.\n3)Cantidad de alumnos y promedio general.\n4)Quitar alumno.\n5)Salir.\nIngresar que opcion desea realizar: "))
    if opcion == 1:
        alumno.append(input("Ingresar el nombre del alumno: "))
        padron.append (int(input("Ingresar el padron del alumno: ")))
        notas.append (int(input("Ingrese la nota del alumno: ")))
        print ("Alumno agregado con exito. \n")
    elif opcion == 2:
        for aprobado in range(len(notas)):
            if notas[aprobado] >= 4:
                print("El alumno {0}, aprobo con una nota de {1}\n".format(alumno[aprobado],notas[aprobado]))
    elif opcion == 3:
        promedio=sum(notas)/len(alumno)
        total = len(alumno)
        print("Hay {0} alumnos, lo que da un promedio total de {1}\n".format(total,promedio))
    elif opcion == 4:
        eliminar = int(input("Ingresar el padron del alumno a eliminar: "))
        for x in range (len(padron)):
            if padron[x] == eliminar:
                print("El alumno {0} de padron {1} fue eliminado de la existencia.".format(alumno[x],padron[x]))
                padron.pop(x)
                alumno.pop(x)
                notas.pop(x)
    elif opcion == 5:
        print("Hasta la vista, baby")