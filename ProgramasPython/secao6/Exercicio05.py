#
e = 0
m = 0

#entrada
p = float(input('Quantos kilos você pescou hoje, João? '))
if p > 50:
    e = p - 50
    m = e * 4
print(f'Peso declarado do dia: {p:.1f} kg')
print(f'Excesso de peso: {e:.1f} kg')
print(f'Valor da multa a ser paga: R$ {m:.2f}')
