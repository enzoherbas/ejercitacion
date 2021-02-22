i = int(input("Dame el valor de i para probar si es Fizzbuzz, Fizz o Buzz: "))

if 0==i%3 and 0==i%5:
        print("FizzBuzz")
elif 0==i%3 and 0!=i%5:
        print("Fizz")
elif 0!=i%3 and 0==i%5:
        print("Buzz")
else :
    print(i)
