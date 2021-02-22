"NUMERO ESCALONADO"
def escalonado (numeros_listados):
    numeros_int = []
    for numero_str in numeros_listados:
        numeros_int.append(int(numero_str))
    mayor = -1
    contador = 0
    cortar = 0
    for numero in range(len(numeros_int)):
        if numeros_int[numero] > mayor and cortar == 0:
            mayor = numeros_int[numero]
            contador += 1
        else:
            cortar = 1
    if cortar == 0:
        print("Es escalonado",contador)
    else:
        print("No es escalonado", contador)
        
def main():
    numero_ingresado = input("Ingresar un numero para saber si es escalonado: ")
    numeros_listados = list(numero_ingresado)
    escalonado(numeros_listados)

main()
    