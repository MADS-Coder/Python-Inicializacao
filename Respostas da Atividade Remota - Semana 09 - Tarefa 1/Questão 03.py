#Questão 03

def carrega_cidades():
    resultado = []
    d = str(int(input("Digite um dia: ")))
    me = str(int(input("Digite um mês: ")))
    res_mes = mês(int(me))
    print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {d} DE {res_mes}:')
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            for n in (1,5558):
                if dia == d and mes == me:
                    print(f'{nome} ({uf})')
                    resultado.append(nome)    
                    break
                        
    arquivo.close()
    return resultado

def mês(m):
    
    if m == 1:
        m = 'JANEIRO'
    elif m == 2:
        m = 'FEVEREIRO'
    elif m == 3:
        m = 'MARÇO'
    elif m == 4:
        m = 'ABRIL'
    elif m == 5:
        m = 'MAIO'
    elif m == 6:
        m = 'JUNHO'
    elif m == 7:
        m = 'JULHO'
    elif m == 8:
        m = 'AGOSTO'
    elif m == 9:
        m = 'SETEMBRO'
    elif m == 10:
        m = 'OUTUBRO'
    elif m == 11:
        m = 'NOVEMBRO'
    elif m == 12:
        m = 'DEZEMBRO'
        
    return m            

cidades = carrega_cidades()


