print("Ingresa la hora del comienzo del intervalo.")

horas1 = int(input("Ingresar las horas: "))

minutos1 = int(input("Ingresar los minutos: "))

segundos1 = int(input("Ingresar los segundos: "))

print("Ingresa la hora del fin del intervalo.")

horas2 = int(input("Ingresar las horas: "))

minutos2 = int(input("Ingresar los minutos: "))

segundos2 = int(input("Ingresar los segundos: "))

horas1 *= 3600

minutos1 *=60

seg1= horas1 + minutos1 + segundos1

horas2 *= 3600

minutos2 *=60

seg2= horas2 + minutos2 + segundos2

total = seg2 - seg1

print("Los segundos totales desde el comienzo al final del intervalo son " + str(total))
        





