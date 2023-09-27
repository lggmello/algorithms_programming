#entrada
i = float(input('Digite a altura da pessoa, em metros: '))
s = input("Informe o sexo da pessoa, digitando 'M' para sexo masculino ou 'F' para sexo feminino: ")
#processamento
if s.lower() == 'm':
    pi = (72.7 * i) - 58
    # saida a
    print(f"A pessoa do sexo masculino, que mede {i} m de altura, tem o peso ideal de {pi:.1f} kg." )
elif s.lower() == 'f':
    pi = (62.1 * i) - 44.7
    #saida b
    print(f"A pessoa do sexo feminino, que mede {i} m de altura, tem o peso ideal de {pi:.1f} kg." )
else:
    #saida c
    print("Opção inválida de sexo! Favor reiniciar o programa e digitar 'M' para sexo masculino ou 'F' para sexo feminino: ")
