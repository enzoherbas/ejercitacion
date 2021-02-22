#import string
#abecedario=list(string.ascii_lowercase)
#print(abecedario)

lista = [[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]]
import random
continuar = "no"
while continuar != "si":
    numerorandom = random.choice(lista)
    filarandom = random.choice(numerorandom)
    columnarandom = random.choice(numerorandom)
    barco6 = []
    continuar = "si"
    if filarandom <= 4 :
        continuar = "si"
        tope = filarandom + 6
        
        for x in range (filarandom, tope ):
            posicion_barco6 = [columnarandom, x]
            barco6.append(posicion_barco6)
            posicion_barco6 = []
        print(barco6)
    else:
        continuar = "no"
#for x in range (numerorandom):
        