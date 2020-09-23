def palavras_com_letra_em_ordem_alfabetica():
    print('>> Palavras com letras em ordem alfabetica \n')
    arquivo = open('words.txt')

    for linha in arquivo:
        palavra = linha.strip()
        if is_abecedarian(palavra):
            print(palavra)

    arquivo.close()


def is_abecedarian(palavra):
    anterior = palavra[0]

    for letra in palavra:
        if letra < anterior:
            return False
        anterior = letra

    return True