CODIGOS_CREMAS = [100,200,300,400,10]
TIPOS_CREMAS =  {CODIGOS_CREMAS[0]:"Humectante clásica",CODIGOS_CREMAS[1]:"Antiage colageno",CODIGOS_CREMAS[2]:"Facial con UV",CODIGOS_CREMAS[3]:"Desmaquillante",CODIGOS_CREMAS[4]:"Vitamina A"}
MEDIDAS_ENVASES = {1:200, 2:500, 3:1000}
def indicar_volumen_tanques ():
    carga_de_tanques = []
    for contador in CODIGOS_CREMAS:
        medida_tanque = int(input("Ingresar la cantidad en CM3 de {0} que hay disponible de materia prima".format(TIPOS_CREMAS[contador])))
        tipo_tanque = contador,medida_tanque
        carga_de_tanques.append(tipo_tanque)
    print(carga_de_tanques)
    tanques_llenos = dict(carga_de_tanques)
    return tanques_llenos
def envasar_cremas (codigo,tanques,envases_usados,materia_prima_usada):
    produccion_cremas = []
    continuar = "si"
    materia_prima_total = 0
    while continuar ==  "si":
        elegir_envase = int(input('''
    1) Envase de 200 CM3
    2) Envase de 500 CM3
    3) Envase de 1000CM3
    Ingresar que envase desea usar:
                            '''))
        cantidad_envases = int(input("Ingresar la cantidad que desea de envases de {0}CM3".format(MEDIDAS_ENVASES[elegir_envase])))
        envases = [elegir_envase, cantidad_envases]
        produccion_cremas.append(envases)
        materia_prima_total += MEDIDAS_ENVASES[elegir_envase] * cantidad_envases
        continuar = input("Desea seguir ingresando otro tipo de envases? Ingrese SI o NO").lower()
        if materia_prima_total > tanques[codigo]:
            print("La materia prima necesaria es superior a la que hay en el tanque la cual es: {0}".format(tanques[codigo]))
            eleccion = int(input("Ingrese 1 si desea volver a ingresar un pedido o 2 para cambiar a otra crema."))
            materia_prima_total = 0
            produccion_cremas = []
            if eleccion == 2:
                continuar = "no"
        else:
            for x in range (len(produccion_cremas)-1):
                for y in produccion_cremas[x]:
                    print(produccion_cremas)
                    envases_usados[y] += produccion_cremas[x][y]
            materia_prima_usada[codigo] += materia_prima_total
            tanques[codigo] -= materia_prima_total
    return envases_usados, materia_prima_usada, tanques
def main ():
    tanques_cargados = indicar_volumen_tanques()
    envases_usados = {1:0,2:0,3:0}
    materia_prima_usada = {100:0,200:0,300:0,400:0,10:0}
    finalizar = "no"
    while finalizar == "no":
        elegir_crema_codigo = int(input("Ingrese el codigo de la crema que desea usar: "))
        envases_usados, materia_prima_usada, tanques_cargados = envasar_cremas(elegir_crema_codigo,tanques_cargados,envases_usados,materia_prima_usada)
        finalizar = input("Ingrese SI para finalizar el cargado de cremas, o NO para continuar: ").lower()
        print(materia_prima_usada)
    print("La materia prima usada en mayor medida fue", TIPOS_CREMAS)
    print("El envase que mas se produjo en general fue:", max(envases_usados.values()))
    for x in CODIGOS_CREMAS:
        print(tanques_cargados[x])
main()
