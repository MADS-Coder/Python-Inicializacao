#Questão 05

matriz = []
anos = []
mês = []
filial = []
S2014 = []
S2015 = []
S2016 = []
S2017 = []
St = []
M = []
F1 = 'Filial 1'
F2 = 'Filial 2'
F3 = 'Filial 3'
a = 2013
cont = 0
#--------------------------------------------------------------------------------          
for l in range(0, 12):
    linha = []
    mes = 0
    cont += 1
    soma = 0
    F1 = 'Filial 1'
    F2 = 'Filial 2'
    F3 = 'Filial 3'
    if a < 2017:
        a += 1
        anos.append(a)
    else:
        if cont >= 5 and cont <= 8:
            a = 2013
            if a < 2017:
                a += 1
        if cont >= 9 and cont <= 12:
            a = 2013
            if a < 2017:
                a += 1
    for c in range(0, 12):
        num = int(input('Digite um número: '))
        mes += 1
        if mes == 1:
            m = 'Janeiro'
        elif mes == 2:
            m = 'Fevereiro'
        elif mes == 3:
            m = 'Março'
        elif mes == 4:
            m = 'Abril'
        elif mes == 5:
            m = 'Maio'
        elif mes == 6:
            m = 'Junho'
        elif mes == 7:
            m = 'Julho'
        elif mes == 8:
            m = 'Agosto'
        elif mes == 9:
            m = 'Setembro'
        elif mes == 10:
            m = 'Outubro'
        elif mes == 11:
            m = 'Novembro'
        elif mes == 12:
            m = 'Dezembro'
        linha.append(num)
        mês.append(m)
        if 2014 in anos:
            if l == 0:
                F = 'Filial 1'
                print(f'2014;{F};{m};{num}')
                soma += num
                S2014.append(num)
                M.append(S2014)
                if m == 'Dezembro':
                    print(f'TOTAL 2014 {F};{soma}')
            elif l == 1:
                F = 'Filial 2'
                print(f'2014;{F};{m};{num}')
                soma += num
                S2014.append(num)
                if m == 'Dezembro':
                    print(f'TOTAL 2014 {F};{soma}')
            elif l == 2:
                F = 'Filial 3'
                print(f'2014;{F};{m};{num}')
                soma += num
                S2014.append(num)
                if m == 'Dezembro':
                    print(f'TOTAL 2014 {F};{soma}')
                    s = sum(S2014)
                    print(f'TOTAL 2014 TODAS FILIAIS;{s}')          
        if 2015 in anos:
            if l == 3:
                F = 'Filial 1'
                print(f'2015;{F};{m};{num}')
                soma += num
                S2015.append(num)
                if m == 'Dezembro':
                    print(f'TOTAL 2015 {F};{soma}')
            elif l == 4:
                F = 'Filial 2'
                print(f'2015;{F};{m};{num}')
                soma += num
                S2015.append(num)
                if m == 'Dezembro':
                    print(f'TOTAL 2015 {F};{soma}')
            elif l == 5:
                F = 'Filial 3'
                print(f'2015;{F};{m};{num}')
                soma += num
                S2015.append(num)
                if m == 'Dezembro':
                    print(f'TOTAL 2015 {F};{soma}')
                    s = sum(S2015)
                    print(f'TOTAL 2015 TODAS FILIAIS;{s}') 
        if 2016 in anos:
            if l == 6:
                F = 'Filial 1'
                print(f'2016;{F};{m};{num}')
                soma += num
                S2016.append(num)
                if m == 'Dezembro':
                    print(f'TOTAL 2016 {F};{soma}')
            elif l == 7:
                F = 'Filial 2'
                print(f'2016;{F};{m};{num}')
                soma += num
                S2016.append(num)
                if m == 'Dezembro':
                    print(f'TOTAL 2016 {F};{soma}') 
            elif l == 8:
                F = 'Filial 3'
                print(f'2016;{F};{m};{num}')
                soma += num
                S2016.append(num)
                if m == 'Dezembro':
                    print(f'TOTAL 2016 {F};{soma}')
                    s = sum(S2016)
                    print(f'TOTAL 2016 TODAS FILIAIS;{s}') 
        if 2017 in anos:
            if l == 9:
                F = 'Filial 1'
                print(f'2017;{F};{m};{num}')
                soma += num
                S2017.append(num)
                if m == 'Dezembro':
                    print(f'TOTAL 2017 {F};{soma}')
            elif l == 10:
                F = 'Filial 2'
                print(f'2017;{F};{m};{num}')
                soma += num
                S2017.append(num)
                if m == 'Dezembro':
                    print(f'TOTAL 2017 {F};{soma}')
            elif l == 11:
                F = 'Filial 3'
                print(f'2017;{F};{m};{num}')
                soma += num
                S2017.append(num)
                if m == 'Dezembro':
                    print(f'TOTAL 2017 {F};{soma}')
                    s = sum(S2017)
                    print(f'TOTAL 2017 TODAS FILIAIS;{s}')
    St = S2014+S2015+S2016+S2017
    s = sum(St)
    matriz.append(linha)
print(f'TOTAL PERÍODO TODAS FILIAIS;{s}')
#--------------------------------------------------------------------------------
for l in range(0, 12):
    for c in range(0, 12):
        print(f'[{matriz[l][c]}]',end=' ')
    print()
#--------------------------------------------------------------------------------    

