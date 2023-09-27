#variaveis
identificador = 1
s1 = 0
s2 = 0
s3 = 0
s4 = 0
#entrada
while identificador != 0:
    identificador = input('Informe o ID do mouse: ') 
    print('Informe um número de 0 a 4, de acordo com a situação do mouse, sendo: ')
    print('    1- Necessita da esfera')
    print('    2- Necessita de limpeza')
    print('    3- Necessita de troca de cabo ou conector')
    print('    4- Quebrado ou inutilizado')
    print('    0- Concluir relatório')
    s = int(input())
    # processamento
    while s > 4 or s < 0 :
        print('Número inválido! Informe um número de 0 a 4, de acordo com a situação do mouse, sendo: ')
        print('    1- Necessita da esfera')
        print('    2- Necessita de limpeza')
        print('    3- Necessita de troca de cabo ou conector')
        print('    4- Quebrado ou inutilizado')
        print('    0- Concluir relatório')
        s = int(input())
    if s == 1:
        s1 = 1 + s1
    elif s == 2:
        s2 = 1 + s2
    elif s == 3:
        s3 = 1 + s3
    elif s == 4:
        s4 = 1 + s4
    else:
        st = s1 + s2 + s3 + s4
        s1p = s1 / st * 100
        s2p = s2 / st * 100
        s3p = s3 / st * 100
        s4p = s4 / st * 100
        print(f'                Situação                  |   Quantidade   |  Percentual ')
        print(f'---------------------------------------------------------------------------')
        print(f'1- Necessita da esfera                    |       {s1}        |    {s1p:.2f} %')
        print(f'2- Necessita de limpeza                   |       {s2}        |    {s2p:.2f} %')
        print(f'3- Necessita de troca de cabo ou conector |       {s3}        |    {s3p:.2f} %')
        print(f'4- Quebrado ou inutilizado                |       {s4}        |    {s4p:.2f} %')
        print(f'\n---------------------------------')
        print(f' Total de mouses analisados: {st}')
        print(f'---------------------------------')
        fim = int(input('\n Terminar relatório? Digite o número 1 para SIM ou qualquer valor para contuinuar.'))
        while fim == 1:
            print('\n### Relatório encerrado ###')
            exit()
