f = float ( input ("Dame el valor de una temperatura en grados Fahrenheit para pasarlo a Celsius: "))

for f in range (0, 11):
        c = 5/9*((f*10)-32)
        print (str(f*10),"El valor en celsius es " + str(c))
