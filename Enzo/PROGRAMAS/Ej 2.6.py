x = int(input("Ingresa el primer valor: "))
y = int(input("Ingresa el segundo valor: "))


if ( x < y ):
        for z in range (x + 1, y):

            j = z

            z %= 2

            if (z==0):

                print(j)

if ( y < x ):
        for z in range (y + 1, x):

            j = z

            z %= 2

            if (z==0):

                print(j)
