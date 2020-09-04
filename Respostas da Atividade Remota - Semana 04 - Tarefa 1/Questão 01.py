#Questão 01

dia = int(input('Informe qual o dia atual: '))
mes = int(input('Informe qual o mês atual: '))
ano = int(input('Informe qual o ano atual: '))
dia_nasc = int(input('\nInforme o seu dia de nascimento: '))
mes_nasc = int(input('Informe o seu dia de nascimento: '))
ano_nasc = int(input('Informe o seu dia de nascimento: '))

data_atual = '{:02d}/{:02d}/{}'.format(dia, mes, ano)
data_nasc = '{:02d}/{:02d}/{}'.format(dia_nasc, mes_nasc, ano_nasc)

d1 = ano
d2 = ano_nasc

idade = abs(d1 - d2)

print(f'\nA data informada é {data_atual}.')
print(f'A sua data de nascimento é {data_nasc}.')
print(f'\nPortanto você tem {idade} anos de idade.')

