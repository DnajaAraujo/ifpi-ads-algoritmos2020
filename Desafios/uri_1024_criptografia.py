def main():
    linhas = int(input('Digite a quantidade de linhas: '))
    rotate_message(linhas)


def rotate_message(linhas):

    if valida_linhas(linhas):
        for i in range(linhas):
            mensagem = input('Digite a mensagem: ')
            
            nova_mensagem = ''
            if valida_mensagem(mensagem):
                for caractere in mensagem:
                    indice = ord(caractere)

                    if (indice >= 65 and indice <= 90) or (indice >= 97 and indice <= 122):
                        indice = ord(caractere) + 3
                        novo_caractere = chr(indice)
                        nova_mensagem += novo_caractere

                    else:
                        nova_mensagem += caractere
            
                inverte_mensagem(nova_mensagem)
            
            else:
                print('Número de caracteres inválido!')
    
    else:
        print('Número de linhas inválido!')


def inverte_mensagem(nova_mensagem):
    nova_mensagem2 = nova_mensagem[::-1]
    rotate_message2(nova_mensagem2)


def rotate_message2(nova_mensagem2):
    nova_mensagem3 = ''
    tamanho = len(nova_mensagem2)

    for i in range(tamanho):
        if i >= (tamanho // 2):
                novo_indice = ord(nova_mensagem2[i]) - 1
                novo_caractere = chr(novo_indice)
                nova_mensagem3 += novo_caractere

        else:
            novo_caractere = nova_mensagem2[i]
            nova_mensagem3 += novo_caractere

    print(nova_mensagem3)


def valida_linhas(linhas):
    if linhas >= 1 and linhas <= 1*(10**4):
        return True
    else:
        return False


def valida_mensagem(mensagem):
    qtd_caractere = len(mensagem)

    if qtd_caractere >= 1 and qtd_caractere <= 1*(10**3):
        return True
    else:
        return False


main()
