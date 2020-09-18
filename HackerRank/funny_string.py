def main():
    num_string = int(input('Digite o número de vezes que deseja digitar: '))
    verifica_string(num_string)


def verifica_string(num_string):
    if valida_num_string(num_string):
        for i in range(num_string):
            string = input('Digite a string: ')

            if valida_string(string):
                if diferenca_absoluta(string) == diferenca_absoluta(inverte_string(string)):
                    print('Funny')
                else:
                    print('Not funny')
               
            else:
                print('String digitada inválida!')
    else:
        print('Número de vezes inválido!')

        
def diferenca_absoluta(string):
    diferenca = ''
    for i in range(len(string)-1):
        operacao = ord(string[i]) - ord(string[i+1])
        diferenca += str(abs(operacao))

    return diferenca


def inverte_string(string):
    nova_string = ''
    for i in range(len(string)-1, -1, -1):
        nova_string += string[i]

    return nova_string


def valida_string(string):
    tamanho = len(string)
    return tamanho >= 2 and tamanho <= 10000


def valida_num_string(num_string):
    return num_string >= 1 and num_string <= 10


main()