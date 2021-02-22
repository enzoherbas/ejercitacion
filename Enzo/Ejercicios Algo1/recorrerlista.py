numeros = (-25,1,5,-2,-4,-5,7,8,-20,15)
mayor = 0
for x in range (len(numeros)):
    for y in range (x+1,len(numeros)):
        posible = numeros[x] * numeros [y]
        if posible > mayor:
            mayor = posible
            mayor_combinacion = ( str(numeros[x])+" * "+ str(numeros[y]))
print(mayor_combinacion)
print(mayor)