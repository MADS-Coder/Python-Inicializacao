#Questão 03


num = int(input('Informe um número entre [10] e [99]: '))

n1 = num // 10 % 10
n2 = num // 1 % 10

if n1 % 2 == 1 and n2 % 2 == 1:
    print('Os dois dígitos são ímpares')
elif n1 % 2 != 0:
    print('Apenas um dígito é ímpar.')
elif n2 % 2 != 0:
    print('Apenas um dígito é ímpar.')
else:
    print('Nenhum dígito é ímpar')

