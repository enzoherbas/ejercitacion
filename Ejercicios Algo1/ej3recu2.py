'''BALDOSAS'''
from random import choice
INICIALES_COLORES = ["B","N","G"]
BALDOSAS_COLOREDAS = {INICIALES_COLORES[0]:"Blanco",INICIALES_COLORES[1]:"Negro",INICIALES_COLORES[2]:"Gris"}

def crear_camino_incompleto ():
    '''
    PRE:
    POST: Creo el camino en manera de LISTA, ingresando cada baldosa e ingresandole un COLOR.
          Previamente los colores ya estan definidos por consigna.
    '''
    camino_incompleto = input('''
    B) Blanco
    N) Negro
    G) Gris
    R) Removido (Posicion sin baldosa)
    Ingresar los colores de las baldosas del camino(todo junto): 
    ''').upper()
    return list(camino_incompleto)

def terminar_camino (baldosas):
    '''PRE: INGRESO EL CAMINO DE BALDOSAS INCOMPLETO PARA PODER LLENARLO.
       POST: RETORNA EL CAMINO CON LAS BALDOSAS SIN SER IGUALES UNA DE LA SIGUIENTE.'''
    print(baldosas)
    tamanio_camino = len(baldosas)
    if baldosas[0] == 'R':
        baldosas[0] = choice(INICIALES_COLORES)
        while baldosas[0] == baldosas[1]:
            baldosas[0] = choice(INICIALES_COLORES)
    for baldosa in range(1,tamanio_camino-1):
        if baldosas[baldosa] == 'R':
            baldosas[baldosa] = choice(INICIALES_COLORES)
            while baldosas[baldosa] == baldosas[baldosa-1] or baldosas[baldosa] == baldosas[baldosa+1]:
                baldosas[baldosa] = choice(INICIALES_COLORES)
    if baldosas[tamanio_camino-1] == 'R':
        baldosas[tamanio_camino-1] = choice(INICIALES_COLORES)
        while baldosas[tamanio_camino-1] == baldosas[tamanio_camino-2]:
            baldosas[tamanio_camino-1] = choice(INICIALES_COLORES)
    return baldosas

def main ():
    '''CREO EL CAMINO INCOMPLETO, LO INGRESO A LA FUNCION PARA TERMINAR DE CREARLO
        Y POSTERIORMENTE LO IMPRIMO'''
    camino_incompleto = crear_camino_incompleto()
    camino_completo = terminar_camino(camino_incompleto)
    for baldosa in camino_completo:
        print(BALDOSAS_COLOREDAS[baldosa])

main()
