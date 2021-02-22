x = int(input("Elegi \n 1 Para pasar de letras a numeros\n 2 Pasar de numero a Letras.\n:"))

if x==1:
        print ("Dame un numero y te lo muestro escrito en letras (solo del 1 al 5)")

        x = int(input("Cual es el numero que queres transformar? :"))

        if x == 1:
                print("Uno")
        
        elif x==2:
                print("Dos")
        
        elif x==3:
                print("Tres")

        elif x==4:
                print("Cuatro")

        elif x==5:
                print("Cinco")
        else:
                print("Valor de 1 a 5 en ENTEROS, PELOTUDE")
elif x==2:

        print ("Dame un numero y te lo muestro escrito en numeros(solo del 1 al 5)")

        x = (input("Cual es el numero que queres transformar? :"))
        x = x.lower()

        if x == "uno":
                print("1")
        
        elif x== "dos":
                print("2")
        
        elif x== "tres" :
                print("3")

        elif x== "cuatro" :
                print("4")

        elif x== "cinco" :
                print("5")
        else:
                print("Valor de 1 a 5 ENTEROS, PELOTUDE")
else:
        print("1 O 2 PELOTUDE")
    
        
                
