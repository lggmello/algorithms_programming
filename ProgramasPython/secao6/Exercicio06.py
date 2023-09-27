#entrada
e = 0
vh = 10
vhe = 20
c = input('Código de usuário: ')
n = float(input('Horas trabalhadas na semana: '))
#processamento
if n > 50 :
    e = n - 50
    n = n - e
    
extra = e * vhe
salario = n * vh
total = extra + salario

#saida
print(f'Salário: R$ {salario:.2f}')
print(f'Extra: R$ {extra:.2f}')
print(f'Total a receber na semana: R$ {total:.2f}')
