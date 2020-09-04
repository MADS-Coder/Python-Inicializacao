#Questão 03

soma = maior = menor = cont = 0
for c in range(1,6):
    num = int(input(f'Escreva um número {c}º: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'Dos números informados o maior é {maior} e o menor é {menor}.')
    

    
