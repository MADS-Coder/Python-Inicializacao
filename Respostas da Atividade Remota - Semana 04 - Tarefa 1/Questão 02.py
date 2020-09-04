#Questão 02


dia1 = int(input('Informe um dia: '))
mes1 = int(input('Informe um mês: '))
ano1 = int(input('Informe um ano: '))

dia2 = int(input('\nInforme um dia: '))
mes2 = int(input('Informe um mês: '))
ano2 = int(input('Informe um ano: '))

data1 = '{:02d}/{:02d}/{}'.format(dia1, mes1, ano1)
data2 = '{:02d}/{:02d}/{}'.format(dia2, mes2, ano2)

print(f'\nA primeira data informada é {data1}.')
print(f'A segunda data informada é {data2}.')

if ano1 > ano2:
    print(f'\nPortanto a data mais recente informada é {data1}.')

else:
    print(f'\nPortanto a data mais recente informada é {data2}.')
