
print("PROGRAMA QUE DETERMINA SI UN NUMERO ES PAR O IMPAR")

x = float(input("Dame el numero : "))

y = x
z = x % 2

if z==0:
    print("El numero " + str(y) + " es par.")
else:
    print("El numero " + str(y) + " es impar.")
