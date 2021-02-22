'''Maquina de billetes'''
def definir_billetes():
    '''Generador de Billetes'''
    valores_billetes = []
    continuar = "si"
    while continuar == "si":
        valor_billete = int(input("Ingrese el valor del billete: "))
        valores_billetes.append(valor_billete)
        continuar = input('''Ingrese SI para continuar o
                            cualquier tecla para finalizar el ingreso de valores: ''').lower()
    return valores_billetes

def devolucion_billetes(importe,billetes):
    '''Devuelve los billetes y sus respectivos importes'''
    resto = importe
    billetes_devolucion = []
    for valor_billete in billetes:
        billetes_usados = resto // valor_billete
        resto %= valor_billete
        total_billetes = (valor_billete, billetes_usados)
        billetes_devolucion.append(total_billetes)
    if resto != 0:
        print("El importe ingresado no es factible para los billetes. Reingrese otro valor")
        billetes_devolucion = 0
    return billetes_devolucion

def main():
    '''Junto todas las funciones para lanzar el programa'''

    billetes = definir_billetes()
    billetes.sort(reverse=True)
    devolucion = 0
    while devolucion == 0:
        importe = int(input("Ingrese el importe a retirar: "))
        devolucion = devolucion_billetes(importe,billetes)
        print(dict(devolucion))
main()
