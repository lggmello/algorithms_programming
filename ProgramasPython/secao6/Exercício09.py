#entrada
indice = float(input('Insira o índice de poluição: '))
#processamento
if indice >= 0.3 and indice < 0.4:
    print('Atenção. Indústrias do grupo 1 devem suspender as atividades.')
elif indice >= 0.4 and indice < 0.5:
    print('Atenção. Indústrias do grupo 1 e grupo 2 devem suspender as atividades.')
elif indice >= 0.5:
    print('Atenção. TODAS indústrias devem suspender as atividades.')
else:
    print('Níveis aceitáveis.')