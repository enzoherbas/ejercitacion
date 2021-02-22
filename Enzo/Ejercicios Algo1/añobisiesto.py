año = int(input("Ingresar año: "))
if año%4 == 0 and año%100 == 0:
    if año%400 == 0:
        print("Es bisiesto")
    elif año%400 != 0:
        print("No es bisiesto")
elif año%4 == 0 and año%100 != 0:
    print("Es bisiesto")

else:
    print("No es bisiesto.")