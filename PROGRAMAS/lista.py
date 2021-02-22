n = int(input("ingresar dimension de la matriz: "))

m = []

for i in range (n):
    
    fila = []
    
    

    for j in range(n):

        if i==j:
                val = 1
                fila.append(val)
        else:
                val = 0
                fila.append(val)
    m.append(fila)
print(m)




    
