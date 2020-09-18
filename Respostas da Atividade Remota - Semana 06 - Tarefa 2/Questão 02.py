#Questão 02

soma = maior = menor = 0
cont = -1
idade = int(input("Informe a sua idade: "))
while True:
    cont += 1
    soma += idade
    if idade == 0:
        break
    if cont == 1:
        maior = menor = idade
    else:
        if idade > maior:
            maior = idade
        if idade < menor:
            menor = idade
    idade = int(input("Informe a sua idade: "))
    
if soma == 0:
    print()
else:
    media = round(soma / cont, 2)
    print(f'Existem {cont} pessoas, a idade média do grupo é {media}, a maior idade é {maior} e a menor é {menor}.')

