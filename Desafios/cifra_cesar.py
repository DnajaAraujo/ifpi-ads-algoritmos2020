def main():
    palavra = input('Digite uma palavra: ')
    chave = int(input('Digite um número: '))

    rotate_word(palavra, chave)


def rotate_word(palavra, chave):

    if valida_chave(chave):
        nova_palavra = palavra.lower()

        cifrada = ''
        for letra in nova_palavra:
            indice = ord(letra)
            novo_indice = indice + chave

            if novo_indice > 122:
                novo_indice -= 122
                novo_indice += 96
            
            if novo_indice < 97:
                novo_indice += 122
                novo_indice -= 96

            nova_letra = chr((novo_indice))
            cifrada += nova_letra

        mostra_resultado(palavra, cifrada)

    else:
        print('Chave inválida!')


def valida_chave(chave):
    if chave > 25 or chave < -25:
        return False
    else:
        return True


def mostra_resultado(palavra, cifrada):
    if palavra == palavra.upper():
        print(cifrada.upper())
    else:
        print(cifrada)


main()