#Questão 05

cont = 1
soma = 0
for n in range (1,4):
    print(f"Digite a {cont}º do aluno: ", end='')
    nota = float(input())
    cont += 1
    soma += nota
    media = soma / 3
    
if n == 3:
    if nota >= 8:
        media += 1
        if media > 10:
            media = 10
print(f'A média do aluno é {media:.1f}')


