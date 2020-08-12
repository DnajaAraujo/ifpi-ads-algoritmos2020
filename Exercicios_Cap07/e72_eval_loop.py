import math

def eval_loop():
    ultima_entrada = ''
    
    while True:
        entrada = input('Digite uma entrada: ')
        
        if (entrada == 'done'):
            print(ultima_entrada)
            break
        
        else:
            ultima_entrada = eval(entrada)
            print(ultima_entrada)


eval_loop()