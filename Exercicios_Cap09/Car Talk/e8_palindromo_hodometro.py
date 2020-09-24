def valida_numero():
    print('>> Car Talk: Palíndromo no hodômetro \n')
    i = 100000

    while i <= 999999:
        if valida_i(i):
            print(i)
        i += 1


def valida_i(i):
    return (eh_palindromo(i, 2, 6) and
        eh_palindromo(i+1, 1, 6) and
        eh_palindromo(i+2, 1, 5) and 
        eh_palindromo(i+3, 0, 6))


def eh_palindromo(i, inicio, fim):
    resultado = str(i)
    resultado = resultado[inicio : fim]
    
    return resultado[::-1] == resultado


valida_numero()

