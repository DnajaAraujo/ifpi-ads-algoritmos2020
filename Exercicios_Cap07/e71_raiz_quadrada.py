import math

def mysqrt(a):
    x = 1.0
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return x



def test_square_root(num, num2):

    print('a   ',end='')
    print('mysqrt(a)     ',end='')
    print('math.sqrt(a)  ',end='')
    print('diff')
    print('-   ',end='')
    print('---------     ',end='')
    print('------------  ',end='')
    print('----')

    while True:
        sqrt1 = mysqrt(num)
        sqrt2 = math.sqrt(num)
        
        if (num <= num2):
            print('{:.1f} '.format(num),end='')
            
            if (sqrt1 == int(sqrt1)):
                print('{}           '.format(sqrt1),end='')
            else:
                print('{:.11f} '.format(sqrt1),end='')
            #----------------------------------------------
            if (sqrt2 == int(sqrt2)):
                print('{:.1f}           '.format(sqrt2),end='')
            else:
                print('{:.11f} '.format(sqrt2),end='')
            #---------------------------------------------
            print('{}'.format(abs(sqrt2 - sqrt1)))

            num += 1

        else:
            break



def main():
    primeiro = int(input('Digite o primeiro número da tabela (obs.: não pode ser zero!): '))
    ultimo = int(input('Digite o último número da tabela: '))
    test_square_root(primeiro, ultimo)


main()


