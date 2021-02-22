print("Vamos a calcular raices de un polinomio")

a = int(input("Ingresar el valor del primer coeficiente (A) :"))
b = int(input("Ingresar el valor del segundo coeficiente (B) :"))
c = int(input("Ingresar el valor del tercer coeficiente (C) :"))

x1 = (-b + ((b**2) - 4 * a * c)**0.5)/(2*a)
x2 = (-b - ((b**2) - 4 * a * c)**0.5)/(2*a)

print("Las raices del polinomio son :" + str(x1) + " y " + str(x2))

