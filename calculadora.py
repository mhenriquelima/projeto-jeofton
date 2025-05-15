def soma(a,b):
    resultado = a + b
    historico.append(f'{n1} + {n2} = {resultado}')
    return resultado

def sub(a,b):
    resultado = a - b
    historico.append(f'{n1} - {n2} = {resultado}')
    return resultado

def mult(a,b):
    resultado = a * b
    historico.append(f'{n1} * {n2} = {resultado}')
    return resultado

def div(a,b):
    if n2 == 0:
        resultado = 'Operação inválida.'
        return resultado
    else:
        resultado = a / b
        historico.append(f'{n1} / {n2} = {resultado}')
        return resultado

def pot(a,b):
    resultado = a ** b
    historico.append(f'{n1} ^ {n2} = {resultado}')
    return resultado

def raiz(a,b):
    if b == 0:
        resultado = 'Operação inválida.'
    elif a < 0 and b % 2 == 0:
        resultado = 'Operação inválida.'
    else:
        resultado = a ** (1 / b)
        historico.append(f'{n2}√ {n1} = {resultado}')
    return resultado
        
def is_input_float(prompt):
    while True:
        user_input = input(prompt)
        if user_input.upper() == 'R':
            reset_calculator()
            return None
        try:
            return float(user_input)
        except ValueError:
            print('insira um número válido.')

def is_input_integer(prompt):
    while True:
        user_input = input(prompt)
        if user_input.upper() == 'R':
            reset_calculator()
            return None
        try:
            return int(user_input)
        except ValueError:
            print('insira um número válido.')

def reset_calculator():
    global historico, n1, n2, is_running
    print('Calculadora reiniciada.')
    historico.clear()
    n1 = 0
    n2 = 0
    is_running = True

is_running = True
historico = []
n1 = 0
n2 = 0

while is_running == True:
    selected_operation = is_input_integer('''
    Bem vindo a calculadora
        Escolha uma opção:
        1 - Soma
        2 - Subtração   
        3 - Multiplicação
        4 - Divisão
        5 - Potenciação
        6 - Raiz
        7 - Histórico
        8 - Sair
> ''')
    if selected_operation is None:
        continue

    if 1 <= selected_operation <= 6:
        n1 = is_input_float('Digite o primeiro número > ')
        if n1 is None:
            continue
        n2 = is_input_float('Digite o segundo número > ')
        if n2 is None:
            continue
        
        operations = {
            1: soma,
            2: sub,
            3: mult,
            4: div,
            5: pot,
            6: raiz
        }
        resultado = operations[selected_operation](n1, n2)
        print(f'O resultado é: {resultado}')
    elif selected_operation == 7:
        print(historico)
        if input('Deseja apagar o histórico? [0] > ') == '0':
            historico.clear()
            print('Histórico apagado.')
        else:
            print('Histórico mantido.')
    elif selected_operation == 8:
        is_running = False
        print('Programa encerrado.')
    else:
        print('Opção inválida.')