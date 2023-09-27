#entrada
n = int(input('Digite um número inteiro: '))
#processamento
if n % 2 == 0:
    print('Número par')
else:
    print('Número impar')
if n > 0:
    print('Número positivo.')
elif n == 0:
    print('Número neutro.')
else:
    print('Número negativo.')
