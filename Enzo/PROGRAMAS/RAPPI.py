print("==========================")
print("Calculador de vacaciones")
print("==========================")

nombre = input("Por favor introduzca su nombre :")
apellido = input("Por favor introduzca su apellido :")
x = int(input("Introduzca su clave con respecto a su area.\n(1)Si es Atencion al Cliente.\n(2)Si es Logistica.\n(3)Si es Gerencia.\n"))
y = float(input("Introduzca sus años de antiguedad:"))

if x==1:
        if y<1 :
                print(nombre + " " + apellido + " Su tiempo es menor a un año. No le corresponde vacaciones")
        if y==1:
                print(nombre + " " + apellido + " Su area de clave 1, con 1 año de antiguedad le corresponde 6 dias de vacaciones.")
        if y>=2 and y<=6:
                print(nombre + " " + apellido + " Su area de clave 1, con " + str(y) +" años de antiguedad le corresponde 14 dias de vacaciones.")
        if y>7:
                print(nombre + " " + apellido + " Su area de clave 1, con " + str(y) +" años de antiguedad le corresponde 20 dias de vacaciones.")
if x==2:
        if y<1 :
                print(nombre + " " + apellido + " Su tiempo es menor a un año. No le corresponde vacaciones")
        if y==1:
                print(nombre + " " + apellido + " Su area de clave 2, con 1 año de antiguedad le corresponde 7 dias de vacaciones.")
        if y>=2 and y<=6:
                print(nombre + " " + apellido + " Su area de clave 2, con " + str(y) +" años de antiguedad le corresponde 15 dias de vacaciones.")
        if y>7:
                print(nombre + " " + apellido + " Su area de clave 2, con " + str(y) +" años de antiguedad le corresponde 22 dias de vacaciones.")
                      
if x==3:
        if y<1 :
                print(nombre + " " + apellido + " Su tiempo es menor a un año. No le corresponde vacaciones")
        if y==1:
                print(nombre + " " + apellido + " Su area de clave 3, con 1 año de antiguedad le corresponde 10 dias de vacaciones.")
        if y>=2 and y<=6:
                print(nombre + " " + apellido + " Su area de clave 3, con " + str(y) +" años de antiguedad le corresponde 20 dias de vacaciones.")
        if y>7:
                print(nombre + " " + apellido + " Su area de clave 3, con " + str(y) +" años de antiguedad le corresponde 30 dias de vacaciones.")
else:
    print("Ingreso una clave de area incorrecta")
