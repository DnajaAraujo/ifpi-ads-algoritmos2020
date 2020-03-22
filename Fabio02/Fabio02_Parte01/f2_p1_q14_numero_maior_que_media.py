def main():
    numero1 = int(input("Digite um número inteiro: "))
    numero2 = int(input("Digite um outro número inteiro: "))
    numero3 = int(input("Digite um outro número inteiro: "))
    numero4 = int(input("Digite um outro número inteiro: "))
    numero5 = int(input("Digite um outro número inteiro: "))

    maiores = maior_que_media(numero1, numero2, numero3, numero4, numero5)
    print(maiores)


def maior_que_media(n1, n2, n3, n4, n5):
    media = (n1 + n2 + n3 + n4 + n5) / 5
    maior1 = ""
    maior2 = ""
    maior3 = ""
    maior4 = ""
    maior5 = ""
    
    if n1 > media:
        maior1 = str(n1) + "\n"
    if n2 > media:
        maior2 = str(n2) + "\n"
    if n3 > media:
        maior3 = str(n3) + "\n"
    if n4> media:
        maior4 = str(n4) + "\n"
    if n5 > media:
        maior5 = str(n5)
    if (n1 <= media) and (n2 <= media) and (n3 <= media) and (n4 <= media) and (n5 <= media):
        return "Nenhum dos números digitados é maior que a média."
    
    return f"Números maiores que a média:\n{maior1}{maior2}{maior3}{maior4}{maior5}"




main()