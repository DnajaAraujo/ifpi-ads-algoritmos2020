import math

def estimate_pi():
    k = 0
    total = 0
    numero = (2*(2**(1/2))) / 9801

    while True:
        numerador = (math.factorial(4*k)) * (1103 + (26390*k))
        denominador = (math.factorial(k)**4) * (396**(4*k))
        ultimo_numero = numero * (numerador / denominador)
        total += ultimo_numero
        
        
        if abs(ultimo_numero) < 1e-15:
            break
    
        k += 1
    
    
    print(1/total)
    #print(math.pi)

    
estimate_pi()  
        