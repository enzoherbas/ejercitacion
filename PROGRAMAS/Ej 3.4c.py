
print("Ingrese los valores de sus 2 vectores para realizar el producto vectorial :")
x1 = int(input("Ingresar X del primer vector :"))
y1 = int(input("Ingresar Y del primer vector :"))
z1 = int(input("Ingresar Z del primer vector :"))
    
x2 = int(input("Ingresar X del segundo vector :"))
y2 = int(input("Ingresar Y del segundo vector :"))
z2 = int(input("Ingresar Z del segundo vector :"))

pv_x = (y1*z2) - (z1*y2)
pv_y = (z1*x2) - (x1*z2)
pv_z = (x1*y2) - (y1*x2)

print( str(pv_x) + "," + str(pv_y) + "," + str(pv_z) + " :Es el producto vectorial")


