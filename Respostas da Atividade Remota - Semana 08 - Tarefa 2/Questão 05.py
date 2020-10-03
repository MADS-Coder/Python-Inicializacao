#Questão 05

nomes = []
idades = []
alturas = []
soma = 0
cont = -1
for m in range(1,31):
    nome = input("Qual o nome do aluno?: ")
    idade = int(input("Qual a idade do aluno?: "))
    altura = float(input("Qual a altura dele?: "))
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    soma += altura
media = round(soma/m,2)
print('MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA')
for idade in idades:
    cont += 1
    if idade > 13:
        if alturas[cont] < media:
            print(nomes[cont])

