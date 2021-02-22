def palabras_repetidas (frase):
    palabras_listadas = frase.split(" ")
    palabras_repetidas = []
    for palabra in palabras_listadas:
        repeticiones = frase.count(palabra)
        repeticiones_palabras = (palabra,repeticiones)
        if repeticiones_palabras not in palabras_repetidas:
            palabras_repetidas.append(repeticiones_palabras)
    print(dict(palabras_repetidas))
def letras_repetidas (frase):
    letras_listadas = list(frase)
    letras_repetidas = []
    for letra in letras_listadas:
        if letra != " ":
            repeticiones = frase.count(letra)
            repeticiones_letra = (letra,repeticiones)
            if repeticiones_letra not in letras_repetidas:
                letras_repetidas.append(repeticiones_letra)
    print(dict(letras_repetidas))

    
def main ():
    frase = input("Ingresar una frase o palabras, separadas por espacios: ")
    palabras_repetidas(frase)
    letras_repetidas(frase)
    
    

main()
    