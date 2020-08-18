def main():
    a0 = int(input('Digite o A0: '))
    limite = int(input('Digite o limite: '))
    r = int(input('Digite o R: '))

    mostra_termos_PA(a0, limite, r)


def mostra_termos_PA(a, l, r):
    contador = 1
    
    while contador <= l:
        termo = a + (contador - 1) * r

        if termo < l:
            print(termo)

            contador += 1

        else:
            break


main()