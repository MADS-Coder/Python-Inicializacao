#Questão 01

nome = str(input('Informe seu nome: '))
estado_civil = str(input('Digite [C] para Casado(a) ou [S] para Solteiro(a): '))

if estado_civil in 'Cc1':
    conjuge = str(input('Informe o nome do(a) Cônjuge: '))
    caracestado_civil = len(nome)
    caracconjuge = len(conjuge)
    caracteretot = (caracestado_civil + caracconjuge)
    print(f'O total de caractere com o seu nome e do seu(a) cônjuge é {caracteretot}.')
else:
    caractere = len(nome)
    print(f'O total de caractere com o seu nome é {caractere}.')



