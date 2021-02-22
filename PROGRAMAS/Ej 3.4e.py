print("Vamos a calcular el area de un cuadrilatero convexo formado por 4 puntos en R2")

x1 = int(input("Ingresar X del primer punto :"))
y1 = int(input("Ingresar Y del primer punto :"))
z1 = 0
    
x2 = int(input("Ingresar X del segundo punto :"))
y2 = int(input("Ingresar Y del segundo punto :"))
z2 = 0

x3 = int(input("Ingresar X del tercer punto :"))
y3 = int(input("Ingresar Y del tercer punto :"))
z3 = 0

x4 = int(input("Ingresar X del cuarto punto :"))
y4 = int(input("Ingresar Y del cuarto punto :"))
z4 = 0



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

adx = x1 - x4
ady = y1 - y4
adz = z1 - z4

pv1_x = (acy*adz) - (acz*ady)
pv1_y = (acz*adx) - (acx*adz)
pv1_z = (acx*ady) - (acy*adx)


norma1 = pv1_x**2 + pv1_y**2 + pv1_z**2

norma1 **= (0.5)

norma1 /= 2

total = norma + norma1

print("El area del triangulo sera: " + str(total))
