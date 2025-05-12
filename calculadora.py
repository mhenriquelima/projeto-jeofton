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

def is_input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('insira um número válido.')
def is_input_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('insira um número válido.')
            


