dimension = int(input("ingresar dimension: "))
matriz= []
for x in range(dimension):
    fila = []
    for y in range(dimension):
        fila.append(0)
    matriz.append(fila)
    matriz[x][x] = 1
    print(matriz[x])
    