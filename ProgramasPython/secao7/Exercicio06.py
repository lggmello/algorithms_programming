#entrada
tab = int(input('Informe a tabuada desejada: '))
#processamento
while tab < 1 or tab > 10:
    print('A tabuada desejava DEVE ser um número inteiro entre 1 e 10.')
    tab = int(input('Informe a tabuada desejada: '))
print(f'Tabuada de {tab}: ')
for i in range(1, 11):
    a = tab * i
    print(f'{tab} x {i} = {a}')
    