"ZANAHORIN Y ZANAHORON"
def comparar_precios (numero_str):
    lista_str = numero_str.split()
    lista_int = []
    repetir = 0
    
    for precio in lista_str:
        lista_int.append(int(precio))
    if lista_int[0] < 1 or lista_int[0] > 100000:
        print("El precio de ZANAHORIN no esta en los limites establecidos.")
        repetir += 1
    elif lista_int[1] < 1 or lista_int[1] > 100000:
        print("El precio de ZANAHORON no esta en los limites establecidos.")
        repetir += 1
    else:
        if lista_int[0] > lista_int[1]:
            print("Conviene comprar en ZANAHORON")
        elif lista_int[0] < lista_int[1]:
            print("Conviene comprar en ZANAHORIN")
        elif lista_int[0] == lista_int[1]:
            print("DA IGUAL")
    return repetir

def main():
    finalizar = 1
    while finalizar >= 1:
        print("Ingresar los precios de ZANAHORIN Y ZANAHORON, separados con un espacio")
        precios_str = input("Primero ZANAHORIN y luego ZANAHORON: ")
        finalizar = comparar_precios(precios_str)

main()