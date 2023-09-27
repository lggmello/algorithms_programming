#entrada
idade = int(input('Informe a idade do nadador: '))
#processamento
if idade >= 5 and idade <= 7:
    print('Entrar no infantil A')
elif idade >= 8 and idade <= 11:
    print('Entrar no infantil B')
elif idade >= 12 and idade <= 13:
    print('Entrar no juvenil A')
elif idade >= 14 and idade <= 17:
    print('Entrar no juvenil B')
elif idade >= 18:
    print('Adulto')
else:
    print('Nadador com idade inferior ao mínimo permitido.')
