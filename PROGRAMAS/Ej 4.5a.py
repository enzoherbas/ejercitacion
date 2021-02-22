año = int(input("Ingresar un año para saber si es bisiesto o no: "))

x = año%4

y = año%400

z = año%100

if x == 0:

    if x == z:

        if x == y:   
            print ("El año es bisiesto")
                
        else:
            print ("El año es normal")
                
    else:      
        print("El " + str(año) + " es bisiesto")
        

    

    
