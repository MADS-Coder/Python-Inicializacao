#Questão 04

n1 = int(input('Escreva qualquer número: '))
n2 = int(input('Escreva qualquer número: '))
n3 = int(input('Escreva qualquer número: '))
n4 = int(input('Escreva qualquer número: '))
n5 = int(input(f'Escreva qualquer número: '))

maior = 0
media = (n1+n2+n3+n4+n5) / 5
    
if (n1 > media < n2):
    maior = '{:.2f},{:.2f}'.format(n1, n2)
if (n3 > media < n4):
    maior = '{:.2f},{:.2f},{:.2f}'.format(maior, n3, n4)
if n5 > media:
    maior = '{:.2f},{:.2f}'.format(maior, n5)

print(f'A média é {media}.')
print(f'Os maiores números acima da média são {maior}.')

