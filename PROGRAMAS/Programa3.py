

nombre = input ("Dame tu nombre y despues vamos a calcular tu promedio :")

x = float(input("Dame tu primer nota:"))
y = float(input("Dame tu segunda nota: "))
z = float(input("Dame tu tercer nota: "))

f = (x + y + z)/3

if f >= 7 :
    print(nombre + ":Tu promedio es " + str(round(f,4)) + " ,felicidades. Aprobaste")

else :
    print(nombre + ":Tu promedio es " + str (f) + ". Desaprobaste")


    
