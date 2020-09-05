def main():
    mensagem = input('Digite a mensagem: ')
    chave = int(input('Digite um número: '))

    rotate_word(mensagem, chave)


def rotate_word(mensagem, chave):

    if valida_chave(chave):
        nova_mensagem = mensagem.lower()

        cifrada = ''
        for caractere in nova_mensagem:
            indice = ord(caractere)

            if (indice >= 65 and indice <= 90) or (indice >= 97 and indice <= 122):
                novo_indice = indice + chave

                if novo_indice > 122:
                    novo_indice -= 122
                    novo_indice += 96
                
                if novo_indice < 97:
                    novo_indice += 122
                    novo_indice -= 96
            
            else:
                novo_indice = indice
        
            novo_caractere = chr(novo_indice)
            cifrada += novo_caractere

        mostra_resultado(mensagem, cifrada)

    else:
        print('Chave inválida!')


def valida_chave(chave):
    if chave > 25 or chave < -25:
        return False
    else:
        return True


def mostra_resultado(mensagem, cifrada):
    if mensagem == mensagem.upper():
        print(cifrada.upper())
    else:
        print(cifrada)


main()
