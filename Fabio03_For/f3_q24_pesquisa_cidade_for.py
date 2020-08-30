def main():
    numero_habitantes = int(input('Digite o número de habitantes: '))
    realiza_pesquisa(numero_habitantes)


def realiza_pesquisa(numero_habitantes):
    salario_total = 0
    filhos_total = 0
    salario_mil = 0 

    for i in range(1, numero_habitantes + 1):
        salario = float(input('Digite o salário: R$ '))
        numero_filhos = int(input('Digite o número de filhos: '))
        
        if salario <= 1000:
            salario_mil += 1
        
        salario_total += salario
        filhos_total += numero_filhos

    calcula_resultados(numero_habitantes, salario_total, filhos_total, salario_mil)


def calcula_resultados(numero_habitantes, salario_total, filhos_total, salario_mil):
    media_salario = salario_total / numero_habitantes
    media_filhos = filhos_total / numero_habitantes
    percentual_mil = (salario_mil / numero_habitantes) * 100

    mostra_resultados(media_salario, media_filhos, percentual_mil)


def mostra_resultados(media_salario, media_filhos, percentual_mil):
    print('-'*30)
    print('Salário médio: R$ {:.2f}'.format(media_salario))
    print('Média de filhos: {:.1f}'.format(media_filhos))
    print('Pessoas com salário de até mil reais: {:.1f}% '.format(percentual_mil))
    print('-'*30)


main()