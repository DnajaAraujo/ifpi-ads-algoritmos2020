def main():
    numero = int(input("Digite um número maior ou igual a dois: "))
    calcula_fibonacci(numero)


def calcula_fibonacci(n):
    a = 0
    b = 0
    contador = 1

    while (contador <= n) and (n >= 2):
        print(b)
        b = b + a
        a = b - a
                
        if b == 0:
            b += 1
                
        contador += 1


main()