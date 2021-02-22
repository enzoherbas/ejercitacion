f = int(input("ingresar un valor :"))

y = 0

for x in range (0 , f+1):

            y = x

            if x == y:

                for x in range (y, f+1):

                        print(str(y) + "|" + str(x))
