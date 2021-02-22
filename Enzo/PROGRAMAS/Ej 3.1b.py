seg = int(input("ingresar los segundos totales del intervalo: "))

horas = seg//3600

seg %= 3600

minutos = seg//60

seg %= 60

print ( horas , minutos, seg )

