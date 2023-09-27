#variaveis
maior = -999
menor = 999
soma = 0
#entrada
for v in range(1, 11):
    valor = int(input(f'Digite o valor {v} inteiro e positivo: '))
    while valor < 0:
        valor = int(input(f'O valor deve ser inteiro e POSITIVO. Digite outro valor {v}: '))
    #processamento
    if valor > maior:
        maior = valor
    elif menor == -1 or valor < menor:
        menor = valor
    soma = soma + valor  
#saida
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
print(f'Média dos 10 valores: {soma / 10}')
