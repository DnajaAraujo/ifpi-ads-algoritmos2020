def main():
    numero1 = int(input("Digite um número inteiro: "))
    numero2 = int(input("Digite um outro número inteiro: "))

    resto0 = calcula_resto(numero1, numero2)
    print(resto0)



def calcula_resto(n1, n2):
    resto = n1 % n2
    if resto == 1:
        resultado = (n1 + n2) + resto
        return f"({n1} + {n2}) + {resto} = {resultado}"
    elif resto == 2:
        if (n1 % 2 == 0) and (n2 % 2 == 0):
            return f"{n1} e {n2} são pares."
        elif (n1 % 2 == 0) and (n2 % 2 != 0):
            return f"{n1} é par e {n2} é ímpar."
        elif (n1 % 2 != 0) and (n2 % 2 == 0):
            return f"{n1} é ímpar e {n2} é par."
        else:
            return f"{n1} e {n2} são ímpares."
    elif resto == 3:
        resultado = (n1 + n2) * n1
        return f"({n1} + {n2}) x {resto} = {resultado}"
    elif resto == 4:
        if (n1 != 0):
            return "Erro: Divisão por zero."
        resultado = (n1 + n2) / n1
        return f"({n1} + {n2}) x {resto} = {resultado}"
    else:
        return f"{n1}^2 = {n1 ** 2}\n{n2}^2 = {n2 ** 2}"



main()

