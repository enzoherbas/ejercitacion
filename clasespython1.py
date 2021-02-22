contador_desaprobados = 0
alumnos_totales = 0
contador_alumnos = 0
for curso in range (1,6):
    alumnos_totales += contador_alumnos
    primero = False
    contador_alumnos = 0
    nota_primer_aprobado = 0
    total_notas=0
    contador_nota_primer_aprobado = 0
    seguir = "si"
    
    while seguir != "no" :
        
        padron = int(input("Ingresar el padron del alumno : "))
        nota = int(input("Ingresar la nota del alumno : "))
        contador_alumnos += 1
        total_notas += nota 
        
        if nota >=4:
            while primero == False:
                nota_primer_aprobado = nota
                primer_aprobado = padron
                primero = True 
            if nota == nota_primer_aprobado:
                contador_nota_primer_aprobado += 1
                
        elif nota < 4:
            contador_desaprobados += 1
        seguir = input("Desea seguir ingresando alumnos? (si/no)")
        if seguir == "no":
            promedio = total_notas / contador_alumnos
            
            if nota_primer_aprobado == 0:
                print("No hubo aprobados en el curso")
                print("El promedio general de la catedra es: " + str(promedio))
            else:
                print("El alumno de padron "+ str(primer_aprobado) + ". Fue el primer aprobado del curso")
                print(str(contador_nota_primer_aprobado) + " alumnos, obtuvieron la misma calificacion.")
                print("El promedio general de la catedra es: " + str(promedio))
            
porcentaje_desaprobados = (contador_desaprobados * 100) / alumnos_totales

print("El porcentaje de reprobados general de todas las cátedras es :" + str(porcentaje_desaprobados))

    
            


        
            
    

