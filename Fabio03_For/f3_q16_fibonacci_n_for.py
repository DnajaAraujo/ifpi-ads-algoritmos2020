def main():
    numero = int(input("Digite um número maior ou igual a dois: "))
    calcula_fibonacci(numero)


def calcula_fibonacci(numero):
    a = 0
    b = 0

    for i in range(1, numero + 1):
        if numero >= 2:
            print(b)
            b = b + a
            a = b - a
                    
            if b == 0:
                b += 1
                

main()