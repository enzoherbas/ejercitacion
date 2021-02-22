import string
import random

abecedario=list(string.ascii_uppercase)
print(abecedario[2])
letra = input("Ingrese Letra")
for x in range (len(abecedario)):
    if abecedario[x] == letra:
        numeroletra = x
        print(numeroletra)
    