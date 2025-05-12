def soma(a,b):
    resultado = a + b
    return resultado

def sub(a,b):
    resultado = a - b
    return resultado

def mult(a,b):
    resultado = a * b
    return resultado

def div(a,b):
    if n2 == 0:
        resultado = 'Operação inválida.'
        return resultado
    else:
        resultado = a / b
        return resultado
    
def pot(a,b):
    resultado = a ** b
    return resultado
    
def raiz(a,b):
    resultado = a ** (1/b)
    return resultado

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))