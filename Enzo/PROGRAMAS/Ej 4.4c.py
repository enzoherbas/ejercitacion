print("Vamos a hallar la interseccion de 2 rectas")

p1 = float(input("Ingresar el valor de la primera pendiente :"))
o1 = float(input("Ingresar el valor de la primera ordenada al origen :"))
p2 = float(input("Ingresar el valor de la segunda pendiente :"))
o2 = float(input("Ingresar el valor de la segunda ordenada al origen :"))

if p1 == p2:

    print ("Las rectas son paralelas, por lo cual nunca van a tener interseccion.")
     
else:

    x = (o1 - o2)/(p2 - p1)

    y = (p1 * x) + o1

    print("La interseccion de la recta sera en :" + str(x) + "," + str(y))

   

    

    
