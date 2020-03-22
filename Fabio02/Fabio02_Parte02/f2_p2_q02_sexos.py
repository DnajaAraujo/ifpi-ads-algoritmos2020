def main():
    print("---Defina o seu sexo---")
    sexo = input("Digite M para masculino ou F para feminino: ")

    sexo_verificado = verifica_sexo(sexo)
    print(sexo_verificado)



def verifica_sexo(s):
    if s == "M" or s =="m":
        return "O sexo escolhido foi o masculino."
    elif s == "F" or s == "f":
        return "O sexo escolhido foi o feminino."
    else:
        return "Sexo inválido!"



main()