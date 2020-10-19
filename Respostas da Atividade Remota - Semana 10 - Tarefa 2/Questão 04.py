#Questão 04

corredor = {}
lista = []
ordenada = {}
cont = 0
#-----------------------------------------------------------
for l in range(1, 7):
    cont += 1
    soma = media = men = mai = 0
    corredor["nome"] = input()
    for c in range(1, 11):
        corredor["tempo"] = float(input())
        soma = round(soma + corredor["tempo"], 2)
        media = round(soma/10, 1)
        if men == 0:
            men = corredor["tempo"]
        else:
            if corredor["tempo"] < men:
                men = corredor["tempo"]
                
    ordenada["Ordem"] = cont
    ordenada["Nome do Corredor"] = corredor["nome"]
    ordenada["Tempo Total"] = soma
    ordenada["Tempo Médio"] = media
    ordenada["Melhor Volta"] = men

    if cont == 1:
        for k in ordenada.keys():
            print(f'{k:^15}',end='')
        print()
        
    for v in ordenada.values():
        print(f'{v:^15}',end='')
    print()

























    
'''    if cont <= 1:
        for n in ordenada.keys():
            t = len(n)
            print(f'{"-"}'*t,'|',end=' ')
        print()
        for k in ordenada.keys():
            print(f'{k:^18}|',end='')
        print()
        for n in ordenada.keys():
            t = len(n)
            print(f'{"-":^1}'*t,'|',end='')
        print()
    for k, v in ordenada.items():
        print(f'{v:^18}|',end='')
    print()'''


