'''Ingresar numeros y alcanzar un tope'''

def ingresar_numero():
    '''INGRESO LOS NUMEROS'''
    ingreso = int(input("Ingresar un numero: "))
    return ingreso

def selector_min(lista,tope):
    '''ELIJO EL TOPE DE LA SUMA'''
    if sum(lista) <= tope :
        print("La suma de la lista no es superior a", tope)
        finalizar = 0
    else:
        print("El numero mas chico de los ingresados es ", min(lista))
        finalizar = 1
    return finalizar

def listar_numeros(listado_previo):
    '''LISTO LOS NUMEROS PARA PODER SUMARLOS POSTERIORMENTE'''
    continuar = 1
    while continuar == 1:
        listado_previo.append(ingresar_numero())
        continuar = input("Si desea seguir agregando numeros ingrese 1,sino ingrese cualquier otro")
    return listado_previo

def main ():
    '''INGRESO TODAS LAS FUNCIONES EN ORDEN'''
    tope = int(input("Elegir el numero a alcanzar con la suma de valores: "))
    listado_numeros = []
    listado_numeros = listar_numeros(listado_numeros)
    finalizar = 0
    while finalizar == 0:
        finalizar = selector_min(listado_numeros,tope)
        if finalizar == 0:
            listado_numeros = listar_numeros(listado_numeros)
main()
