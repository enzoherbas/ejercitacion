"Estetica"
def ingreso_pacientes (pacientes_nuevos,cantidad_nuevos,pacientes_viejos,cantidad_viejos,solicitud_tratamiento,solitud_nuevos):
    print("Ingrese:")
    ingreso_dni = int(input("El numero de DNI: "))
    ingreso_nombre = input("El nombre del usuario: ").capitalize()
    consultas_asistidas = int(input("El numero de veces que asistio a una consulta: "))
    consultas_totales = []
    continuar = "si"
    while continuar == "si":
        tratamientos_realizados = input("El tratamiento que se realizo: ").capitalize()
        veces_realizado = int(input("Veces realizado: "))
        solicitud_tratamiento[tratamientos_realizados] += veces_realizado
        if consultas_asistidas == 1:
            solitud_nuevos[tratamientos_realizados] += veces_realizado
        consulta = (tratamientos_realizados,veces_realizado)
        consultas_totales.append(consulta)
        continuar = input("Si desea seguir cargando tratamientos, ingrese SI, en caso contrario NO.").lower()
    paciente = [ingreso_dni,ingreso_nombre,consultas_asistidas,consultas_totales]
    if consultas_asistidas == 1:
        cantidad_nuevos += 1
        pacientes_nuevos.append(paciente)
    else:
        cantidad_viejos += 1
        pacientes_viejos.append(paciente)
    return pacientes_nuevos,cantidad_nuevos,pacientes_viejos,cantidad_viejos,solicitud_tratamiento,solitud_nuevos

def tratamiento_mas_solicitado(tratamientos):
    tratamientos_clave = tratamentos.keys()
    mayor = 0
    for nombre in tratamientos_clave:
        if tratamientos(nombre) > mayor:
            mayor = nombre
            numero_mayor = tratamientos(nombre)
    print("El tratamiento mas usado es {} con {} consultas.".format(mayor,numero_mayor))
          
def menu ():
    finalizar = "no"
    pacientes_nuevos = []
    pacientes_viejos = []
    cantidad_nuevos = 0
    cantidad_viejos = 0
    solicitud_tratamiento = {"Higiene profunda": 0, "Tratamiento acne": 0, "Tratamiento tensor con aparatologia": 0, "Tratamiento revitalizante": 0}
    solicitud_tratamiento_nuevos = {"Higiene profunda": 0, "Tratamiento acne": 0, "Tratamiento tensor con aparatologia": 0, "Tratamiento revitalizante": 0}
    while finalizar == "no":
        print("Ingrese que opcion desea: ")
        opcion = int(input('''
    1)Ingresar paciente.
    2)Reporte tratamiento mas solicitado.
    3)Reporte de ganancias totales.
    4)Reporte de pacientes nuevos y viejos.
    5)Cual es el tratamiento mas solicitado por pacientes nuevos.
    6)Finalizar.
        '''))
        if opcion == 1 :
            pacientes_nuevos,cantidad_nuevos,pacientes_viejos,cantidad_viejos, solicitud_tratamiento = ingreso_pacientes(pacientes_nuevos,cantidad_nuevos,pacientes_viejos,cantidad_viejos,solicitud_tratamiento,solicitud_tratamiento_nuevos)
        if opcion == 2:
            tratamiento_mas_solicitado(solicitud_tratamiento)
        if opcion == 4:
            print("Los pacientes nuevos son {} y los pacientes viejos son {}".format(cantidad_nuevos,cantidad_viejos))
        if opcion == 5:
            tratamiento_mas_solicitado(solicitud_tratamiento_nuevos)
        if opcion == 6:
            finalizar = "si"

def main ():
    menu()
    
main()