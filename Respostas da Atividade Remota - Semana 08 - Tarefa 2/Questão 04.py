#Questão 04

jogador = []
altura = []
mai = name = soma = 0
cont = -1
for c in range(2,14):
    nome = input("Qual o nome do jogador?: ")
    alt = float(input("Qual a altura do jogador?: "))
    jogador.append(nome)
    altura.append(alt)
    soma += alt
    for alt in altura:
        if alt < 0:
            mai = alt
        else:
            if alt > mai:
                mai = alt
    if c > altura.index(mai):
        c -= 2
        if c == altura.index(mai):
            name = nome
media = round(soma / 12, 2)
print(f'JOGADOR MAIS ALTO DO TIME\n{name}\n{mai:.2f}')
print(f'ALTURA MÉDIA DO TIME\n{media:.2f}')
print(f'JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')
for alt in altura:
    cont += 1
    if alt > media:
        print(f'{jogador[cont]}\n{alt:.2f}')

