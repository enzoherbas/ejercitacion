n = int(input('Introduce un entero positivo: '))

m = []

for i in range(n):

	fila = []

	for j in range(n):

		val = 1 if i==j else 0

		fila.append(val)

	m.append(fila)

print (m)
