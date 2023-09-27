#entradas
valor_por_hora = float(input('Quanto você ganha por hora? '))
horas_trabalhadas = int(input('Qauntas horas você trabalhou por mês? '))
#processamento
salario = horas_trabalhadas * valor_por_hora
#saida
print(f'Neste mês você irá receber R$ {salario:.2f} .')
