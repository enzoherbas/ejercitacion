def fibonacci(n):   
    a = 0
    b = 1
    if n >= 1:
        while a < n:
            aux = a + b
            a = b
            b = aux
    else:
        aux = 0
    return aux

def pasaje_hexadecimal (digito):
    decimal = digito
    digitos_hexadecimal = {10: "A", 11: "B", 12:"C", 13:"D",14:"E",15:"F"}
    if decimal >= 10:
        decimal = digitos_hexadecimal[digito]
    return decimal
      
def telefono ():
    numero = input("Ingresar el numero de telefono: ")
    numero_listado = [int(x) for x in list(numero)]
    hexadecimal = []
    for x in numero_listado:
        hexadecimal.append(pasaje_hexadecimal(fibonacci(x)))
    hexadecimal = [str(x) for x in hexadecimal]
    print("".join(hexadecimal))

def main ():
    telefono()

main()
