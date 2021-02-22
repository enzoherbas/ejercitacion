dia = int(input("Ingrese el  numero de dia y te dire a que dia del año corresponde: "))

fecha = dia
if dia <= 366:
    
    if dia == 1:

        print ("La fecha " + str(fecha) + "que ingreso es Lunes.")

    if dia == 2:

        print ("La fecha " + str(fecha) + "que ingreso es Martes.")

    if dia == 3:
        print ("La fecha " + str(fecha) + "que ingreso es Miercoles.")

    if dia == 4:

        print ("La fecha " + str(fecha) + "que ingreso es Jueves.")

    if dia == 5:

        print ("La fecha " + str(fecha) + "que ingreso es Viernes.")

    if dia == 6:

        print ("La fecha " + str(fecha) + "que ingreso es Sabado")

    if dia == 7:

        print ("La fecha " + str(fecha) + "que ingreso es Domingo.")

    if dia > 7:

        dia %= 7

        if dia == 1:

            print ("La fecha " + str(fecha) + "que ingreso es Lunes.")
            
        if dia == 2:

            print ("La fecha " + str(fecha) + "que ingreso es Martes.")

        if dia == 3:

            print ("La fecha " + str(fecha) + "que ingreso es Miercoles.")
        if dia == 4:

            print ("La fecha " + str(fecha) + "que ingreso es Jueves.")
        if dia == 5:

            print ("La fecha " + str(fecha) + "que ingreso es Viernes.")
        if dia == 6:
            
            print ("La fecha " + str(fecha) + "que ingreso es Sabado.")
            
        if dia == 0:
            print ("La fecha " + str(fecha) + "que ingreso es Domingo.")

else:

    print("El numero debe estar entre 1 y 366")
    
