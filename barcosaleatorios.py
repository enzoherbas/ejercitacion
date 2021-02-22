posiciones_ocupadas = [[5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9]]
posicion_barco3v = [[5, 1], [5,10], [2, 5]]
contador = 0
for x in range(0,3):
                if posicion_barco3v[x] in posiciones_ocupadas:
                    contador += 1 
                    print("PASO")
if contador == 0:
                    print("No paso")
