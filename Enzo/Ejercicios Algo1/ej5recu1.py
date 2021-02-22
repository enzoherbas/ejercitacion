'''Ingreso una palabra principal, posteriormente las 5 palabras a comprar
y con un FOR las recorro viendo sus semejanzas'''
palabras_totales = []
palabra_principal = list(input("Ingresar la palabra principal: "))
for cantidad_palabras in range (5):
    palabra_lista = list(input("Ingresar la palabra a comparar: "))
    palabras_totales.append(palabra_lista)
for palabra in palabras_totales:
    CONTADOR = 0
    for letra in palabra_principal:
        if letra in palabra:
            if palabra.count(letra) == palabra_principal.count(letra):
                CONTADOR += 1
                if CONTADOR == len(palabra_principal):
                    print("Se puede generar", "".join(palabra))
