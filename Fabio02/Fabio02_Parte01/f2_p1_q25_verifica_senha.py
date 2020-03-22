def main():
    senha = int(input("Digite a senha: "))

    senha_verificada = verifica_senha(senha)
    print(senha_verificada)

def verifica_senha(s):
    senha_certa = 1234
    if s == senha_certa:
        return "Acesso permitido!"
    else:
        return "Acesso negado!"


main()