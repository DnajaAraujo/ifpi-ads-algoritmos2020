def palavras_com_mais_de_20_letras():
    print('>> Palavras com + de 20 letras \n')
    arquivo = open('words.txt')

    for linha in arquivo:
        palavra = linha.strip()
        if len(palavra) > 20:
            print(palavra)

    arquivo.close()