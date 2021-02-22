print("VAMOS A VER CUAL ES EL NUMERO MAS GRANDE LOS SOLICITADOS")

print("Dame 3 valores y te indicare cual es el mayor")

x = float(input("Dame el primer valor: "))

y = float(input("Dame el segundo valor: "))

z = float(input("Dame el tercer valor: "))

if x > y and x > z:
          
    if y > z :
          
        print("El numero " + str(x) + " es el mayor de todos y el numero " + str(z) + " es el menor.")

    if y < z :
        
        print("El numero " + str(x) + " es el mayor de todos y el numero " + str(y) + " es el menor.")
              
if y > x and y > z:
          
        if x > z:
          
            print("El numero " + str(y) + " es el mayor de todos y el numero " + str(z) + " es el menor.")

        if x < z:
        
            print("El numero " + str(y) + " es el mayor de todos y el numero " + str(x) + " es el menor.")

if z > y and z > x:
          
        if x > y:
          
            print("El numero " + str(z) + " es el mayor de todos y el numero " + str(y) + " es el menor.")

        if x < y:
        
        
            print("El numero " + str(z) + " es el mayor de todos y el numero " + str(x) + " es el menor.")

if x==y or y==z:
              print("Los numeros tienen que ser distintos")
elif x==z:
                print("Los numeros tienen que ser distintos")
