y= int(input("Calculadora de 2 variables.\n1)Para Suma.\n2)Para resta. \n3)Para multiplicar. \n4)Para dividir. \n5)Division entera. \n6)Potencia de primera a segunda. \n7)Modulo. \n:"))

if y == 1:
        numero = int(input("Elegiste la suma, dame el primer valor: "))
        numero += int(input("Dame el segundo valor: "))
        print ("La respuesta es " + str(numero) )
if y == 2:
        numero = int(input("Elegiste la resta, dame el primer valor: "))
        numero -= int(input("Dame el segundo valor: "))
        print ("La respuesta es " + str(numero) )

if y == 3:
        numero = int(input("Elegiste la multiplicacion, dame el primer valor: "))
        numero *= int(input("Dame el segundo valor: "))
        print ("La respuesta es " + str(numero) )

if y == 4:
        numero = int(input("Elegiste la division, dame el primer valor: "))
        numero /= int(input("Dame el segundo valor: "))
        print ("La respuesta es " + str(numero) )

if y == 5:
        numero = int(input("Elegiste la division entera dame el primer valor: "))
        numero //= int(input("Dame el segundo valor: "))
        print ("La respuesta es " + str(numero) )

if y == 6:
        numero = int(input("Elegiste la potencia, dame el primer valor: "))
        numero **= int(input("Dame el segundo valor: "))
        print ("La respuesta es " + str(numero) )

if y == 7:
        numero = int(input("Elegiste el resto, dame el primer valor: "))
        numero %= int(input("Dame el segundo valor: "))
        print ("La respuesta es " + str(numero) )

if y < 1 and y > 7:
    print("papi, del 1 al 7")
