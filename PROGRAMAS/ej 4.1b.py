x = int(input("Ingresa un numero para ver si es PRIMO o COMPUESTO: "))

if x > 1:
    
    cont=0
    
    for num in range (2,x):

            resto = x%num

            if resto == 0:

                cont+=1
    if cont == 0:
        print ("El {} es un numero primo." .format(x))
    
    else:
        print ("El {} es un numero compuesto" .format(x))

else:
    print("El 1 es un numero primo")
