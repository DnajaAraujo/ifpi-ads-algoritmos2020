def main():
    numero = int(input('Digite um número: '))
    mostra_soma(numero)


def mostra_soma(numero):
    total = 0
    
    for i in range(numero + 1):
        if i <= numero:
            total += i
        else:
            break

    print('Soma total: {}'.format(total)) 


main()