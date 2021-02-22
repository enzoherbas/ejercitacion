c = float(input("Ingresar la capital inicial en pesos :"))

x = float(input("Ingresar la tasa de intereses :"))

n = float(input("Ingresar cantidad de años :"))

d =(1 + (x/100))

d **=n

c *= d

print("El capital final sera " + str(c))
