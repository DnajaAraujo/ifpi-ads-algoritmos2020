def main():
    print("Equação do 2º grau")
    print("---------------------")
    print("aX^2 + bX + c = 0")
    print("---------------------")
    
    a = float(input("Digite um número a: "))
    b = float(input("Digite um número b: "))
    c = float(input("Digite um número c: "))
    print("---------------------")

    raizes = encontra_raizes(a, b, c)
    print(raizes)


def encontra_raizes(a, b, c):
    delta = (b**2) - (4*a*c)
    x1 = (-b + (delta ** 0.5)) / 2*a
    x2 = (-b - (delta ** 0.5)) / 2*a

    if a == 0:
        return "Erro: 'a' igual a 0."
    else:
        return f"As raízes dessa equação do 2º grau são: {x1:.1f} e {x2:.1f}."



main()
