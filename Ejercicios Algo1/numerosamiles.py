frase = "25525525505555"
lista = list(frase)
contador = 0
lista2 = []
for x in range(len(lista)):
    contador += 1
    lista2.append(lista[x])
    if contador%3 == 0:
        lista2.append(".")
if lista2[-1] == ".":
    lista2.pop(-1)
numero = ("".join(lista2))
print(numero[::-1])