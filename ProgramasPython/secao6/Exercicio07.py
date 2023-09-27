#entrada
num1 = int(input('Informe o número 1: '))
num2 = int(input('Informe o número 2: '))
num3 = int(input('Informe o número 3: '))
num4 = int(input('Informe o número 4: '))
#processamento
q1 = num1 ** 2
q2 = num2 ** 2
q3 = num3 ** 2
if q3 >= 1000:
    print(f'O quadrado de {num3} é maior ou igual a mil e é de {q3}. Programa encerrado.')
else:
    q4 = num4 ** 2
    print(f'O valor ao quadrado de {num1} é de {q1}')
    print(f'O valor ao quadrado de {num2} é de {q2}')
    print(f'O valor ao quadrado de {num3} é de {q3}')
    print(f'O valor ao quadrado de {num4} é de {q4}')
    