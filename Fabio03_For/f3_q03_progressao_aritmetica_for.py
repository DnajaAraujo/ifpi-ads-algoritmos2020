def main():
    a = int(input('Digite o A0: '))
    limite = int(input('Digite o limite: '))
    r = int(input('Digite o R: '))

    mostra_PA(a, limite, r)


def mostra_PA(a, limite, r):
    for i in range(1, limite):
        termo = a + (i - 1) * r
        
        if termo < limite:
            print(termo)
        else:
            break


main()