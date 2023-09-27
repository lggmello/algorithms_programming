#variaveis
maior = 0
#entrada
valor = int(input('Digite um valor: '))
while valor != 0 :
    if valor > maior:
        maior = valor
    valor = int(input('Digite outro valor: '))
#saida
print(f'Maior valor declarado: {maior}')
