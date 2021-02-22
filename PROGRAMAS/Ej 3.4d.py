print("Vamos a calcular el area de un triangulo formado por 3 puntos en R3")

x1 = int(input("Ingresar X del primer punto :"))
y1 = int(input("Ingresar Y del primer punto :"))
z1 = int(input("Ingresar Z del primer punto :"))
    
x2 = int(input("Ingresar X del segundo punto :"))
y2 = int(input("Ingresar Y del segundo punto :"))
z2 = int(input("Ingresar Z del segundo punto :"))

x3 = int(input("Ingresar X del tercer punto :"))
y3 = int(input("Ingresar Y del tercer punto :"))
z3 = int(input("Ingresar Z del tercer punto :"))

abx = x1 - x2
aby = y1 - y2
abz = z1 - z2

acx = x1 - x3
acy = y1 - y3
acz = z1 - z3

pv_x = (aby*acz) - (abz*acy)
pv_y = (abz*acx) - (abx*acz)
pv_z = (abx*acy) - (aby*acx)


norma = pv_x**2 + pv_y**2 + pv_z**2

norma **= (0.5)

norma/= 2

print("El area del triangulo sera: " + str(norma))

