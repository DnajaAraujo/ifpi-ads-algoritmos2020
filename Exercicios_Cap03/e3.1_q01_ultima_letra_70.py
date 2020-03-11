def main():
    palavra = input("Digite uma palavra: ")
    tam_linha = int(input("Digite o tamanho da linha: "))

    resposta = right_justify(palavra, tam_linha)

    print("linha formatada:\n{}".format(resposta))

def right_justify(s, tam_espaco):
    tam_palavra = len(s)

    quant_espaco = tam_espaco - tam_palavra
    espacos = quant_espaco * ' '
    linha = espacos + s

    return linha
    

main()

