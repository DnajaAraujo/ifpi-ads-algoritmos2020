from existe_tipo import *

def main():
    num_caracteres = int(input('Digite o número de caracteres: '))
    senha = input('Digite a senha: ')

    verifica_senha(num_caracteres, senha)


def verifica_senha(num_caracteres, senha):
    if valida_tamanho(num_caracteres, senha):
        if not valida_senha(num_caracteres, senha):
            complemento = 0

            if num_caracteres < 6:
                complemento = 6 - len(senha)

            else:
                if existe_numero(senha):
                    complemento += 1
                if existe_upper(senha):
                    complemento += 1
                if existe_lower(senha):
                    complemento += 1
                if existe_special_character(senha):
                    complemento += 1
                
                if complemento == 0:
                    complemento = 4
                elif complemento == 1:
                    complemento = 3
                elif complemento == 2:
                    complemento = 2
                elif complemento == 3:
                    complemento = 1

            print('Faltam {} caracteres para tornar essa senha forte.'.format(complemento))
        else:
            print('Essa senha já é forte!')
    else:
        print('Número de caracteres incompatível com a senha!')


def valida_senha(num_caracteres, senha):
    if num_caracteres >= 1 and num_caracteres <= 100:
        n = existe_numero(senha)
        u = existe_upper(senha)
        l = existe_lower(senha)
        s = existe_special_character(senha)

        return n and u and l and s and len(senha) >= 6


def valida_tamanho(num_caracteres, senha):
    return num_caracteres == len(senha)
    

main()