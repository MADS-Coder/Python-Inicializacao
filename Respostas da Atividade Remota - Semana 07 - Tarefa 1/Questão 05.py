#Questão 05

aves = int(input("Escreva quantidade de aves no inicio do ano 1600: "))

morreram = (6/100)*aves
nascidos = (1/100)*aves
total_populacao = (aves - morreram) + nascidos
populacao_inicial_menos10 = (10/100)*aves
ano = 1600
print(f'{ano},{nascidos:.0f},{morreram:.0f},{total_populacao:.0f}')
while True:
    ano += 1
    if total_populacao > populacao_inicial_menos10:
        nascidos = (1/100)*total_populacao
        morreram = (6/100)*total_populacao
        total_populacao = (total_populacao - morreram) + nascidos
    else:
        break
               
    print(f'{ano},{nascidos:.0f},{morreram:.0f},{total_populacao:.0f}')
