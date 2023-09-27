#entradas
a = input('Informe o nome: ')
b = input('Informe a senha: ')
#processamento
while a == b:
    print('A senha não pode ser igual ao nome!')
    a = input('Informe o nome: ')
    b = input('Informe a senha: ')
#saida
print(f'Bem vindo {a}!')
