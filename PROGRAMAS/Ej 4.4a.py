print("Vamos a calcular el maximo o minimo de una funcion cuadratica")

a = int(input("Ingresar el valor del primer coeficiente (A) :"))
b = int(input("Ingresar el valor del segundo coeficiente (B) :"))
c = int(input("Ingresar el valor del tercer coeficiente (C) :"))


xvertice = -b / (2 * a)

yvertice = a * (xvertice**2) + b * xvertice + c

if a > 0:
     
    print ("El punto " + str(xvertice) + "," + str(yvertice) + ": Es maximo de la funcion")

if a < 0:

    print ("El punto " + str(xvertice) + "," + str(yvertice) + ": Es minimo de la funcion")

else:
    print ("Esta no es una funcion cuadratica")
